from data_parsing import ProjectData


def resource_constraint(*start_times, time_slots, project_data: ProjectData):
    resource_usage = {
        resource: [0] * len(time_slots)
        for resource in project_data.resource_availability.keys()
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
