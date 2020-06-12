import argparse


def get_parser():
    parser = argparse.ArgumentParser(description="whereis")

    parser.add_argument("path", type=str, help="Path to start searching from.")
    parser.add_argument("pattern", type=str, help="Pattern to search for."
                                                  "Can be regex or regular string")

    return parser.parse_args()
