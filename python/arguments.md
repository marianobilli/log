
This library allows to quickly add parameters to a python program. And will also enable to call the program with the --help parameter for more info

```
import argparse
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