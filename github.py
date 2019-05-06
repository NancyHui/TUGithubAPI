from api.repositories.repos import Repos
# from api.repositories.branches import Branches


class Github(object):
    def __init__(self, **kwargs):
        self.api_host = 'https://api.github.com'
        self.repos = Repos(self.api_host, **kwargs)
        # self.branches = Branches(self.api_host, **kwargs)


if __name__ == '__main__':
    username = 'NancyHui'
    orgname = 'TestUpCommunity'

    token = '5a82ed2aee953483ee627ee651af3b8df60ab62e'
    github = Github(token=token)

    # All data is sent and received as JSON

    # # 1
    # params1 = {'direction': 'desc'}
    # r1 = github.repos.list_your_repos(params=params1)
    # # assert r1.status_code == 200
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
    # r135 = github.repos.branches.list_branches(username, 'TUGithubAPI', params=params135)
    # print(r135.status_code)
    # print(r135.text)

    # # 136
    # r136 = github.repos.branches.get_branch(username, 'TUGithubAPI', 'feature_local')
    # print(r136.status_code)
    # print(r136.text)

    # # 137
    # headers = {'Accept': 'application/vnd.github.luke-cage-preview+json'}
    # r137 = github.repos.branches.get_branch(username, 'hello-world', 'readme-edits', headers=headers)
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
    # r138 = github.repos.branches.update_branch_protection(username, 'hello-world', 'branch_test', json=params138,
    #                                                         headers=headers)
    # print(r138.status_code)
    # print(r138.text)

    # # 139
    # r139 = github.repos.branches.remove_branch_protection(username, 'hello-world', 'branch_test')
    # print(r139.status_code)
    # print(r139.text)

    # # 140
    # r140 = github.repos.branches.get_required_status_checks_of_protected_branch(username, 'hello-world', 'branch_test')
    # print(r140.status_code)
    # print(r140.text)

    # # 141
    # params141 = {
    #   "strict": True,
    #   "contexts": [
    #     "update"
    #   ]
    # }
    # r141 = github.repos.branches.update_required_status_checks_of_protected_branch(username, repo='hello-world', branch='branch_test', json=params141)
    # print(r141.status_code)

    # # 142
    # r142 = github.repos.branches.remove_required_status_checks_of_protected_branch(username, 'hello-world', 'branch_test')
    # print(r142.status_code)
    # print(r142.text)

    # # 143
    # r143 = github.repos.branches.list_required_status_checks_contexts_of_protected_branch(username, 'hello-world', 'branch_test')
    # print(r143.status_code)
    # print(r143.text)

    # # 144
    # params144 = ["replaced"]
    # r144 = github.repos.branches.replace_required_status_checks_contexts_of_protected_branch(username, 'hello-world', 'branch_test', json=params144)
    # print(r144.status_code)
    # print(r144.text)

    # # 145
    # params145 = ["Adding_two"]
    # r145 = github.repos.branches.add_required_status_checks_contexts_of_protected_branch(username, 'hello-world', 'branch_test', json=params145)
    # print(r145.status_code)
    # print(r145.text)

    # # 146
    # params146 = ["Adding_two"]
    # r146 = github.repos.branches.remove_required_status_checks_contexts_of_protected_branch(username, 'hello-world', 'branch_test', json=params146)
    # print(r146.status_code)
    # print(r146.text)

    # # 147
    # headers = {"Accept": "application/vnd.github.luke-cage-preview+json"}
    # r147 = github.repos.branches.get_pull_request_review_enforcement_of_protected_branch(username, 'hello-world', 'branch_test', headers=headers)
    # print(r147.status_code)
    # print(r147.text)

    # # 148
    # headers = {"Accept": "application/vnd.github.luke-cage-preview+json"}
    # # 参数dismissal_restrictions，与team有关
    # params148 = {
    #   "dismiss_stale_reviews": True,
    #   "require_code_owner_reviews": True,
    #   "required_approving_review_count": 2
    # }
    # r148 = github.repos.branches.update_pull_request_review_enforcement_of_protected_branch(username, 'hello-world', 'branch_test', json=params148, headers=headers)
    # print(r148.status_code)
    # print(r148.text)

    # # 149
    # r149 = github.repos.branches.remove_pull_request_review_enforcement_of_protected_branch(username, 'hello-world', 'branch_test')
    # print(r149.status_code)
    # print(r149.text)

    # # 150
    # headers = {"Accept": "application/vnd.github.zzzax-preview+json"}
    # r150 = github.repos.branches.get_required_signatures_of_protected_branch(username, 'hello-world', 'branch_test', headers=headers)
    # print(r150.status_code)
    # print(r150.text)

    # # 151
    # headers = {"Accept": "application/vnd.github.zzzax-preview+json"}
    # r151 = github.repos.branches.add_required_signatures_of_protected_branch(username, 'hello-world', 'branch_test', headers=headers)
    # print(r151.status_code)
    # print(r151.text)

    # # 152
    # headers = {"Accept": "application/vnd.github.zzzax-preview+json"}
    # r152 = github.repos.branches.add_required_signatures_of_protected_branch(username, 'hello-world', 'branch_test',
    #                                                                    headers=headers)
    # print(r152.status_code)
    # print(r152.text)

    # # 153
    # r153 = github.repos.branches.get_admin_enforcement_of_protected_branch(username, 'hello-world', 'branch_test')
    # print(r153.status_code)
    # print(r153.text)

    # # 154
    # r154 = github.repos.branches.add_admin_enforcement_of_protected_branch(username, 'hello-world', 'branch_test')
    # print(r154.status_code)
    # print(r154.text)

    # # 155
    # r155 = github.repos.branches.remove_admin_enforcement_of_protected_branch(username, 'hello-world', 'branch_test')
    # print(r155.status_code)
    # print(r155.text)

    # # 156
    # r156 = github.repos.branches.get_restrictions_of_protected_branch(username, 'hello-world', 'branch_test')
    # print(r156.status_code)
    # print(r156.text)

    # # 157
    # r157 = github.repos.branches.remove_restrictions_of_protected_branch(username, 'hello-world', 'branch_test')
    # print(r157.status_code)
    # print(r157.text)

    # # 158
    # headers = {"Accept": "application/vnd.github.hellcat-preview+json"}
    # r158 = github.repos.branches.list_team_restrictions_of_protected_branch(username, 'hello-world', 'branch_test',
    #                                                                   headers=headers)
    # print(r158.status_code)
    # print(r158.text)

    # # 159
    # headers = {"Accept": "application/vnd.github.hellcat-preview+json"}
    # params159 = ["replace"]
    # r159 = github.repos.branches.replace_team_restrictions_of_protected_branch(username, 'hello-world', 'branch_protected',
    #                                                                      json=params159, headers=headers)
    # print(r159.status_code)
    # print(r159.text)

    # # 160
    # headers = {"Accept": "application/vnd.github.hellcat-preview+json"}
    # params160 = ["Adding"]
    # r160 = github.repos.branches.add_team_restrictions_of_protected_branch(username, 'hello-world', 'branch_protected',
    #                                                                   json=params160, headers=headers)
    # print(r160.status_code)
    # print(r160.text)

    # # 161
    # headers = {"Accept": "application/vnd.github.hellcat-preview+json"}
    # params161 = ["remove"]
    # r161 = github.repos.branches.remove_team_restrictions_of_protected_branch(username, 'hello-world', 'branch_protected',
    #                                                                     json=params161, headers=headers)
    # print(r161.status_code)
    # print(r161.text)

    # # 162
    # r162 = github.repos.branches.list_user_restrictions_of_protected_branch(username, 'hello-world', 'branch_protected')
    # print(r162.status_code)
    # print(r162.text)

    # # 163
    # params163 = ["replace"]
    # r163 = github.repos.branches.replace_team_restrictions_of_protected_branch(username, 'hello-world', 'branch_protected',
    #                                                                      json=params163)
    # print(r163.status_code)
    # print(r163.text)

    # # 164
    # params164 = ["Adding"]
    # r164 = github.repos.branches.add_team_restrictions_of_protected_branch(username, 'hello-world', 'branch_protected',
    #                                                                  json=params164)
    # print(r164.status_code)
    # print(r164.text)

    # 165
    # params165 = ["remove"]
    # r165 = github.repos.branches.remove_user_restrictions_of_protected_branch(username, 'hello-world', 'branch_protected',
    #                                                                     json=params165)
    # print(r165.status_code)
    # print(r165.text)

    # # 244
    # r244 = github.repos.traffic.list_referrers(username, 'hello-world')
    # print(r244.status_code)
    # print(r244.text)

    # # 245
    # r245 = github.repos.traffic.list_paths(username, 'hello-world')
    # print(r245.status_code)
    # print(r245.text)

    # # 246
    # params246 = {"per": "day"}
    # r246 = github.repos.traffic.views(username, 'requests', params=params246)
    # print(r246.status_code)
    # print(r246.text)

    # 247
    params247 = {"per": "week"}
    r247 = github.repos.traffic.clones(username, 'ZSXQ', params=params247)
    print(r247.status_code)
    print(r247.text)
