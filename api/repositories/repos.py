from core.rest_client import RestClient
from api.repositories.branches import Branches
from api.repositories.collaborators import Collaborators
from api.repositories.comments import Comments
from api.repositories.traffic import Traffic


class Repos(RestClient):
    def __init__(self, api_host, **kwargs):
        super(Repos, self).__init__(api_host, **kwargs)
        self.branches = Branches(self.api_host, **kwargs)
        self.collaborators = Collaborators(self.api_host, **kwargs)
        self.comments = Comments(self.api_host, **kwargs)
        self.traffic = Traffic(self.api_host, **kwargs)

    # 1
    def list_your_repos(self, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-your-repositories
        """
        return self.get('/user/repos', **kwargs)

    # 2
    def list_user_repos(self, username, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-user-repositories
        :param username: username
        """
        return self.get('/users/{}/repos'.format(username), **kwargs)

    # 3
    def list_org_repos(self, org, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-organization-repositories
        :param org: orgname
        """
        return self.get('/orgs/{}/repos'.format(org), **kwargs)

    # 4
    def list_all_public_repos(self, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-all-public-repositories
        """
        return self.get('/repositories', **kwargs)

    # 5
    def create_user_repo(self, **kwargs):
        """
        https://developer.github.com/v3/repos/#create
        """
        return self.post('/user/repos', **kwargs)

    # 6
    def create_org_repo(self, org, **kwargs):
        """
        https://developer.github.com/v3/repos/#create
        """
        return self.post('/orgs/{}/repos'.format(org), **kwargs)

    # 7
    def edit_repo(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/#edit
        :param owner: owner
        :param repo: repo
        """
        return self.patch('/repos/{}/{}'.format(owner, repo), **kwargs)

    # 127
    def list_all_topics_for_a_repository(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-all-topics-for-a-repository
        :param owner: owner
        :param repo: repo
        """
        return self.get('/repos/{}/{}/topics'.format(owner, repo), **kwargs)

    # 128
    def replace_all_topics_for_a_repository(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/#replace-all-topics-for-a-repository
        :param owner: owner
        :param repo: repo
        """
        return self.put('/repos/{}/{}/topics'.format(owner, repo), **kwargs)

    # 129
    def list_contributors(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-contributors
        :param owner: owner
        :param repo: repo
        """
        return self.get('/repos/{}/{}/contributors'.format(owner, repo), **kwargs)

    # 130
    def list_languages(self, owner, repo):
        """
        https://developer.github.com/v3/repos/#list-languages
        :param owner: owner
        :param repo: repo
        """
        return self.get('/repos/{}/{}/languages'.format(owner, repo))

    # 131
    def list_teams(self, owner, repo):
        """
        https://developer.github.com/v3/repos/#list-teams
        :param owner: owner
        :param repo: repo
        """
        return self.get('/repos/{}/{}/teams'.format(owner, repo))

    # 132
    def list_tags(self, owner, repo):
        """
        https://developer.github.com/v3/repos/#list-tags
        :param owner: owner
        :param repo: repo
        """
        return self.get('/repos/{}/{}/tags'.format(owner, repo))

    #  133
    def delete_a_repository(self, owner, repo):
        """
        https://developer.github.com/v3/repos/#delete-a-repository
        :param owner:
        :param repo:
        """
        return self.delete('/repos/{}/{}'.format(owner, repo))

    #   134
    def transfer_a_repository(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/#transfer-a-repository
        :param owner: owner
        :param repo: repo
        """
        return self.post('/repos/{}/{}/transfer'.format(owner, repo), **kwargs)

# if __name__ == '__main__':
#     host = 'https://api.github.com'
#     re = Repos(host, username='chn0622', password='chn432431')
#     params = {'direction': 'desc', 'sort': 'created'}
#     r = re.list_your_repos(params=params)
#     print(r.status_code)
#     print(r.text)