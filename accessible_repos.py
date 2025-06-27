import requests


def get_user_accessible_repos(username: str, opa_inputs: list):
    accessible_repos = []

    for item in opa_inputs:
        if item["user"] != username:
            continue

        response = requests.post(
            "http://localhost:8181/v1/data/github/authz/allow",
            json={"input": item}
        )

        if response.status_code != 200:
            print(f"[!] OPA error for {item['repository']}: {response.text}")
            continue

        result = response.json().get("result", False)

        if result:
            accessible_repos.append(item["repository"])

    return accessible_repos