from core.rest_client import RestClient

class Traffic(RestClient):
    # 244
    def list_referrers(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/traffic/#list-referrers
        :param owner: owner
        :param repo: repo
        """
        return self.get("/repos/{}/{}/traffic/popular/referrers".format(owner, repo), **kwargs)

    # 245
    def list_paths(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/traffic/#list-paths
        :param owner: owner
        :param repo: repo
        """
        return self.get("/repos/{}/{}/traffic/popular/paths".format(owner, repo), **kwargs)

    # 246
    def views(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/traffic/#views
        :param owner: owner
        :param repo: repo
        """
        return self.get("/repos/{}/{}/traffic/views".format(owner, repo), **kwargs)

    # 247
    def clones(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/traffic/#clones
        :param owner: owner
        :param repo: repo
        """
        return self.get("/repos/{}/{}/traffic/clones".format(owner, repo), **kwargs)