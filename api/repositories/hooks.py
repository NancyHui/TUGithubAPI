from core.rest_client import RestClient


class Hooks(RestClient):
    # 248
    def list_hooks(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/hooks/#list-hooks
        """
        return self.get("/repos/{}/{}/hooks".format(owner, repo), **kwargs)

    # 249
    def get_single_hook(self, owner, repo, hook_id, **kwargs):
        """
        https://developer.github.com/v3/repos/hooks/#get-single-hook
        """
        return self.get("/repos/{}/{}/hooks/{}".format(owner, repo, hook_id), **kwargs)

    # 250
    def create_a_hook(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/hooks/#create-a-hook
        """
        return self.post("/repos/{}/{}/hooks".format(owner, repo), **kwargs)

    # 251
    def edit_a_hook(self, owner, repo, hook_id, **kwargs):
        """
        https://developer.github.com/v3/repos/hooks/#edit-a-hook
        """
        return self.patch("/repos/{}/{}/hooks/{}".format(owner, repo, hook_id), **kwargs)

    # 252
    def test_a_push_hook(self, owner, repo, hook_id, **kwargs):
        """
        https://developer.github.com/v3/repos/hooks/#test-a-push-hook
        """
        return self.post("/repos/{}/{}/hooks/{}/tests".format(owner, repo, hook_id), **kwargs)

    # 253
    def ping_a_hook(self, owner, repo, hook_id, **kwargs):
        """
        https://developer.github.com/v3/repos/hooks/#ping-a-hook
        """
        return self.post("/repos/{}/{}/hooks/{}/pings".format(owner, repo, hook_id), **kwargs)

    # 254
    def delete_a_hook(self, owner, repo, hook_id, **kwargs):
        """
        https://developer.github.com/v3/repos/hooks/#delete-a-hook
        """
        return self.delete("/repos/{}/{}/hooks/{}/tests".format(owner, repo, hook_id), **kwargs)

    # 255