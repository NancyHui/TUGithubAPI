from core.rest_client import RestClient


class Commits(RestClient):
    # 178
    def list_commits_on_a_repository(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/commits/#list-commits-on-a-repository
        """
        return self.get("/repos/{}/{}/commits".format(owner, repo), **kwargs)

    # 179
    def get_a_single_commit(self, owner, repo, commit_sha, **kwargs):
        """
        https://developer.github.com/v3/repos/commits/#get-a-single-commit
        """
        return self.get("/repos/{}/{}/commits/{}".format(owner, repo, commit_sha), **kwargs)

    # 180
    def get_the_sha_1_of_a_commit_reference(self, owner, repo, ref, **kwargs):
        """
        https://developer.github.com/v3/repos/commits/#get-the-sha-1-of-a-commit-reference
        """
        return self.get("/repos/{}/{}/commits/{}".format(owner, repo, ref), **kwargs)

    # 181
    def compare_two_commits(self, owner, repo, base, head, **kwargs):
        """
        https://developer.github.com/v3/repos/commits/#compare-two-commits
        """
        return self.get("/repos/{}/{}/compare/{}...{}".format(owner, repo, base, head), **kwargs)

    # 182
    def list_branches_for_head_commit(self, owner, repo, commit_sha, **kwargs):
        """
        https://developer.github.com/v3/repos/commits/#list-branches-for-head-commit
        """
        return self.get("/repos/{}/{}/commits/{}/branches-where-head".format(owner, repo, commit_sha), **kwargs)

    # 183
    def list_pull_requests_associated_with_commit(self, owner, repo, commit_sha, **kwargs):
        """
        https://developer.github.com/v3/repos/commits/#list-pull-requests-associated-with-commit
        """
        return self.get("/repos/{}/{}/commits/{}/pulls".format(owner, repo, commit_sha), **kwargs)