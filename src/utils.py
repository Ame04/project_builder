#!/usr/bin/python3

import os
import json

# ANSI escape codes for text colors
color_reset = "\033[0m"
color_red = "\033[31m"
color_green = "\033[32m"
color_yellow = "\033[33m"
color_blue = "\033[34m"
color_magenta = "\033[35m"
color_cyan = "\033[36m"

FILE_PATH = os.path.abspath(__file__)
DEFAULT_LAYOUT_PATH = FILE_PATH + "../data/default_layout.json"

class Project():
    ''' Class to propagate informations between scripts '''
    is_interactive:bool=False
    output_dir:str=None
    parts:list=None
    repo_url:str=None
    path:str=None
    layout:dict=None

    def __init__(self, args):
        ''' Initialyse the class with info from the arg parser '''
        self.is_interactive = args.interactive
        self.output_dir = args.output
        if args.project_part is not None:
            self.parts = args.project_part

        if not args.interactive:
            if args.repo_url is None:
                raise Exception("No repo_url, if not in interactive mode a repo_url is required")
            else:
                self.repo_url = args.repo_url

            if args.layout_path is not None:
                self.parse_layout(args.layout_path)
            else:
                self.parse_layout(DEFAULT_LAYOUT_PATH)

        else:
            layout_path = input("enter the path to your project layout file"
                                " (if empty default will be taken): ")
            if layout_path == "":
                self.parse_layout(DEFAULT_LAYOUT_PATH)
            else:
                self.parse_layout(layout_path)



    def parse_layout(self, path):
        ''' Import the layout from a given path '''
        self.layout = json.loads(path)