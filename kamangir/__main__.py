import argparse
from kamangir import NAME, VERSION
from kamangir import README
from kamangir.logger import logger
from blueness.argparse.generic import sys_exit

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="build_README|version",
)
args = parser.parse_args()

success = False
if args.task == "version":
    print(f"{NAME}-{VERSION}")
    success = True
elif args.task == "build_README":
    success = README.build()
else:
    success = None

sys_exit(logger, NAME, args.task, success)
