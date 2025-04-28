import hashlib
import sys


def hash_function(data):
    hasher = hashlib.sha256()
    hasher.update(data)
    return hasher.digest()


def main():
    if len(sys.argv) != 2:
        print(f"вы указали: {sys.argv[0]}", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    try:
        with open(input_path, "rb") as f:
            data = f.read()
    except OSError as e:
        print(f"ошибка - {e}", file=sys.stderr)
        sys.exit(1)
    digest = hash_function(data)
    print(digest.hex())


if __name__ == "__main__":
    main()
