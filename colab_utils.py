from google.colab import drive
import json
import os

def mount_google_drive(path='/content/gdrive'):
    """Mounts google drive to notebook's filesystem

    Args:
        path (str, optional): Where to mount google drive in notebook filesystem. Defaults to '/content/gdrive'.
    """
    drive.mount(path)
    print(f"Mounted goolge drive at: {path}")
    print(f"Files can be found at  : {path}/My Drive")
    return


def load_env(path="/content/gdrive/My Drive/repos/env.json"):
    """Loads saved secrets in .json file as a dictionary. 
    This is a cheap and portableapproximation of using environment variables.

    Args:
        path (str, optional): path to file with secrets. Defaults to "/content/gdrive/My Drive/repos".

    Returns:
        dict: info saved in file
    """
    with open(path) as f:
        env = json.load(f)
    return env


def clone_repo(gh_username, gh_repo_name, gh_token):
    """Clones github repo
    """
    git_str = f"https://{gh_token}@github.com/{gh_username}/{gh_repo_name}.git"
    os.system(f"git clone {git_str}")  
    return
