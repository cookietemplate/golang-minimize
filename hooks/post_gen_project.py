"""
Does the following:

1. Inits git if used
2. Deletes dockerfiles if not going to be used
3. Deletes config utils if not needed
"""
from __future__ import print_function
import os
import shutil
from subprocess import Popen

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filename):
    """
    generic remove file from project dir
    """
    fullpath = os.path.join(PROJECT_DIRECTORY, filename)
    if os.path.exists(fullpath):
        os.remove(fullpath)

def init_git():
    """
    Initialises git on the new project folder
    """
    GIT_COMMANDS = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-a", "-m", "Initial Commit."]
    ]

    for command in GIT_COMMANDS:
        git = Popen(command, cwd=PROJECT_DIRECTORY)
        git.wait()


# def remove_docker_files():
#     """
#     Removes files needed for docker if it isn't going to be used
#     """
#     for filename in ["Dockerfile",]:
#         os.remove(os.path.join(
#             PROJECT_DIRECTORY, filename
#         ))

def remove_viper_files():
    """
    Removes files needed for viper config utils
    """
    shutil.rmtree(os.path.join(
        PROJECT_DIRECTORY, "config"
    ))

def remove_log_files():
    """
    Removes files needed for viper config utils
    """
    shutil.rmtree(os.path.join(
        PROJECT_DIRECTORY, "log"
    ))

def remove_cobra_files():
    """
    Removes files needed for viper config utils
    """
    shutil.rmtree(os.path.join(
        PROJECT_DIRECTORY, "cmd"
    ))

# def remove_circleci_files():
#     """
#     Removes files needed for viper config utils
#     """
#     shutil.rmtree(os.path.join(
#         PROJECT_DIRECTORY, ".circleci"
#     ))

def remove_api_files():
    """
    Removes files needed for viper config utils
    """
    shutil.rmtree(os.path.join(
        PROJECT_DIRECTORY, "api"
    ))

def remove_web_files():
    """
    Removes files needed for viper config utils
    """
    shutil.rmtree(os.path.join(
        PROJECT_DIRECTORY, "web"
    ))

def remove_extra_files():
    """
    Removes files needed for viper config utils
    """
    shutil.rmtree(os.path.join(
        PROJECT_DIRECTORY, "assets"
    ))
    shutil.rmtree(os.path.join(
        PROJECT_DIRECTORY, "docs"
    ))
    shutil.rmtree(os.path.join(
        PROJECT_DIRECTORY, "examples"
    ))
    shutil.rmtree(os.path.join(
        PROJECT_DIRECTORY, "githooks"
    ))
    shutil.rmtree(os.path.join(
        PROJECT_DIRECTORY, "third_party"
    ))
    shutil.rmtree(os.path.join(
        PROJECT_DIRECTORY, "tools"
    ))
    shutil.rmtree(os.path.join(
        PROJECT_DIRECTORY, "website"
    ))

# # 1. Remove Dockerfiles if docker is not going to be used
# if '{{ cookiecutter.use_docker }}'.lower() != 'y':
#     remove_docker_files()

# 2. Remove viper config if not seleted
if '{{ cookiecutter.use_viper_config }}'.lower() != 'y':
    remove_viper_files()

# 3. Remove logrus utils if not seleted
if '{{ cookiecutter.logger_type }}'.lower() != 'logrus':
    remove_log_files()

# 4. Remove cobra utils if not seleted
if '{{ cookiecutter.use_cobra_cmd }}'.lower() != 'y':
    remove_cobra_files()

# # 5. Remove unused ci choice
# if ' cookiecutter.use_ci'.lower() == 'travis':
#     remove_circleci_files()
# elif ' cookiecutter.use_ci'.lower() == 'circle':
#     remove_file(".travis.yml")
# else:
#     remove_file(".travis.yml")
#     remove_circleci_files()

# 6. Initialize Git (should be run after all file have been modified or deleted)
if '{{ cookiecutter.use_git }}'.lower() == 'y':
    init_git()
else:
    remove_file(".gitignore")

# 7. Remove unused extra files
if '{{ cookiecutter.extra_folders }}'.lower() != 'y':
    remove_extra_files()

# 8. Remove unused api files
if '{{ cookiecutter.project_type }}'.lower()!= 'api':
    remove_web_files()
elif '{{ cookiecutter.project_type }}'.lower()!= 'cli':
    remove_api_files()
    remove_web_files()
