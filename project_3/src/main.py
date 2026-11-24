"""Entry point for the Expense Tracker."""

import yaml
from argparse import ArgumentParser

from application import expense
from ui.cli_user_interface import expense_entry


def main():
    args = configure_and_parse_commandline_arguments()

    if args.configfile:
        config = None
        with open(args.configfile, "r") as f:
            config = yaml.load(f.read(), Loader=yaml.SafeLoader)

    expense_entry(expense)


def configure_and_parse_commandline_arguments():
    """Configure and parse command-line arguments."""
    parser = ArgumentParser(
        prog="main.py",
        description="Start the Expense Tracker from a configuration file",
    )
    parser.add_argument(
        "-c",
        "--configfile",
        help="Configuration file to load",
        required=True,
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()