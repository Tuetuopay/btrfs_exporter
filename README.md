# BTRFS exporter

Prometheus exporter for BTRFS volumes.

## Howto

```
pip3 install btrfs flask
FLASK_APP=btrfs_exporter.py STAT_URL=/metrics flask run --host=127.0.0.1 --port 9101
```
