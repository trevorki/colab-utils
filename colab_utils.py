import json
import os


def load_env_vars(path="/content/gdrive/My Drive/repos/env.json"):
    """Loads saved secrets in .json file to environment variables.

    Args:
        path (str, optional): path to file with secrets. Defaults to "/content/gdrive/My Drive/repos".

    """
    with open(path) as f:
        env = json.load(f)
    for key,value in env.items():
        os.environ[key]=value
    return 


def git_set_config():
    """Sets git config to allow pushing/pulling
    NOTE: uses `GH_NAME`, `GH_EMAIL` environment variable
    """
    os.system(f'git config --global user.name  "{os.environ["GH_NAME"]}"')  
    os.system(f'git config --global user.email "{os.environ["GH_EMAIL"]}"')  
    return


def git_clone_repo(gh_repo_name):
    """Clones github repo (NOTE: uses `GH_TOKEN` environment variable)
    Args:
        gh_repo_name (str): repo to clone in "user/repo" format
    """
    git_str = f"https://{os.environ['GH_TOKEN']}@github.com/{gh_repo_name}.git"
    os.system(f"git clone {git_str}")  
    return

def copy_nb_to_drive(colab_nb_filename, project_folder):
    """Copies active notebook from `Colab Notebooks` to project folder

    Args:
        colab_filename (str): name of current notebook (from top of page)
        project_folder (str): path to destination folder
    """
    os.system(f'cp {colab_nb_filename} {project_folder}')
    return
