from core.rest_client import RestClient


class Forks(RestClient):
    # 206
    def list_forks(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/forks/#list-forks
        """
        return self.get("/repos/{}/{}/forks".format(owner, repo), **kwargs)

    #  207
    def create_a_fork(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/forks/#create-a-fork
        """
        return self.post("/repos/{}/{}/forks".format(owner, repo), **kwargs)