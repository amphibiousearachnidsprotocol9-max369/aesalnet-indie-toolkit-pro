import os
import psutil
from datetime import datetime

def get_status():
    return {
        "time": datetime.now().isoformat(timespec="seconds"),
        "cpu": psutil.cpu_percent(interval=None),
        "memory": psutil.virtual_memory().percent,
        "pid": os.getpid(),
        "state": "ONLINE",
    }
