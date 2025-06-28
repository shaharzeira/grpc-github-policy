from .config import HEADERS
import requests


def build_opa_repo_access_inputs(org_name: str):
    """
    Fetches collaborator permissions for each repository in the org.
    Returns a list of (repo_name, {user: permissions_dict}) tuples.
    """
    opa_repo_access_inputs  = []

    repos_url = f"https://api.github.com/orgs/{org_name}/repos"
    repos = requests.get(repos_url, headers=HEADERS).json()

    for repo in repos:
        repo_name = repo["name"]
        collaborators_url = f"https://api.github.com/repos/{org_name}/{repo_name}/collaborators"
        response = requests.get(collaborators_url, headers=HEADERS)

        if response.status_code != 200:
            print(f"[!] Error fetching collaborators for {repo_name}: {response.status_code}")
            continue

        collaborators = response.json()

        if not isinstance(collaborators, list):
            continue

        user_permissions = {
            user["login"]: user.get("permissions", {}) for user in collaborators
        }

        for user, perms in user_permissions.items():
            opa_repo_access_inputs.append({
                "repository": repo_name,
                "user": user,
                "permissions": perms
            })

    return opa_repo_access_inputs
