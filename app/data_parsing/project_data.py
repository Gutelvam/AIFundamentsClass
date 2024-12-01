from . import (
    GeneralInformation,
    ProjectSummary,
    Job,
    DurationResource,
    ResourceAvailability,
)


# Definition for data loaded
class ProjectData:
    """
    Stores all parsed data for a project.

    Attributes:
        general_info (GeneralInformation): Metadata about the project, such as the number of jobs and resources.
        projects_summary (list[ProjectSummary]): A list summarizing project details like release dates and deadlines.
        precedence_relations (list[Job]): A list of jobs and their precedence relationships.
        durations_resources (list[DurationResource]): A list of job durations and their resource requirements.
        resource_availability (dict[str, ResourceAvailability]): A dictionary mapping resource names to their availability.
    """
    def __init__(self):
        self.general_info: GeneralInformation = None
        self.projects_summary: list[ProjectSummary] = []
        self.precedence_relations: list[Job] = []
        self.durations_resources: list[DurationResource] = []
        self.resource_availability: dict[str, ResourceAvailability] = {}
