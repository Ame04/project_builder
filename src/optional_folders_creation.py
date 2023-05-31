#!/usr/bin/python3

import os
import utils

def create_optional_folder(project:utils.Project):
    ''' Create the optional folders and fill them '''

    for folder in project.optionnal_folders:
        if project.is_interactive:
            keep = input("Do you want to have the " + str(folder) + " folder ? ")
        else:
            keep = True if folder in project.parts else False

        if keep:
            folder_place = os.path.join(project.path, folder)
            utils.print_ongoing_task("Creating the folder : " + str(folder))
            os.makedirs(folder_place)
            utils.print_task_done()

            utils.print_ongoing_task("Creating folder content")
            utils.create_folder_objects(project.layout[folder], folder_place, create_folder=True)
            utils.print_task_done()