#!/usr/bin/python3

import argparse
from main_folder_creation import create_main_folder

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
    parser.add_argument("--output", "-o",
                        default="./",
                        help="The path where to put you new project"
                        )
    parser.add_argument("--project_part", "-p",
                        nargs="*",
                        choices=["meca", "elec", "code"],
                        help="The part you want to put in your project"
                        )
    return parser

def main(args):
    ''' The main part of the script '''

class Project():
    ''' Class to propagate informations between scripts '''
    interactive:bool=False
    output:str=None
    project_part:list=None
    repo_url:str=None

    def __init__(self, args):
        ''' Initialyse the class with info from the arg parser '''
        self.interactive = args.interactive
        self.output = args.output
        if args.project_part is not None:
            self.project_part = args.project_part

        if not args.interactive:
            if args.repo_url is None:
                raise Exception("No repo_url, if not in interactive mode an repo_url is required")
            else:
                self.repo_url = args.repo_url

if __name__=="__main__":
    # Parse the arguments
    parser = get_parser()
    args = parser.parse_args()
    print("Let's have a project with : " + str(args.project_part))
    if args.interactive:
        print("Script launched in interactive mode")
    project_opt = Project(args=args)
    create_main_folder(project_opt=project_opt)

