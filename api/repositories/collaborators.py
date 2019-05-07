from core.rest_client import RestClient


class Collaborators(RestClient):
    # 166
    def list_collaborators(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/collaborators/#list-collaborators
        """
        return self.get("/repos/{}/{}/collaborators".format(owner, repo), **kwargs)

    # 167
    def check_if_a_user_is_a_collaborator(self, owner, repo, username, **kwargs):
        """
        https://developer.github.com/v3/repos/collaborators/#check-if-a-user-is-a-collaborator
        """
        return self.get("/repos/{}/{}/collaborators/{}".format(owner, repo, username), **kwargs)

    # 168
    def review_a_users_permission_level(self, owner, repo, username, **kwargs):
        """
        https://developer.github.com/v3/repos/collaborators/#review-a-users-permission-level
        """
        return self.get("/repos/{}/{}/collaborators/{}/permission".format(owner, repo, username), **kwargs)

    # 169
    def add_user_a_collaborator(self, owner, repo, username, **kwargs):
        """
        https://developer.github.com/v3/repos/collaborators/#add-user-as-a-collaborator
        """
        return self.put("/repos/{}/{}/collaborators/{}".format(owner, repo, username), **kwargs)

    # 170
    def remove_user_a_collaborator(self, owner, repo, username, **kwargs):
        """
        https://developer.github.com/v3/repos/collaborators/#remove-user-as-a-collaborator
        """
        return self.delete("/repos/{}/{}/collaborators/{}".format(owner, repo, username), **kwargs)