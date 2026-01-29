import time
from datetime import datetime
import os

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 40)
        print("AESALNET STATUS DASHBOARD")
        print("Time:", datetime.now().isoformat(timespec="seconds"))
        print("Status: ONLINE")
        print("PID:", os.getpid())
        print("=" * 40)
        time.sleep(2)

if __name__ == "__main__":
    main()
import time
from datetime import datetime

def main():
    while True:
        print("=" * 40)
        print("AESALNET STATUS DASHBOARD")
        print("Time:", datetime.now().isoformat(timespec="seconds"))
        print("Status: ONLINE")
        print("=" * 40)
        time.sleep(2)

if __name__ == "__main__":
    main()
