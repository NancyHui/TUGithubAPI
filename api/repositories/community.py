from core.rest_client import RestClient


class Community(RestClient):
    # 257
    def retrieve_community_profile(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/community/#retrieve-community-profile-metrics
        """
        return self.get("/repos/{}/{}/community/profile".format(owner, repo), **kwargs)