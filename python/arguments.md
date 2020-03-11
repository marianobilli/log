
This library allows to quickly add parameters to a python program. And will also enable to call the program with the --help parameter for more info

```
import argparse
```

Initial object setup with program main description
```
parser = argparse.ArgumentParser(description='This is a demo program.')
```

Simple argument with help message
```
parser.add_argument('--arg1', help='Some descriptive text')
```

Argument with default value
```
parser.add_argument('--arg2', default='somevalue')
```

Arrgument with only some available actions:
```
parser.add_argument('--action', help='To force START/STOP', choices=['START', 'STOP'])
```


Finally to parse the arguments into a dictionary
```
args = vars(parser.parse_args())
```


And to get the value:
```
parameter_value = args['arg1']
```

example output using no parameters
```
[Running] python -u "/Users/mbilling/github/log/python/arguments_example.py"
{'arg1': None, 'arg2': 'somevalue', 'action': None}
```

Using the `--help` parameter
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