import sys


def print_args(args):
    print(' '.join(args))


def main():
    if len(sys.argv) <= 1:
        print("No arguments were provided. Please provide at least one argument.")
    else:
        print_args(sys.argv[1:])


if __name__ == "__main__":
    main()
