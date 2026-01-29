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
