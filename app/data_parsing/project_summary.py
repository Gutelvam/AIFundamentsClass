class ProjectSummary:
    """
    Represents a summary of a single project.

    Attributes:
        project_number (int): The unique identifier for the project.
        jobs (int): The total number of jobs in the project.
        release_date (int): The earliest start time for the project.
        due_date (int): The deadline by which the project should be completed.
        tardiness_cost (int): The cost incurred per unit time of tardiness.
        mpm_time (int): The minimum project makespan time.
    """
    
    def __init__(
        self, project_number, jobs, release_date, due_date, tardiness_cost, mpm_time
    ):
        self.project_number = project_number
        self.jobs = jobs
        self.release_date = release_date
        self.due_date = due_date
        self.tardiness_cost = tardiness_cost
        self.mpm_time = mpm_time
