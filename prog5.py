import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase out verbosity", action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")