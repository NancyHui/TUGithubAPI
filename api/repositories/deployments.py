from core.rest_client import RestClient


class Deployments(RestClient):
    # 196
    def list_deployments(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/deployments/#list-deployments
        """
        return self.get("/repos/{}/{}/deployments".format(owner, repo), **kwargs)

    # 197
    def get_a_single_deployment(self, owner, repo, deployment_id, **kwargs):
        """
        https://developer.github.com/v3/repos/deployments/#get-a-single-deployment
        """
        return self.get("/repos/{}/{}/deployments/{}".format(owner, repo, deployment_id), **kwargs)

    # 198
    def create_a_deployment(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/deployments/#create-a-deployment
        """
        return self.post("/repos/{}/{}/deployments".format(owner, repo), **kwargs)

    # 199

    # 200
    def list_deployment_statuses(self, owner, repo, deployment_id, **kwargs):
        """
        https://developer.github.com/v3/repos/deployments/#list-deployment-statuses
        """
        return self.get("/repos/{}/{}/deployments/{}/statuses".format(owner, repo, deployment_id), **kwargs)

    # 201
    def get_a_single_deployment_status(self, owner, repo, deployment_id, status_id, **kwargs):
        """
        https://developer.github.com/v3/repos/deployments/#get-a-single-deployment-status
        """
        return self.get("/repos/{}/{}/deployments/{}/statuses/{}".format(owner, repo, deployment_id, status_id), **kwargs)

    # 202
    def create_a_deployment_status(self, owner, repo, deployment_id, **kwargs):
        """
        https://developer.github.com/v3/repos/deployments/#create-a-deployment-status
        """
        return self.post("/repos/{}/{}/deployments/{}/statuses".format(owner, repo, deployment_id), **kwargs)