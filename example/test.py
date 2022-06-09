
import githubapps
from github import Github

# using an access token


def main():
    with open('env/private.key', 'rb') as f_private:
        private_key = f_private.read()
    with open('env/app_id.key', 'r') as f_app_id:
        app_id = f_app_id.read()
    with open('env/installation_id.key', 'r') as f_installation_id:
        installation_id = f_installation_id.read()
    client_secret = private_key
    auth = githubapps.Auth(app_id, installation_id, client_secret)
    access_token = auth.get_access_token()

    g = Github(access_token)

    repo = g.get_repo("RTa-scp/reserveiframe")
    repocontent = []
    contents = repo.get_contents("src/reserve", ref="reserve")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            repocontent.append(file_content.path)
    file = "src/reserve/component/theme.md"
    if file in repocontent:
        contents = repo.get_contents(file, ref="reserve")
        repo.update_file(contents.path, "update: GithubApps",
                         '---\nurl: content\nuser: user\nstarttime: "2022-04-10"\nendtime: "2022-07-10"\n---\n<reserve />', contents.sha, branch="reserve")
    else:
        repo.create_file(file, "create: GithubApps",
                         '---\nurl: content\nuser: user\nstarttime: "2022-04-11"\nendtime: "2022-07-11"\n---\n<reserve />', branch="reserve")

if __name__ == "__main__":
    main()
