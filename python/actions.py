import requests
import json

def get_github_action_status(repo_owner, repo_name, action_name, run_id):
    # Create a GET request to the GitHub REST API
    # url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs/{action_name}"
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs"
    headers = {
        "Authorization": "Bearer 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",
        "Accept": "application/vnd.github.antiope-preview+json",
    }
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        data = json.loads(response.content)
        print(data)
    else:
        print("Failed to get GitHub Action status:", response.status_code)

# Replace YOUR_GITHUB_TOKEN with your personal access token for GitHub
# Replace RUN_ID with the ID of the GitHub Action run
get_github_action_status("ls404", "02_GH_Actions_Test", "test_and_deploy", "9")