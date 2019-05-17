from core.rest_client import RestClient


class Teams(RestClient):
    def __init__(self, api_host, **kwargs):
        super(Teams, self).__init__(api_host, **kwargs)

    # 277
    def list_teams(self, org, **kwargs):
        """
        https://developer.github.com/v3/teams/#list-teams
        """
        return self.get("/orgs/{}/teams".format(org), **kwargs)

    # 278
    def get_team(self, team_id, **kwargs):
        """
        https://developer.github.com/v3/teams/#get-team
        """
        return self.get("/teams/{}".format(team_id), **kwargs)

    # 279
    def get_team_by_name(self, org, team_slug, **kwargs):
        """
        https://developer.github.com/v3/teams/#get-team-by-name
        """
        return self.get("/orgs/{}/teams/{}".format(org, team_slug), **kwargs)

    # 280
    def create_team(self, org, **kwargs):
        """
        https://developer.github.com/v3/teams/#create-team
        """
        return self.post("/orgs/{}/teams".format(org), **kwargs)

    # 281
    def edit_team(self, team_id, **kwargs):
        """
        https://developer.github.com/v3/teams/#edit-team
        """
        return self.patch("/teams/{}".format(team_id), **kwargs)

    # 282
    def delete_team(self, team_id, **kwargs):
        """
        https://developer.github.com/v3/teams/#delete-team
        """
        return self.delete("/teams/{}".format(team_id), **kwargs)

    # 283
    def list_child_teams(self, team_id, **kwargs):
        """
        https://developer.github.com/v3/teams/#list-child-teams
        """
        return self.get("/teams/{}/teams".format(team_id), **kwargs)

    # 284
    def list_team_repos(self, team_id, **kwargs):
        """
        https://developer.github.com/v3/teams/#list-team-repos
        """
        return self.get("/teams/{}/repos".format(team_id), **kwargs)

    # 285
    def check_if_a_team_manages_a_repository(self, team_id, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/teams/#check-if-a-team-manages-a-repository
        """
        return self.get("/teams/{}/repos/{}/{}".format(team_id, owner, repo), **kwargs)

    # 286
    def add_or_update_team_repository(self, team_id, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/teams/#add-or-update-team-repository
        """
        return self.put("/teams/{}/repos/{}/{}".format(team_id, owner, repo), **kwargs)

    # 287
    def remove_team_repository(self, team_id, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/teams/#remove-team-repository
        """
        return self.delete("/teams/{}/repos/{}/{}".format(team_id, owner, repo), **kwargs)
