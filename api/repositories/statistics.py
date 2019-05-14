from core.rest_client import RestClient


class Statistics(RestClient):
    # 236
    def get_contributors_list_with_additions_deletions_and_commit_counts(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/statistics/#get-contributors-list-with-additions-deletions-and-commit-counts
        """
        return self.get("/repos/{}/{}/stats/contributors".format(owner, repo), **kwargs)

    # 237
    def get_the_last_year_of_commit_activity_data(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/statistics/#get-the-last-year-of-commit-activity-data
        """
        return self.get("/repos/{}/{}/stats/commit_activity".format(owner, repo), **kwargs)

    # 238
    def get_the_number_of_addtions_and_deletions_per_week(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/statistics/#get-the-number-of-additions-and-deletions-per-week
        """
        return self.get("/repos/{}/{}/stats/code_frequency".format(owner, repo), **kwargs)

    # 239
    def get_the_weekly_commit_count_for_the_repository_owner_and_everyone_else(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/statistics/#get-the-weekly-commit-count-for-the-repository-owner-and-everyone-else
        """
        return self.get("/repos/{}/{}/stats/participation".format(owner, repo), **kwargs)

    # 240
    def get_the_number_of_commits_per_hour_in_each_day(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/statistics/#get-the-number-of-commits-per-hour-in-each-day
        """
        return self.get("/repos/{}/{}/stats/punch_card".format(owner, repo), **kwargs)