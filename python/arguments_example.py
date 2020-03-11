import argparse

parser = argparse.ArgumentParser(description='This is a demo program.')
parser.add_argument('--arg1', help='Some descriptive text')
parser.add_argument('--arg2', default='somevalue')
parser.add_argument('--action', help='To force START/STOP', choices=['START', 'STOP'])

args = vars(parser.parse_args())

print(args)