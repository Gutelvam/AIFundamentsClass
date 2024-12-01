from ortools.sat.python import cp_model

from data_parsing import ProjectData


def define_problem(data: ProjectData):
    model: cp_model.CpModel = cp_model.CpModel()
    horizon = data.general_info.horizon

    # Define variables for start times
    start_times = {}
    end_times = {}
    intervals = {}

    for job in data.precedence_relations:
        start_times[job.job_number] = model.NewIntVar(
            0, horizon, f"start_job_{job.job_number}"
        )
        duration = data.durations_resources[job.job_number - 1].duration
        end_times[job.job_number] = model.NewIntVar(
            0, horizon, f"end_job_{job.job_number}"
        )
        intervals[job.job_number] = model.NewIntervalVar(
            start_times[job.job_number],
            duration,
            end_times[job.job_number],
            f"interval_job_{job.job_number}",
        )
        model.Add(end_times[job.job_number] == start_times[job.job_number] + duration)

    # Add precedence constraints
    for job in data.precedence_relations:
        for successor in job.successors:
            model.Add(end_times[job.job_number] <= start_times[successor])

    # Add resource constraints
    for resource_name, resource_availability in data.resource_availability.items():
        tasks = []
        demands = []

        for duration_resource in data.durations_resources:
            demand = duration_resource.resources.get(resource_name, 0)
            if demand > 0:
                tasks.append(intervals[duration_resource.job_number])
                demands.append(demand)

        # Add cumulative constraint for this resource
        if tasks:
            model.AddCumulative(
                intervals=tasks,
                demands=demands,
                capacity=resource_availability.quantity,
            )

    # Define makespan variable
    makespan = model.NewIntVar(0, horizon, "makespan")

    # Constrain makespan to be the maximum of all end times
    for job in data.precedence_relations:
        model.Add(makespan >= end_times[job.job_number])

    # Set the objective to minimize makespan
    model.Minimize(makespan)

    return model, start_times


def extract_solution(solver, start_times, data: ProjectData):
    solution = {}
    for job in data.precedence_relations:
        job_number = job.job_number
        start_time = solver.Value(start_times[job_number])
        solution[f"job_{job_number}"] = start_time

    return solution
