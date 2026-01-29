import time
from datetime import datetime
import os
import psutil

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        cpu = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory()

        print("=" * 40)
        print("AESALNET STATUS DASHBOARD")
        print("Time:", datetime.now().isoformat(timespec="seconds"))
        print("CPU Usage:", f"{cpu}%")
        print("Memory Usage:", f"{mem.percent}%")
        print("Status: ONLINE")
        print("PID:", os.getpid())
        print("=" * 40)

        time.sleep(2)

if __name__ == "__main__":
    main()
