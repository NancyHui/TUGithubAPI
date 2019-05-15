from core.rest_client import RestClient


class Statuses(RestClient):
    # 241
    def create_a_status(self, owner, repo, sha, **kwargs):
        """
        https://developer.github.com/v3/repos/statuses/#create-a-status
        """
        return self.post("/repos/{}/{}/statuses/{}".format(owner, repo, sha), **kwargs)

    # 242
    def list_statuses_for_a_specific_ref(self, owner, repo, ref, **kwargs):
        """
        https://developer.github.com/v3/repos/statuses/#list-statuses-for-a-specific-ref
        """
        return self.get("/repos/{}/{}/commits/{}/statuses".format(owner, repo, ref), **kwargs)

    # 243
    def get_the_combined_status_for_a_specific_ref(self, owner, repo, ref, **kwargs):
        """
        https://developer.github.com/v3/repos/statuses/#get-the-combined-status-for-a-specific-ref
        """
        return self.get("/repos/{}/{}/commits/{}/status".format(owner, repo, ref), **kwargs)