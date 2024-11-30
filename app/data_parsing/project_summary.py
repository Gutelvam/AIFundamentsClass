class ProjectSummary:
    def __init__(
        self, project_number, jobs, release_date, due_date, tardiness_cost, mpm_time
    ):
        self.project_number = project_number
        self.jobs = jobs
        self.release_date = release_date
        self.due_date = due_date
        self.tardiness_cost = tardiness_cost
        self.mpm_time = mpm_time
