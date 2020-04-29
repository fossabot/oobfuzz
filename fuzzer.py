import argparse, sys
from oobfuzz import OOBFuzz

parser = argparse.ArgumentParser(prog='OOBFuzz')
parser.add_argument('--output', type=str, help='File to output result to')
parser.add_argument('--callback', type=str, help='Callback server')
parser.add_argument('--target', type=str, help='Single target to run against')
parser.add_argument('--targets', type=str, help='File with newline seperator including several targets')

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

output = args.output if args.output else None
callback = args.callback if args.callback else None
target = args.target if args.target else None
targets = args.targets if args.targets else None

oobfuzz = OOBFuzz(output, callback, target, targets)
oobfuzz.run()