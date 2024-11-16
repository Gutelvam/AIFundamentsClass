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


# def makespan_constraint(*start_times, project_data: ProjData.ProjectData, horizon):
#     # Find the latest finish time (max finish time of all jobs)
#     latest_finish_time = 0
#     for job_index, start_time in enumerate(start_times):
#         job_data = project_data.durations_resources[job_index]
#         finish_time = start_time + job_data.duration
#         latest_finish_time = max(latest_finish_time, finish_time)

#     # Ensure that the latest finish time doesn't exceed the available horizon
#     return latest_finish_time <= horizon


# def full_resource_utilization_constraint(*start_times, time_slots, project_data: ProjData.ProjectData):
#     usage_R1 = [0] * len(time_slots)
#     usage_R2 = [0] * len(time_slots)

#     # Track resource usage for each job over time slots
#     for job_index, start_time in enumerate(start_times):
#         job_data = project_data.durations_resources[job_index]
#         end_time = start_time + job_data.duration

#         # Mark the resources used in the relevant time slots
#         for t in range(start_time, end_time):
#             if t >= len(time_slots):
#                 break  # Stay within time slots
            
#             usage_R1[t] += job_data.resources["R1"]
#             usage_R2[t] += job_data.resources["R2"]

#     # Ensure that if a resource is used at a time slot, it must continue to be used until the job is completed
#     for t in range(1, len(time_slots)):
#         if usage_R1[t] == 0 and usage_R1[t-1] > 0:
#             return False  # R1 was in use before t, but not at t (idle time for R1)
#         if usage_R2[t] == 0 and usage_R2[t-1] > 0:
#             return False  # R2 was in use before t, but not at t (idle time for R2)

#     # Ensure that at no time does the resource usage exceed the available resource capacity
#     for t in range(len(time_slots)):
#         if (
#             usage_R1[t] > project_data.resource_availability["R1"].quantity
#             or usage_R2[t] > project_data.resource_availability["R2"].quantity
#         ):
#             return False  # Constraint violated (resources exceed availability)

#     return True