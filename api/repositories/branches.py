from core.rest_client import RestClient

class Branches(RestClient):
    def __init__(self, api_host, **kwargs):
        super(Branches, self).__init__(api_host, **kwargs)

    # 135
    def list_branches(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#list-branches
        :param owner: owner
        :param repo: repo
        """
        return self.get('/repos/{}/{}/branches'.format(owner, repo), **kwargs)

    # 136
    def get_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#get-branch
        :param owner: owner
        :param repo: repo
        :param branch: branch
        """
        return self.get('/repos/{}/{}/branches/{}'.format(owner, repo, branch), **kwargs)

    # 137
    def get_branch_protection(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#get-branch-protection
        :param owner: owner
        :param repo: repo
        :param branch: branch
        """
        return self.get('/repos/{}/{}/branches/{}/protection'.format(owner, repo, branch), **kwargs)

    # 138
    def update_branch_protection(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#update-branch-protection
        :param owner: owner
        :param repo: repo
        :param branch: branch
        """
        return self.put('/repos/{}/{}/branches/{}/protection'.format(owner, repo, branch), **kwargs)

    # 139
    def remove_branch_protection(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#remove-branch-protection
        :param owner: owner
        :param repo: repo
        :param branch: branch
        """
        return self.delete('/repos/{}/{}/branches/{}/protection'.format(owner, repo, branch), **kwargs)

    # 140
    def get_required_status_checks_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#get-required-status-checks-of-protected-branch
        :param owner: owner
        :param repo: repo
        :param branch: branch
        """
        return self.get('/repos/{}/{}/branches/{}/protection/required_status_checks'.format(owner, repo, branch), **kwargs)