import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you want here")
args = parser.parse_args()
print(args.echo)