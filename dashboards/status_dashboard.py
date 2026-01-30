import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import time
import os
from src.status import get_status

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        status = get_status()

        print("=" * 40)
        print("AESALNET STATUS DASHBOARD")
        print("Time:", status["time"])
        print("CPU Usage:", f'{status["cpu"]}%')
        print("Memory Usage:", f'{status["memory"]}%')
        print("Disk Usage:", f'{status["disk"]}%')
        print("Net Sent:", status["net_sent"])
        print("Net Recv:", status["net_recv"])
        print("Uptime (s):", status["uptime_sec"])
        print("Status:", status["state"])
        print("PID:", status["pid"])
        print("=" * 40)

        time.sleep(2)

if __name__ == "__main__":
    main()
