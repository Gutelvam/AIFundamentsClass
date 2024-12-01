class GeneralInformation:
    """
    Holds general metadata about the project.

    Attributes:
        projects (int): The total number of projects.
        jobs (int): The total number of jobs across all projects.
        horizon (int): The planning horizon for the projects.
        resources (dict[str, int]): A dictionary specifying the count of:
            - "renewable": Number of renewable resources.
            - "nonrenewable": Number of nonrenewable resources.
            - "doubly_constrained": Number of doubly constrained resources.
    """

    def __init__(
        self,
        projects,
        jobs,
        horizon,
        renewable_resources,
        nonrenewable_resources,
        doubly_constrained_resources,
    ):
        self.projects = projects
        self.jobs = jobs
        self.horizon = horizon
        self.resources = {
            "renewable": renewable_resources,
            "nonrenewable": nonrenewable_resources,
            "doubly_constrained": doubly_constrained_resources,
        }
