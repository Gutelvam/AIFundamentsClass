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

    def __str__(self):
        return "\n".join(
            [
                f"Projects: {self.projects}",
                f"Jobs: {self.jobs}",
                f"Horizon: {self.horizon}",
                f"Resources: {self.resources}",
            ]
        )


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

    def __str__(self):
        return "\n".join(
            [
                f"  - Project Number: {self.project_number}",
                f"\tJobs: {self.jobs}",
                f"\tRelease Date: {self.release_date}",
                f"\tDue Date: {self.due_date}",
                f"\tTardiness Cost: {self.tardiness_cost}",
                f"\tMPM Time: {self.mpm_time}",
            ]
        )


class Job:
    def __init__(self, job_number, successors):
        self.job_number = job_number
        self.successors = successors

    def get_successors_count(self):
        return len(self.successors)

    def __str__(self):
        return "\n".join(
            [
                f"  - Job Number: {self.job_number}",
                f"\tSuccessors Count: {self.get_successors_count()}",
                f"\tSuccessors: {', '.join(map(str, self.successors)) if self.successors else 'None'}",
            ]
        )


class DurationResource:
    def __init__(self, job_number, mode, duration, resources):
        self.job_number = job_number
        self.mode = mode
        self.duration = duration
        self.resources = resources

    def __str__(self):
        return "\n".join(
            [
                f"  - Job Number: {self.job_number}",
                f"\tMode: {self.mode}",
                f"\tDuration: {self.duration} days",
                f"\tResources: {', '.join([f'{key}: {value}' for key, value in self.resources.items()]) if self.resources else 'None'}",
            ]
        )


class ResourceAvailability:
    def __init__(self, resource_name, quantity):
        self.resource_name = resource_name
        self.quantity = quantity

    def __str__(self):
        return f"  - Resource: {self.resource_name}\n\tQuantity: {self.quantity}"
