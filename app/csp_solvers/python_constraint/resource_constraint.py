from data_parsing import ProjectData


def resource_constraint(*start_times, time_slots, project_data: ProjectData):
    """
    Ensures that the total resource usage at any time does not exceed the available resource quantities.

    This function checks the resource usage for each job over the defined time slots,
    and ensures that the resources used at any given time do not exceed the available quantity.

    Args:
        *start_times (int): The start times for all jobs.
        time_slots (range): The range of time slots over which resources are being tracked.
        project_data (ProjectData): The project data containing resource availability and job resource requirements.

    Returns:
        bool: True if resource usage does not exceed availability, False if the constraint is violated.
    """
    # Initialize resource usage for each resource type (renewable, nonrenewable, etc.)
    resource_usage = {
        resource: [0] * len(time_slots)
        for resource in project_data.resource_availability.keys()
    }

    # Update resource usage for active jobs during their assigned time slots
    for job_index, start_time in enumerate(start_times):
        job_data = project_data.durations_resources[job_index]
        end_time = start_time + job_data.duration

        for t in range(start_time, end_time):
            if t >= len(time_slots):
                break

            for resource, amount in job_data.resources.items():
                resource_usage[resource][t] += amount

    # Check if resource usage at any time exceeds the available quantity for any resource
    for t in range(len(time_slots)):
        for resource, usage in resource_usage.items():
            if usage[t] > project_data.resource_availability[resource].quantity:
                return False  # Constraint violated

    # If all checks pass, return True indicating no resource constraints are violated
    return True
