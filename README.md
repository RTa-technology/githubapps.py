# githubapps.py
[![GitHub license](https://img.shields.io/github/license/RTa-technology/githubapps.py)](https://github.com/RTa-technology/githubapps.py/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/RTa-technology/githubapps.py)](https://github.com/RTa-technology/githubapps.py/issues)
[![GitHub forks](https://img.shields.io/github/forks/RTa-technology/githubapps.py)](https://github.com/RTa-technology/githubapps.py/network)
[![GitHub stars](https://img.shields.io/github/stars/RTa-technology/githubapps.py)](https://github.com/RTa-technology/githubapps.py/stargazers)
[![PyPI version](https://badge.fury.io/py/githubapps.py.svg)](https://badge.fury.io/py/githubapps.py)
[![Python Versions](https://img.shields.io/pypi/pyversions/githubapps.py.svg)](https://pypi.org/project/githubapps.py/)
[![Downloads](https://pepy.tech/badge/githubapps-py)](https://pepy.tech/project/githubapps-py?period=total)

A Python wrapper for the Github Apps API
  
# installing  
Install and update using pip:

`pip install githubapps.py`  

# examples
A simple example.  

## Sync
```python
import githubapps
def main():
    with open('env/private.key', 'rb') as f_private:
        private_key = f_private.read()
    with open('env/app_id.key', 'r') as f_app_id:
        app_id = f_app_id.read()
    with open('env/installation_id.key', 'r') as f_installation_id:
        installation_id = f_installation_id.read()
    client_secret = private_key
    auth = githubapps.RequestsAuth(app_id, installation_id, client_secret)
    access_token = auth.get_access_token()
    print(access_token)

if __name__ == "__main__":
    main()
```
## Async
```python
import githubapps
import asyncio

async def main():
    with open('env/private.key', 'rb') as f_private:
        private_key = f_private.read()
    with open('env/app_id.key', 'r') as f_app_id:
        app_id = f_app_id.read()
    with open('env/installation_id.key', 'r') as f_installation_id:
        installation_id = f_installation_id.read()
    client_secret = private_key
    auth = githubapps.AiohttpAuth(app_id, installation_id, client_secret)
    access_token = await auth.get_access_token()
    print(access_token)

if __name__ == "__main__":
    asyncio.run(main())
```
