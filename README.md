# colab-utils
Google Colab is a nessecary evil sometimes when you need to train large models. But the interface is the absolute worst... little control over where notebooks are stored, difficulty with version control. It practically encourages you to create massive and disorganized notebooks.

This repo is meant to provide few simple functions that simplify the Google Colab / Google Drive / Github workflow.
- Create a repo and work locally until you need a colab notebook for training
- 


## Setup
- Create a `repos` folder in your google drive
- Create a Github token with repo access
- Create a file `repos/env.json` that contains all your secrets, that looks like this:
```json
{
    "GH_TOKEN":"<github_token>",
    "GH_USERNAME":"<github_username>",
    "GH_NAME":"<firtname lastname>",
    "GH_EMAIL":"<github_email>",
}
```
## Installation
1. Go to [Google Colab](https://colab.research.google.com/) and in the **Open notebook** window, select **GitHub** on the left, then locate this repo and open `install-update-colab_utils.ipynb`

![open from github](img/colab-open-window.png)
2. Step through the *clone repo* steps suntil you see the repo is cloned into a folder on your google drive.


## Usage

```python
import colab_utils
import os
```

Load github auth info, secrets, etc from `env.json` in your google drive to environment variables:

```python
colab_utils.load_env_vars("path/to/env.json")
```

Set git config parameters from environment variables
```
colab_utils.git_set_config()
```


Clone a repo:

```python
# navigate to folder where you keep repos
os.chdir("path/to/repos")

# clone repo
colab_utils.git_clone_repo("user_name/repo_name")

# navigate into repo folder
os.chdir("repo_name")
```

Copy current notebook to google drive folder
```python
copy_nb_to_drive("content/<current_notebook_filename>", "path/to/repos/repo_name")
```

# Starting a new notebook
Once the repo is cloned, you can import the colub_utils module and start using it in new notebooks by with the following code.

```python

```