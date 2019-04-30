from api.repositories.repos import Repos
from api.repositories.branches import Branches
import json


class Github(object):
    def __init__(self, **kwargs):
        self.api_host = 'https://api.github.com'
        self.repos = Repos(self.api_host, **kwargs)
        self.branches = Branches(self.api_host, **kwargs)


if __name__ == '__main__':
    username = 'NancyHui'
    orgname = 'TestUpCommunity'

    token = '06e0e489b4d061069c2189cd11dbcd9502f9e348'
    github = Github(token=token)

    # All data is sent and received as JSON

    # # 1
    # params1 = {'direction': 'desc'}
    # r1 = github.repos.list_your_repos(params=params1)
    # assert r1.status_code == 200
    # print(r1.status_code)
    # print(r1.text)
    # print(type(r1.text))
    # print(type(r1.json()))
    # print(type(json.loads(r1.text)))


    # # 2
    # params2 = {'direction': 'desc'}
    # r2 = github.repos.list_user_repos(username, params=params2)
    # assert r2.status_code == 200
    # print(r2.status_code)
    # print(r2.text)

    # # 3
    # params3 = {'sort': 'created'}
    # r3 = github.repos.list_org_repos(orgname, params=params3)
    # assert r3.status_code == 200
    # print(r3.status_code)
    # print(r3.text)

    # # 4
    # params4 = {'since': '364'}
    # r4 = github.repos.list_all_public_repos(params=params4)
    # assert r4.status_code == 200
    # print(r4.status_code)
    # print(r4.text)

    # # 5
    # params5 = {
    #       "name": "Created-From-API-4",
    #       "description": "This is your first repository",
    #       "homepage": "https://github.com",
    #       "private": False,
    #       "has_issues": True,
    #       "has_projects": True,
    #       "has_wiki": True
    #     }
    # r5 = github.repos.create_user_repo(json=params5)
    # assert r5.status_code == 201
    # print(r5.status_code)
    # print(r5.text)

    # # 6
    # params6 = {
    #       "name": "Created-From-API-4",
    #       "description": "This is your first repository",
    #       "homepage": "https://github.com",
    #       "private": False,
    #       "has_issues": True,
    #       "has_projects": True,
    #       "has_wiki": True
    # }
    # r6 = github.repos.create_org_repo(org=org, json=params6)
    # print(r6.status_code)
    # print(r6.text)

    # # 7
    # params7 = {
    #       "name": "Created-From-API-3",
    #       "description": "This is your first repository",
    #       "homepage": "https://github.com",
    #       "private": True,
    #       "has_issues": True,
    #       "has_projects": True,
    #       "has_wiki": True
    # }
    # r7 = github.repos.edit_repo(owner=username, repo='Created-From-API-2', json=params7)
    # print(r7.status_code)
    # print(r7.text)

    # # 127
    # headers = {'Accept': 'application/vnd.github.mercy-preview+json'}
    # r127 = github.repos.list_all_topics_for_a_repository(username, 'hello-world', headers=headers)
    # assert r127.status_code == 200
    # print(r127.status_code)
    # print(r127.text)

    # # 128
    # names = {"names": ["one"]}
    # headers = {'Accept': 'application/vnd.github.mercy-preview+json'}
    # r128 = github.repos.replace_all_topics_for_a_repository(username, 'hello-world', json=names, headers=headers)
    # print(r128.status_code)
    # print(r128.text)

    # # 129
    # params129 = {"anon": "true"}
    # r129 = github.repos.list_contributors(username, 'Created-From-API', params=params129)
    # print(r129.status_code)
    # print(r129.text)

    # # 130
    # r130 = github.repos.list_languages(username, 'hello-world')
    # print(r130.status_code)
    # print(r130.text)

    # # 131
    # r131 = github.repos.list_teams(username, 'TUGithubAPI')
    # print(r131.status_code)
    # print(r131.text)

    # # 132
    # r132 = github.repos.list_tags(username, 'hello-world')
    # print(r132.status_code)
    # print(r132.text)

    # # 133
    # r133 = github.repos.delete_a_repository('chn0622', 'Created-From-API-3')
    # print(r133.status_code)
    # print(r133.text)

    # # 134
    # param134 = {
    #   "new_owner": "chn0622",
    #   "team_ids": [
    #     12,
    #     345
    #   ]
    # }
    # headers = {"Accept": "application/vnd.github.nightshade-preview+json"}
    # r134 = github.repos.transfer_a_repository(username, 'Created-From-API-3', json=param134, headers=headers)
    # print(r134.status_code)
    # print(r134.text)

    # # 135
    # 作为get方法中的params，最终拼接在url后面形式为?protected=false，参数表中虽然规定参数类型为boolean，但传递参数是应为string
    # params135 = {"protected": "false"}
    # r135 = github.branches.list_branches(username, 'TUGithubAPI', params=params135)
    # print(r135.status_code)
    # print(r135.text)

    # # 136
    # r136 = github.branches.get_branch(username, 'TUGithubAPI', 'feature_local')
    # print(r136.status_code)
    # print(r136.text)

    # # 137
    # headers = {'Accept': 'application/vnd.github.luke-cage-preview+json'}
    # r137 = github.branches.get_branch(username, 'hello-world', 'readme-edits', headers=headers)
    # print(r137.status_code)
    # print(r137.text)

    # # 138
    # headers = {'Accept': 'application/vnd.github.luke-cage-preview+json'}
    # params138 = {
    #   "required_status_checks": {
    #     "strict": True,
    #     "contexts": [
    #       "continuous-integration/travis-ci"
    #     ]
    #   },
    #   "enforce_admins": True,
    #   "required_pull_request_reviews": {
    #     "dismissal_restrictions": {},
    #     "dismiss_stale_reviews": True,
    #     "require_code_owner_reviews": True,
    #     "required_approving_review_count": 2
    #   },
    #   "restrictions": None
    # }
    # r138 = github.branches.update_branch_protection(username, 'hello-world', 'branch_test', json=params138, headers=headers)
    # print(r138.status_code)
    # print(r138.text)

    # # 139
    # r139 = github.branches.remove_branch_protection(username, 'hello-world', 'branch_test')
    # print(r139.status_code)
    # print(r139.text)

    # 140
    r140 = github.branches.get_required_status_checks_of_protected_branch(username, 'hello-world', 'branch_test')
    print(r140.status_code)
    print(r140.text)