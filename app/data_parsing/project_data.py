from . import (
    GeneralInformation,
    ProjectSummary,
    Job,
    DurationResource,
    ResourceAvailability,
)


# Definition for data loaded
class ProjectData:
    def __init__(self):
        self.general_info: GeneralInformation = None
        self.projects_summary: list[ProjectSummary] = []
        self.precedence_relations: list[Job] = []
        self.durations_resources: list[DurationResource] = []
        self.resource_availability: dict[str, ResourceAvailability] = {}
