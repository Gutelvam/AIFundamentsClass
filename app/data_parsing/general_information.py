class GeneralInformation:
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
