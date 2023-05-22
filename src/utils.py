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

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
DEFAULT_LAYOUT_PATH = FILE_PATH + "/../data/default_layout.json"

class Project():
    ''' Class to propagate informations between scripts '''
    is_interactive:bool=False
    output_dir:str=None
    parts:list=None
    repo_url:str=None
    path:str=None
    layout:dict=None
    optionnal_folders:list=None

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
        with open(path, "r", encoding="utf-8") as layout_file:
            self.layout = json.load(layout_file)

    def get_optionnal_folders(self):
        ''' Parse the layout dictionnary to get first layer folders '''
        for item, content in self.layout.items():
            if isinstance(content, dict):
                # Dict represent folders
                self.optionnal_folders.append(item)

def create_folder_objects(folder:dict, create_folder:bool=True):
    ''' Takes a dict discribing a folder and creates the contained objects '''
    for item, content in folder.items():
        if isinstance(content, dict) and create_folder:
            # Dict represent folders
            os.makedirs(item)
        elif isinstance(content, str):
            # Str represent files
            with open(item, "w", encoding="utf-8") as new_f:
                new_f.write(content)