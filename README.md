# BTRFS exporter

Prometheus exporter for BTRFS volumes.

## Howto

```
pip3 install btrfs flask
FLASK_APP=btrfs_exporter.py STAT_URL=/metrics flask run --host=127.0.0.1 --port 9101
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
