
import argparse
from unit import logger



def run():
    parsers = argparse.ArgumentParser(description="you need some flags to run function!!!")
    parsers.add_argument("--mode","--m",action="store_true",help="build mode")
    parsers.add_argument("--all","--a",action="store_true",help="build a new robot",default=True)
    args = parsers.parse_args()
    if args.mode:
        logger.info("begin build a")
    elif args.all:
        logger.info("begin build all")
    else:
        logger.info("build args not exits!")


if __name__ == '__main__':
    run()
