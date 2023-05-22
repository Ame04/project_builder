#!/usr/bin/python3

import argparse
from main_folder_creation import create_main_folder
from optional_folders_creation import create_optional_folder
import utils

def get_parser() -> argparse.ArgumentParser:
    ''' Construct and return the paser object with all the options '''
    # Create an argument parser object
    parser = argparse.ArgumentParser(prog="Project builder",
                                     description="Build a squeletton of a project"
                                                 " with the needed folders",
                                    )

    # Add arguments
    parser.add_argument("repo_url",
                        nargs="?",
                        help="The URL of you repository to clone from"
                        )
    parser.add_argument("--interactive", "-i",
                        action="store_true",
                        help="To launch the scrypt in interactive mode"
                        )
    parser.add_argument("--layout_path","-l",
                        help="Path to your project layout,"
                        " if not set the default layout will be used"
    )
    parser.add_argument("--output", "-o",
                        default="./",
                        help="The path where to put you new project"
                        )
    parser.add_argument("--project_part", "-p",
                        nargs="*",
                        default=["meca", "elec", "code"],
                        help="The part you want to put in your project"
                        )

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
    project = utils.Project(args=args)
    create_main_folder(project=project)
    create_optional_folder(project=project)

