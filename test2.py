import argparse
parser = argparse.ArgumentParser(exit_on_error=False)
parser.add_argument("square", type=int,
                    help="display the square of a given number")
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")
try:
    print("-- Start of try block")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbosity == 2:
        print(f"the square of {args.square} equals {answer}")
    elif args.verbosity == 1:
        print(f"{args.square}^2 == {answer}")
    else:
        print(answer)
    print("-- End of try block")
except Exception as e:
    print("-- Start of except block")
    print(e)
    print("-- End of except block")

