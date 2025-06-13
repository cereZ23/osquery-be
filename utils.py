# utils.py
from datetime import datetime

RECEIVED_REQUESTS = []

EXAMPLE_CONFIG = {
    "schedule": {
        "tls_proc": {"query": "select * from processes", "interval": 10}
    },
    "node_invalid": False
}

def debug(msg):
    print(f"[DEBUG] {datetime.now().isoformat()} - {msg}")
