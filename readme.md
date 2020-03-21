GitHub analysis by using GitHub API.

First of all you need to install requirements (you need only one package - requests).

Secondly, you my want to create your own config instance (config.py). You can copy this from app and place it in folder "instance" on project level. Then you can modify it. You should do this, because GitHub will block all your requests (with 403 Error) if it haven't user's login and password.

Then, you can run app with the next command:
python -m app
