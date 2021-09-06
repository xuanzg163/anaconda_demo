
import logging
import datetime

format = '[%(asctime)s  %(filename)s  %(levelname)s]: %(message)s'

logging.basicConfig(filename='./logs/'+__name__+datetime.datetime.now().strftime("%Y%m%d")+'.log',
                    format=format,
                    level = logging.DEBUG,
                    filemode='a',
                    datefmt='%Y-%m-%d%I:%M:%S'
                    )
logger = logging.getLogger(__name__)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(logging.Formatter(format))

logger.addHandler(console)


