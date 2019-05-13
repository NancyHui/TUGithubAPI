from core.rest_client import RestClient


class Pages(RestClient):
    # 216
    def get_information_about_a_pages_site(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/pages/#get-information-about-a-pages-site
        """
        return self.get("/repos/{}/{}/pages".format(owner, repo), **kwargs)

    # 217
    def enable_a_pages_site(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/pages/#enable-a-pages-site
        """
        return self.post("/repos/{}/{}/pages".format(owner, repo), **kwargs)

    # 218
    def disable_a_pages_site(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/pages/#disable-a-pages-site
        """
        return self.delete("/repos/{}/{}/pages".format(owner, repo), **kwargs)

    # 219
    def update_information_about_a_pages_site(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/pages/#update-information-about-a-pages-site
        """
        return self.put("/repos/{}/{}/pages".format(owner, repo), **kwargs)

    # 220
    def request_a_page_build(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/pages/#request-a-page-build
        """
        return self.post("/repos/{}/{}/pages/builds".format(owner, repo), **kwargs)

    # 221
    def list_pages_bulids(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/pages/#list-pages-builds
        """
        return self.get("/repos/{}/{}/pages/builds".format(owner, repo), **kwargs)

    # 222
    def get_latest_pages_build(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/pages/#get-latest-pages-build
        """
        return self.get("/repos/{}/{}/pages/builds/latest".format(owner, repo), **kwargs)

    # 223
    def get_a_special_pages_bulid(self, owner, repo, build_id, **kwargs):
        """
        https://developer.github.com/v3/repos/pages/#get-a-specific-pages-build
        """
        return self.get("/repos/{}/{}/pages/builds/{}".format(owner, repo, build_id), **kwargs)