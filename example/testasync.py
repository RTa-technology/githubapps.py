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