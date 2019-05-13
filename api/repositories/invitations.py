from core.rest_client import RestClient


class Invitation(RestClient):
    # 208

    # 209
    def list_invitations_for_a_repository(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/invitations/#list-invitations-for-a-repository
        """
        return self.get("/repos/{}/{}/invitations".format(owner, repo), **kwargs)

    # 210
    def delete_a_repository_invitation(self, owner, repo, invitation_id, **kwargs):
        """
        https://developer.github.com/v3/repos/invitations/#delete-a-repository-invitation
        """
        return self.delete("/repos/{}/{}/invitations/{}".format(owner, repo, invitation_id), **kwargs)

    # 211
    def update_a_repository_invitation(self, owner, repo, invitation_id, **kwargs):
        """
        https://developer.github.com/v3/repos/invitations/#update-a-repository-invitation
        """
        return self.patch("/repos/{}/{}/invitations/{}".format(owner, repo, invitation_id), **kwargs)

    # 212
    def list_a_user_repository_invitation(self, **kwargs):
        """
        https://developer.github.com/v3/repos/invitations/#list-a-users-repository-invitations
        """
        return self.get("/user/repository_invitations", **kwargs)

    # 213
    def accept_a_repository_invitation(self, invitation_id, **kwargs):
        """
        https://developer.github.com/v3/repos/invitations/#accept-a-repository-invitation
        """
        return self.patch("/user/repository_invitations/{}".format(invitation_id), **kwargs)

    # 214
    def decline_a_repository_invitation(self, invitation_id, **kwargs):
        """
        https://developer.github.com/v3/repos/invitations/#decline-a-repository-invitation
        """
        return self.delete("/user/repository_invitations/{}".format(invitation_id), **kwargs)