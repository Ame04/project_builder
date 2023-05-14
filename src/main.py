#!/usr/bin/python3

import argparse

def get_parser() -> argparse.ArgumentParser:
    ''' Construct and return the paser object with all the options '''
    # Create an argument parser object
    parser = argparse.ArgumentParser(prog="Project builder",
                                     description="Build a squeletton of a project"
                                                 " with the needed folders",
                                    )

    # Add arguments
    parser.add_argument("project_part",
                        nargs="*",
                        choices=["meca", "elec", "code"],
                        help="The part you want to put in your project"
                        )
    parser.add_argument("--interactive", "-i",
                        action="store_true",
                        help="To launch the scrypt in interactive mode")

    return parser

def main(args):
    ''' The main part of the script '''


if __name__=="__main__":
    # Parse the arguments
    parser = get_parser()
    args = parser.parse_args()
    print("Let's have a project with : " + str(args.project_part))
    if args.interactive:
        print("Script launched in interactive mode")

