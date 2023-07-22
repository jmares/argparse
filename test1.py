import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--language", help="select source language")
parser.add_argument("-t", "--tag", help="select tag")
parser.add_argument("-n", "--number", help="select number of words", type=int)
args = parser.parse_args()
print(args)

if args.language:
    print("Language set to ", args.language)
else:
    print("Lamguage not set")
