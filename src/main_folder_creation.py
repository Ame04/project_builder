#!/usr/bin/python3

import os
import subprocess
import utils

def create_main_folder(project:utils.Project):
    ''' Create the main folder and fill it '''
    if project.is_interactive:
        tmp = input("Enter the path where you want to create your project : ")
        if tmp != "":
            project.output_dir = tmp

    # Verify the path and create it if it does not exist
    path_existed = os.path.exists(project.output_dir)
    if not path_existed:
        utils.print_ongoing_task("The path doesn't exist, creating it")
        os.makedirs(project.output_dir)
        utils.print_task_done()
        utils.print_info("Path created : " + os.getcwd() + "/" + project.output_dir)
    else:
        existing_folders = os.listdir(project.output_dir)

    if project.is_interactive:
        project.repo_url = input("Enter you repo URL : ")


    ########### Repository clonning ###########
    cmd_line = "git clone " + project.repo_url

    utils.print_ongoing_task("Entering the folder and cloning the blank repository")
    os.chdir(project.output_dir)
    try:
        subprocess.run(cmd_line, shell=True, check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        utils.print_error("Cloning exited with return code : " + str(e.returncode))
        utils.print_error(e.stderr)
        exit(1)

    utils.print_task_done()
    if not path_existed:
        project_name = os.listdir(os.getcwd())[0]
    else:
        new_folder_ls = os.listdir(os.getcwd())
        project_name = [folder for folder in new_folder_ls if folder not in existing_folders][0]

    project.path = os.path.join(os.getcwd(), project_name, "")

    ########### Main folder objects creation ###########
    utils.print_ongoing_task("Creating main folder objects")
    utils.create_folder_objects(project.layout, project.path, create_folder=False)
    utils.print_task_done()