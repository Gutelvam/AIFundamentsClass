from ortools.sat.python import cp_model

from data_parsing import ProjectData


def define_problem(data: ProjectData):
    model: cp_model.CpModel = cp_model.CpModel()
    longest_project = max(
        data.projects_summary, key=lambda summary: summary.due_date
    ).due_date

    # Define variables for start times
    start_times = {}
    intervals = {}

    for job in data.precedence_relations:
        start_times[job.job_number] = model.NewIntVar(
            0, longest_project, f"start_job_{job.job_number}"
        )
        duration = data.durations_resources[job.job_number - 1].duration
        intervals[job.job_number] = model.NewIntervalVar(
            start_times[job.job_number],
            duration,
            start_times[job.job_number] + duration,
            f"interval_job_{job.job_number}",
        )

    # Add precedence constraints
    for job in data.precedence_relations:
        start_var = start_times[job.job_number]
        for successor in job.successors:
            successor_var = start_times[successor]
            model.Add(start_var + duration <= successor_var)

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


    return model, start_times


def extract_solution(solver, start_times, data: ProjectData):
    solution = {}
    for job in data.precedence_relations:
        job_number = job.job_number
        start_time = solver.Value(start_times[job_number])
        solution[f"job_{job_number}"] = start_time

    return solution
