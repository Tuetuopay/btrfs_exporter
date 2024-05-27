# BTRFS exporter

Prometheus exporter for BTRFS volumes.

## Howto

```
pip3 install btrfs flask
FLASK_APP=btrfs_exporter.py STAT_URL=/metrics flask run --host=127.0.0.1 --port 9101
```

Sample output:

```
$ curl localhost:9101/metrics
node_btrfs_fs_bytes_raw_total{mountpoint="/",profile="single",type="Data",device="/dev/sdk1"} 116790394880
node_btrfs_fs_bytes_raw_total{mountpoint="/",profile="single",type="System",device="/dev/sdk1"} 4194304
node_btrfs_fs_bytes_raw_total{mountpoint="/",profile="single",type="Metadata",device="/dev/sdk1"} 1082130432
node_btrfs_fs_bytes_raw_total{mountpoint="/",profile="single",type="GlobalReserve",device="/dev/sdk1"} 52510720
node_btrfs_fs_bytes_used{mountpoint="/",profile="single",type="Data",device="/dev/sdk1"} 25820164096
node_btrfs_fs_bytes_used{mountpoint="/",profile="single",type="System",device="/dev/sdk1"} 16384
node_btrfs_fs_bytes_used{mountpoint="/",profile="single",type="Metadata",device="/dev/sdk1"} 239222784
node_btrfs_fs_bytes_used{mountpoint="/",profile="single",type="GlobalReserve",device="/dev/sdk1"} 0
node_btrfs_fs_bytes_total{mountpoint="/",profile="single",type="Data",device="/dev/sdk1"} 116790394880
node_btrfs_fs_bytes_total{mountpoint="/",profile="single",type="System",device="/dev/sdk1"} 4194304
node_btrfs_fs_bytes_total{mountpoint="/",profile="single",type="Metadata",device="/dev/sdk1"} 1082130432
node_btrfs_fs_bytes_total{mountpoint="/",profile="single",type="GlobalReserve",device="/dev/sdk1"} 52510720
node_btrfs_dev_bytes_total{mountpoint="/",devpath="/dev/sdk1",device="/dev/sdk1",devid="1"} 120032591872
node_btrfs_dev_bytes_used{mountpoint="/",devpath="/dev/sdk1",device="/dev/sdk1",devid="1"} 117876719616
node_btrfs_dev_corruption_errors{mountpoint="/",devpath="/dev/sdk1",device="/dev/sdk1",devid="1"} 0
node_btrfs_dev_flush_errors{mountpoint="/",devpath="/dev/sdk1",device="/dev/sdk1",devid="1"} 0
node_btrfs_dev_generation_errors{mountpoint="/",devpath="/dev/sdk1",device="/dev/sdk1",devid="1"} 0
node_btrfs_dev_read_errors{mountpoint="/",devpath="/dev/sdk1",device="/dev/sdk1",devid="1"} 0
node_btrfs_dev_write_errors{mountpoint="/",devpath="/dev/sdk1",device="/dev/sdk1",devid="1"} 0
node_btrfs_fs_bytes_raw_used{mountpoint="/",profile="single",type="Data",device="/dev/sdk1"} 25820164096
node_btrfs_fs_bytes_raw_used{mountpoint="/",profile="single",type="System",device="/dev/sdk1"} 16384
node_btrfs_fs_bytes_raw_used{mountpoint="/",profile="single",type="Metadata",device="/dev/sdk1"} 239222784
node_btrfs_fs_bytes_raw_used{mountpoint="/",profile="single",type="GlobalReserve",device="/dev/sdk1"} 0
```

## License

```
----------------------------------------------------------------------------
"THE BEER-WARE LICENSE" (Revision 42):
<tuetuopay@me.com> wrote this file.  As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return.   Tuetuopay
----------------------------------------------------------------------------
```
