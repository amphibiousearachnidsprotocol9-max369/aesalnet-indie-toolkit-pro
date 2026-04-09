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
        print("Status:", status["state"])
        print("PID:", status["pid"])
        print("=" * 40)

        time.sleep(2)

if __name__ == "__main__":
    main()
