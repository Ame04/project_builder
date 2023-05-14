#!/usr/bin/python3

import os
import subprocess

def create_main_folder(project_opt):
    ''' Create the main folder and fill it '''
    if project_opt.interactive:
        project_opt.output = input("Enter the path where you want to creat your project : ")

    # Verify the path and create it if it does not exist
    if not os.path.exists(project_opt.output):
        print("The path doesn't exist, creating it ...")
        os.makedirs(project_opt.output)
        print("Path created : " + os.getcwd() + "/" + project_opt.output)

    if project_opt.interactive:
        project_opt.repo_url = input("Enter you repo URL : ")

    cmd_line = "git clone " + project_opt.repo_url

    print("Cloning the blank repository ...")
    # Check if the path exists
    os.chdir(project_opt.output)
    print("The current working directory is there : " + os.getcwd())
    # Clone the repository
    subprocess.run(cmd_line, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Cloning the blank repository : done")





