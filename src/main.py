import argparse

def main():
    parser = argparse.ArgumentParser(description="AESALNET Indie Toolkit")
    parser.add_argument("--status", action="store_true", help="Show status")
    args = parser.parse_args()

    if args.status:
        print("Toolkit status: ONLINE")
    else:
        print("AESALNET Indie Toolkit online")

if __name__ == "__main__":
    main()
def main():
    print("AESALNET Indie Toolkit online")

if __name__ == "__main__":
    main()
