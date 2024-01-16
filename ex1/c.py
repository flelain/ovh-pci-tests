import argparse
from art import text2art


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str, help="Text to convert to ASCII art.")
    args = parser.parse_args()

    print(text2art(args.text))


if __name__ == "__main__":
    main()
