from pathlib import Path

def main():
    for p in Path(".").iterdir():
        print(p.name)

if __name__ == "__main__":
    main()
