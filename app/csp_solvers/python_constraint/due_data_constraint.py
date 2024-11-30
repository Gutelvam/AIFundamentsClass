from data_parsing import ProjectData


def due_date_constraint(*start_times, project_data: ProjectData):
    durations = [dr.duration for dr in project_data.durations_resources]
    due_date = project_data.projects_summary[0].due_date

    # Identify all sink jobs (jobs with no successors)
    sink_jobs = []
    for i, job in enumerate(project_data.precedence_relations):
        if not job.successors:  # Job with no successors
            sink_jobs.append(i)

    if not sink_jobs:
        raise ValueError("No sink jobs found in precedence relations!")

    # Compute the completion times of all sink jobs
    latest_completion_time = 0
    for sink_job_index in sink_jobs:
        sink_job_start_time = start_times[sink_job_index]
        sink_job_duration = durations[sink_job_index]
        sink_job_completion_time = sink_job_start_time + sink_job_duration

        # Track the latest completion time
        latest_completion_time = max(latest_completion_time, sink_job_completion_time)

    # Ensure the latest completion time respects the due date
    return latest_completion_time <= due_date
