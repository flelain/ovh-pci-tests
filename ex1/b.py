import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", required=True, choices=['titi', 'toto', 'tata'],
                        help="target can be 'titi', 'toto' or 'tata'")
    args = parser.parse_args()

    print(args.target)


if __name__ == "__main__":
    main()
