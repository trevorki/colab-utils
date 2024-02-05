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

Mounting your google drive to notebook file system:

```python
mount_google_drive()
```

Load secrets, etc from `env.json` file:

```python
env = load_env(path="/content/gdrive/My Drive/repos/env.json")
gh_token = env["GITHUB_TOKEN"]
```


Clone a repo:

```python
clone_repo(gh_username, gh_repo_name, gh_token)
```