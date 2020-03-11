it is usefull to prepare this dictionary
```
loglevel_map = {'DEBUG': logging.DEBUG,
                'INFO': logging.INFO,
                'WARN': logging.WARN,
                'ERROR': logging.ERROR}
```

Also to use `argparse` library to set the log level by paramter
```
parser.add_argument('--loglevel', help='loglevel of the application', default='INFO', choices=['DEBUG', 'INFO', 'WARN', 'ERROR'])
```

Initial setup
```
import logging

logging.basicConfig(stream=sys.stdout, 
                    level=loglevel_map[args['loglevel']],
                    format="time: %(asctime)s - name: %(name)s - level: %(levelname)s - message: %(message)s")
```

To get a log object
```
log = logging.getLogger('MAIN')
```

To write a log
```
log.info("No actions taken")
```