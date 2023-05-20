#!/usr/bin/python3

import os
import subprocess
import utils

def create_main_folder(project:utils.Project):
    ''' Create the main folder and fill it '''
    if project.is_interactive:
        project.output_dir = input("Enter the path where you want to create your project : ")

    # Verify the path and create it if it does not exist
    if not os.path.exists(project.output_dir):
        print("The path doesn't exist, creating it ...")
        os.makedirs(project.output_dir)
        print("Path created : " + os.getcwd() + "/" + project.output_dir)

    if project.is_interactive:
        project.repo_url = input("Enter you repo URL : ")


    ########### Repository clonning ###########
    cmd_line = "git clone " + project.repo_url

    print("Entering the folder and cloning the blank repository ... ", end="")
    os.chdir(project.output_dir)
    try:
        subprocess.run(cmd_line, shell=True, check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(utils.color_red + "Cloning exited with return code : " +
              str(e.returncode) + utils.color_reset)
        print(e.stderr)
        exit(1)

    print(utils.color_cyan + "DONE" + utils.color_reset)
    current_dir = os.getcwd()
    project_name = os.listdir(current_dir)[0]

    project.path = os.path.join(current_dir, project_name, "")

    ########### Main folder objects creation ###########
    print("Entering the project and creating main folder objects ... ", end="")
    os.chdir(project.path)
    utils.create_folder_objects(project.layout)
    print(utils.color_cyan + "DONE" + utils.color_reset)