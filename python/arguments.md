
This library allows to quickly add parameters to a python program. And will also enable to call the program with the --help parameter for more info

# Full example
```
import argparse

parser = argparse.ArgumentParser(description='This is a demo program.')
parser.add_argument('--arg1', help='Some descriptive text')
parser.add_argument('--arg2', default='somevalue')
parser.add_argument('--action', help='To force START/STOP', choices=['START', 'STOP'])

args = vars(parser.parse_args())

print(args)
```

# Using the `--help` parameter
```
$ python3 arguments_example.py --help
usage: arguments_example.py [-h] [--arg1 ARG1] [--arg2 ARG2]
                            [--action {START,STOP}]

This is a demo program.

optional arguments:
  -h, --help            show this help message and exit
  --arg1 ARG1           Some descriptive text
  --arg2 ARG2
  --action {START,STOP} To force START/STOP
```
