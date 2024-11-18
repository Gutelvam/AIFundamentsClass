import data_types.project_data as ProjData
from data_types.parse_types import *


def sucessor_constraint(start_job, start_successor, duration):
    return start_job + duration <= start_successor


def resource_constraint(*start_times, time_slots, project_data: ProjData.ProjectData):
    usage_R1 = [0] * len(time_slots)
    usage_R2 = [0] * len(time_slots)

    # Update resources only for active times
    for job_index, start_time in enumerate(start_times):
        job_data = project_data.durations_resources[job_index]
        end_time = start_time + job_data.duration

        # Mark the resources used in the relevant time slots
        for t in range(start_time, end_time):
            if t >= len(time_slots):
                break  # Stay within time slots
            
            usage_R1[t] += job_data.resources["R1"]
            usage_R2[t] += job_data.resources["R2"]

    # Check if resources exceed availability
    for t in range(len(time_slots)):
        if (
            usage_R1[t] > project_data.resource_availability["R1"].quantity
            or usage_R2[t] > project_data.resource_availability["R2"].quantity
        ):
            return False  # Constraint violated

    return True
