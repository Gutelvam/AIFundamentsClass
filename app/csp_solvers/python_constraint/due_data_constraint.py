from data_parsing import ProjectData


def due_date_constraint(*start_times, project_data: ProjectData):
    """
    Ensures that the latest completion time of sink jobs (jobs with no successors)
    does not exceed the project's due date.

    Args:
        *start_times (int): The start times of all jobs.
        project_data (ProjectData): The project data containing job durations, precedence relations,
                                    and project due date.

    Returns:
        bool: True if the latest completion time of sink jobs is less than or equal to the due date,
            otherwise False.

    Raises:
        ValueError: If no sink jobs are found in the project data.
    """
    # Extract durations of all jobs
    durations = [dr.duration for dr in project_data.durations_resources]

    # Get the project's due date
    due_date = project_data.projects_summary[0].due_date

    # Identify all sink jobs (jobs with no successors)
    sink_jobs = []
    for i, job in enumerate(project_data.precedence_relations):
        if not job.successors:
            sink_jobs.append(i)

    # If no sink jobs are found, raise an error
    if not sink_jobs:
        raise ValueError("No sink jobs found in precedence relations!")

    # Compute the completion times of all sink jobs and track the latest completion time
    latest_completion_time = 0
    for sink_job_index in sink_jobs:
        sink_job_start_time = start_times[sink_job_index]
        sink_job_duration = durations[sink_job_index]
        sink_job_completion_time = sink_job_start_time + sink_job_duration

        latest_completion_time = max(latest_completion_time, sink_job_completion_time)

    # Ensure the latest completion time respects the due date
    return latest_completion_time <= due_date
