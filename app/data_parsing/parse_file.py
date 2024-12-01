from . import (
    ProjectData,
    GeneralInformation,
    ProjectSummary,
    Job,
    DurationResource,
    ResourceAvailability,
)


def parse_file(file) -> ProjectData:
    """
    Parses a project data file into a ProjectData object.

    Processes sections like general information, project summaries, precedence relations,
    durations/resources, and resource availability, extracting relevant details into structured data.

    Args:
        file: An open file object containing the project data.

    Returns:
        ProjectData: Parsed data with project details, jobs, resources, and constraints.
    """

    data = ProjectData()
    # Track the file section
    section = None

    for line in file:
        line = line.strip()

        # Skip ornament and invalid
        if line.startswith("**") or not line:
            continue

        if line.startswith("#"):
            # Match the file section
            match line:
                case "#General Information":
                    section = "general_info"
                    continue
                case "#Projects summary":
                    section = "projects_summary"
                    continue
                case "#Precedence relations":
                    section = "precedence_relations"
                    continue
                case "#Duration and resources":
                    section = "durations_resources"
                    continue
                case "#Resource availability":
                    section = "resource_availability"
                    continue

        match section:
            case "general_info":
                if "projects" in line:
                    data.general_info = GeneralInformation(
                        int(line.split(":")[1].strip()),
                        jobs=0,
                        horizon=0,
                        renewable_resources=0,
                        nonrenewable_resources=0,
                        doubly_constrained_resources=0,
                    )
                elif "jobs" in line:
                    data.general_info.jobs = int(line.split(":")[1].strip())
                elif "horizon" in line:
                    data.general_info.horizon = int(line.split(":")[1].strip())
                elif line.startswith("- renewable"):
                    data.general_info.resources["renewable"] = int(
                        line.split(":")[1].split()[0].strip()
                    )
                elif line.startswith("- nonrenewable"):
                    data.general_info.resources["nonrenewable"] = int(
                        line.split(":")[1].split()[0].strip()
                    )
                elif line.startswith("- doubly constrained"):
                    data.general_info.resources["doubly_constrained"] = int(
                        line.split(":")[1].split()[0].strip()
                    )

            case "projects_summary":
                # Skip header line
                if line.startswith("pronr."):
                    continue

                splits = line.split()
                if splits:
                    data.projects_summary.append(
                        ProjectSummary(
                            project_number=int(splits[0]),
                            jobs=int(splits[1]),
                            release_date=int(splits[2]),
                            due_date=int(splits[3]),
                            tardiness_cost=int(splits[4]),
                            mpm_time=int(splits[5]),
                        )
                    )

            case "precedence_relations":
                # Skip header line
                if line.startswith("#jobnr."):
                    continue

                splits = line.split()
                if splits:
                    data.precedence_relations.append(
                        Job(
                            job_number=int(splits[0]),
                            successors=list(map(int, splits[3:])),
                        )
                    )

            case "durations_resources":
                # Skip header line
                if line.startswith("#jobnr."):
                    continue

                splits = line.split()
                if splits:
                    resourcesData: dict[str, int] = {}
                    for i in range(len(splits) - 3):
                        resourcesData[f"R{i+1}"] = int(splits[i + 3])

                    data.durations_resources.append(
                        DurationResource(
                            job_number=int(splits[0]),
                            mode=int(splits[1]),
                            duration=int(splits[2]),
                            resources=resourcesData,
                        )
                    )

            case "resource_availability":
                # Skip header line
                if line.startswith("#resource"):
                    continue

                splits = line.split()
                if splits:
                    name = splits[0]

                    data.resource_availability[name] = ResourceAvailability(
                        resource_name=name, quantity=int(splits[1])
                    )

    return data
