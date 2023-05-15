#!/usr/bin/python3

import os
import subprocess
import utils

def create_main_folder(project_opt):
    ''' Create the main folder and fill it '''
    if project_opt.interactive:
        project_opt.output = input("Enter the path where you want to create your project : ")

    # Verify the path and create it if it does not exist
    if not os.path.exists(project_opt.output):
        print("The path doesn't exist, creating it ...")
        os.makedirs(project_opt.output)
        print("Path created : " + os.getcwd() + "/" + project_opt.output)

    if project_opt.interactive:
        project_opt.repo_url = input("Enter you repo URL : ")

    cmd_line = "git clone " + project_opt.repo_url

    print("Entering the folder and cloning the blank repository ...")
    os.chdir(project_opt.output)
    # Clone the repository
    try:
        subprocess.run(cmd_line, shell=True, check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(utils.color_red + "Cloning exited with return code : " +
              str(e.returncode) + utils.color_reset)
        print(e.stderr)
        exit(1)

    print("Cloning the blank repository : done")
