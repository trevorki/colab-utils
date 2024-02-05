# colab-utils
A few simple functions to simplify the Google Colab / Google Drive / Github workflow.

## Setup
- Create a Github token with repo access
- Create a file called `env.json` that contains all your secrets, that looks like this:
```json
{
    "GITHUB_TOKEN":"<your_github_token>",
    "GITHUB_USERNAME":"<your_github_username>",
    "GITHUB_EMAIL":"<your_github_email>",
}
```

## Instructions

```python
import colab_utils
import os
```

Load github auth info, secrets, etc from `env.json` file to environment variables:

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