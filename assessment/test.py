from constraint import Problem

# Job data: each job has successors
jobs = {
    1: {"successors": [2, 3]},
    2: {"successors": [4]},
    3: {"successors": [4]},
    4: {"successors": []},
    5: {"successors": [6, 7]},
    6: {"successors": [8]},
    7: {"successors": [8]},
    8: {"successors": []},
}

# Duration and resource requirements for each job
job_details = {
    1: {"duration": 2, "R1": 1, "R2": 0},
    2: {"duration": 3, "R1": 0, "R2": 1},
    3: {"duration": 4, "R1": 0, "R2": 1},
    4: {"duration": 1, "R1": 0, "R2": 1},
    5: {"duration": 2, "R1": 1, "R2": 0},
    6: {"duration": 3, "R1": 0, "R2": 1},
    7: {"duration": 4, "R1": 0, "R2": 1},
    8: {"duration": 1, "R1": 0, "R2": 1},
}

# Resource availability
resources = {
    "R1": 1,  # 1 unit available at any time
    "R2": 2,  # 2 units available at any time
}

# Initialize the problem
problem = Problem()

# Define the range for possible start times (assuming max time of 20 for this example)
time_slots = range(21)

# Add start time variables for each job
for job in jobs.keys():
    problem.addVariable(f"start_{job}", time_slots)


# Define successor constraint function (same as before)
def successor_constraint(start_j, start_s, duration):
    """Ensure the successor's start time is after the job's end time."""
    return start_j + duration <= start_s


# Add constraints for job dependencies
for job, details in jobs.items():
    for successor in details["successors"]:
        problem.addConstraint(
            lambda start_j, start_s, duration=job_details[job][
                "duration"
            ]: successor_constraint(start_j, start_s, duration),
            (f"start_{job}", f"start_{successor}"),
        )


# Define resource constraint function
def resource_constraint(*start_times):
    """Ensure resource availability constraints are met at all time slots."""
    # Initialize resource usage tracking across time slots
    usage_R1 = {t: 0 for t in time_slots}
    usage_R2 = {t: 0 for t in time_slots}

    # Calculate each job's active time range and resource needs
    for job, start_time in enumerate(start_times, start=1):
        end_time = start_time + job_details[job]["duration"]
        for t in range(start_time, end_time):

            usage_R1[t] += job_details[job]["R1"]
            usage_R2[t] += job_details[job]["R2"]

            # Check if resource usage exceeds availability
            if usage_R1[t] > resources["R1"] or usage_R2[t] > resources["R2"]:
                return False  # Constraint violated

    return True


# Apply the resource constraint to all jobs' start times
problem.addConstraint(resource_constraint, [f"start_{job}" for job in jobs.keys()])

# Solve the problem
solution = problem.getSolution()
if solution:
    print(solution)
