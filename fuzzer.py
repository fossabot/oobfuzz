import argparse, sys
from oobfuzz import OOBFuzz

parser = argparse.ArgumentParser(prog='OOBFuzz')
parser.add_argument('--output', type=str, help='File to output result to')
parser.add_argument('--threads', type=int, help='Number of threads to fuzz (default: 5)')
parser.add_argument('--target', type=str, help='Single target to run against')
parser.add_argument('--targets', type=str, help='File with newline seperator including several targets')
parser.add_argument('--exclude', type=str, help='String of response codes seperated by "," (example 404,401,403) to exclude from printing')
parser.add_argument('--proxy', type=str, help='Proxy to route through (example "http://localhost:8080")')
parser.add_argument('--blocks', type=int, help='Amount of blocks registered to exit (default: 5). This means that if 5 blocks are registered the fuzzer will exit')
parser.add_argument('--redir', help='Allow HTTP redirects', action="store_true")



if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

output = args.output if args.output else None
callback = args.threads if args.threads else 5
target = args.target if args.target else None
targets = args.targets if args.targets else None
exclude = args.exclude if args.exclude else None
proxy = args.proxy if args.proxy else None
blocks = args.blocks if args.blocks else 5
redir = args.redir if args.redir else False


oobfuzz = OOBFuzz(output, callback, target, targets, exclude, proxy, blocks, redir)