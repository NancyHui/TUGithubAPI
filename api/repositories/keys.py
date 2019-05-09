from core.rest_client import RestClient


class Keys(RestClient):
    # 191
    def list_deploy_keys(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/keys/#list-deploy-keys
        """
        return self.get("/repos/{}/{}/keys".format(owner, repo), **kwargs)

    # 192
    def get_a_deploy_key(self, owner, repo, key_id, **kwargs):
        """
        https://developer.github.com/v3/repos/keys/#get-a-deploy-key
        """
        return self.get("/repos/{}/{}/keys/{}".format(owner, repo, key_id), **kwargs)

    # 193
    def add_a_new_deploy_key(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/keys/#add-a-new-deploy-key
        """
        return self.post("/repos/{}/{}/keys".format(owner, repo), **kwargs)

    # 194

    # 195
    def remove_a_deploy_key(self, owner, repo, key_id, **kwargs):
        """
        https://developer.github.com/v3/repos/keys/#remove-a-deploy-key
        """
        return self.delete("/repos/{}/{}/keys/{}".format(owner, repo, key_id), **kwargs)