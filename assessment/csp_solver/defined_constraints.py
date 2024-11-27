import data_types.project_data as ProjData
from data_types.parse_types import *


def successor_constraint(start_job, start_successor, duration):
    return start_job + duration <= start_successor


def resource_constraint(*start_times, time_slots, project_data: ProjData.ProjectData):
    resource_usage = {
        resource: [0] * len(time_slots) for resource in project_data.resource_availability.keys()
    }

    # Update resources only for active times
    for job_index, start_time in enumerate(start_times):
        job_data = project_data.durations_resources[job_index]
        end_time = start_time + job_data.duration

        # Mark the resources used in the relevant time slots
        for t in range(start_time, end_time):
            if t >= len(time_slots):
                break  # Stay within time slots
            
            for resource, amount in job_data.resources.items():
                resource_usage[resource][t] += amount

    # Check if resources exceed availability
    for t in range(len(time_slots)):
        for resource, usage in resource_usage.items():
            if usage[t] > project_data.resource_availability[resource].quantity:
                return False  # Constraint violated

    return True


def due_date_constraint(*start_times, project_data: ProjData.ProjectData):
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