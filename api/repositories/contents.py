from core.rest_client import RestClient


class Contents(RestClient):
    # 184
    def get_the_readme(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/contents/#get-the-readme
        """
        return self.get("/repos/{}/{}/readme".format(owner, repo), **kwargs)

    # 185
    def get_contents(self, owner, repo, path, **kwargs):
        """
        https://developer.github.com/v3/repos/contents/#get-contents
        """
        return self.get("/repos/{}/{}/contents/{}".format(owner, repo, path), **kwargs)

    # 186
    def create_a_file(self, owner, repo, path, **kwargs):
        """
        https://developer.github.com/v3/repos/contents/#create-a-file
        """
        return self.put("/repos/{}/{}/contents/{}".format(owner, repo, path), **kwargs)

    # 187
    def update_a_file(self, owner, repo, path, **kwargs):
        """
        https://developer.github.com/v3/repos/contents/#update-a-file
        """
        return self.put("/repos/{}/{}/contents/{}".format(owner, repo, path), **kwargs)

    # 188
    def delete_a_file(self, owner, repo, path, **kwargs):
        """
        https://developer.github.com/v3/repos/contents/#delete-a-file
        """
        return self.delete("/repos/{}/{}/contents/{}".format(owner, repo, path), **kwargs)

    # 189
    def get_archive_link(self, owner, repo, archive_format, ref, **kwargs):
        """
        https://developer.github.com/v3/repos/contents/#get-archive-link
        """
        return self.get("/repos/{}/{}/{}/{}".format(owner, repo, archive_format, ref), **kwargs)

    # 190
