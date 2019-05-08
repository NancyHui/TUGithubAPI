from core.rest_client import RestClient


class Comments(RestClient):
    # 171
    def list_commit_comments_for_a_repository(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/comments/#list-commit-comments-for-a-repository
        """
        return self.get("/repos/{}/{}/comments".format(owner, repo), **kwargs)

    # 172
    def list_comments_for_a_single_commit(self, owner, repo, ref, **kwargs):
        """
        https://developer.github.com/v3/repos/comments/#list-comments-for-a-single-commit
        :param ref: The name of the commit/branch/tag
        """
        return self.get("/repos/{}/{}/commits/{}/comments".format(owner, repo, ref), **kwargs)

    # 173
    def create_a_commit_comment(self, owner, repo, sha, **kwargs):
        """
        https://developer.github.com/v3/repos/comments/#create-a-commit-comment
        :param sha: SHA or branch
        """
        return self.post("/repos/{}/{}/commits/{}/comments".format(owner, repo, sha), **kwargs)

    # 174
    def get_a_single_commit_comment(self, owner, repo, comment_id, **kwargs):
        """
        https://developer.github.com/v3/repos/comments/#get-a-single-commit-comment
        """
        return self.get("/repos/{}/{}/comments/{}".format(owner, repo, comment_id), **kwargs)

    # 175
    def update_a_commit_comment(self, owner, repo, comment_id, **kwargs):
        """
        https://developer.github.com/v3/repos/comments/#update-a-commit-comment
        """
        return self.patch("/repos/{}/{}/comments/{}".format(owner, repo, comment_id), **kwargs)

    # 176
    def delete_a_commit_comment(self, owner, repo, comment_id, **kwargs):
        """
        https://developer.github.com/v3/repos/comments/#delete-a-commit-comment
        """
        return self.delete("/repos/{}/{}/comments/{}".format(owner, repo, comment_id), **kwargs)

    # 177

