import json
import os


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
