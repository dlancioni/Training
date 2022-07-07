import argparse

# usage:
# python cmd.py: do nothing
# python cmd.py --help: print available argumentos (-g -r) and its description
# python cmd.py --r recon.json: do nothing
# python cmd.py --g group.json: do nothing

parser = argparse.ArgumentParser()
parser.add_argument("--g", help="json file that groups the recons")
parser.add_argument("--r", help="json file with single recon")
args = parser.parse_args()
if args.g:
    print("Importing a group of recons...", args.g)

if args.r:
    print("Importing a single recon...", args.r)


    
    
