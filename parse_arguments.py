"""Module for handling all the arguments related things."""
import argparse


def parse_arguments():
    """Arg parse.

    Args: None

    Returns:
        args (Argparse object): Argument object which contain details of all the command line arguments.
    """
    # Create the parser and add arguments
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)

    # Add arguments
    group.add_argument('-c', '--clone', help="Action type",
                       action='store_true')
    group.add_argument('-uc', '--unclone',
                       help="Action type for uncloning", action='store_true')
    parser.add_argument(
        '-d', '--main-doc-name', help="Specify the doc name that you want to copy", required=True)
    parser.add_argument('-sr', '--source-region',
                        help="Specify the region from which you want to copy", required=True)
    parser.add_argument('-dr', '--destination-regions',
                        help="Specify the regions in which we want to copy", required=True)

    args = parser.parse_args()
    return args
