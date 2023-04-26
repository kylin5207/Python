import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--a", type=int, help="first parameter")
parser.add_argument("--b", type=int, help="second parameter")
args = parser.parse_args()

if args.a and args.b:
    result = args.a + args.b
    print("The sum of a and b is:", result)
else:
    print("Please provide both parameters using --a and --b.")
