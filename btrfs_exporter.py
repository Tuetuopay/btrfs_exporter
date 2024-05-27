#!/usr/bin/env python3

# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <tuetuopay@me.com> wrote this file.  As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return.   Tuetuopay
# ----------------------------------------------------------------------------

import os, btrfs, psutil, time

class FS:
    def __init__(self, device, mount):
        self.device = device
        self.mount = mount
        self.btrfs = btrfs.FileSystem(mount)

    def get_stats(self):
        stats = {
            "dev_bytes_total": [],    "dev_bytes_used": [],
            "dev_corruption_errs": [], "dev_flush_errs": [],
            "dev_generation_errs": [], "dev_read_errs": [],
            "dev_write_errs": [],
            "fs_bytes_total": [],     "fs_bytes_used": [],
            "fs_bytes_raw_total": [], "fs_bytes_raw_used": []
        }

        for dev in self.btrfs.devices():
            di = self.btrfs.dev_info(dev.devid)
            s = self.btrfs.dev_stats(dev.devid)
            key = {"devid": dev.devid, "devpath": di.path.replace("\x00", "")}
            stats["dev_bytes_used"].append((key, di.bytes_used))
            stats["dev_bytes_total"].append((key, di.total_bytes))
            stats["dev_corruption_errs"].append((key, s.corruption_errs))
            stats["dev_flush_errs"].append((key, s.flush_errs))
            stats["dev_generation_errs"].append((key, s.generation_errs))
            stats["dev_read_errs"].append((key, s.read_errs))
            stats["dev_write_errs"].append((key, s.write_errs))

        for si in self.btrfs.space_info():
            key = {
                "type": btrfs.utils.block_group_type_str(si.flags),
                "profile": btrfs.utils.block_group_profile_str(si.flags)
            }
            stats["fs_bytes_total"].append((key, si.total_bytes))
            stats["fs_bytes_used"].append((key, si.used_bytes))
            stats["fs_bytes_raw_total"].append((key, si.raw_total_bytes))
            stats["fs_bytes_raw_used"].append((key, si.raw_used_bytes))

        return stats

filesystems = []
def __prepare__():
    global filesystems

    # Prepare filesystem stuff
    mounts = [(p.device, p.mountpoint) for p in psutil.disk_partitions()
                   if p.fstype == "btrfs"]

    mounts.sort()
    i = 0
    while i < len(mounts) - 1:
        if mounts[i][0] == mounts[i + 1][0]:
            del mounts[i + 1]
        else:
            i += 1

    filesystems = [FS(mount[0], mount[1]) for mount in mounts]
__prepare__()

# Setup Flask web server
from flask import Flask
app = Flask(__name__)

# Global stat cache
global_stats, stats_timestamp = [], 0

def dict2gostr(dict):
    l = []
    for key in dict:
        l.append('{}="{}"'.format(key, dict[key]))
    return "{" + (",".join(l)) + "}"

@app.route(os.environ.get("STAT_URL", "/"))
def get_data():
    global global_stats, stats_timestamp

    # If stats were not updated in the last 5 seconds
    if time.time() - stats_timestamp > 5.0:
        stats_timestamp = time.time()
        global_stats = [(fs, fs.get_stats()) for fs in filesystems]
        app.logger.debug("Refreshed cache")

    stats = []
    for fs, fs_stats in global_stats:
        for name in fs_stats:
            for stat in fs_stats[name]:
                attr = dict(stat[0])
                attr["mountpoint"] = fs.mount
                attr["device"] = fs.device
                stats.append("node_btrfs_{}{} {}".format(name, dict2gostr(attr), stat[1]))
    return "\n".join(stats)
