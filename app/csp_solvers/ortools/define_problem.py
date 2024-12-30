from ortools.sat.python import cp_model

from data_parsing import ProjectData


def define_problem(data: ProjectData):
    """
    Defines a constraint optimization problem using Google OR-Tools.

    This function creates a constraint programming model where jobs are assigned start times,
    end times, and intervals. Precedence constraints (i.e., a job must finish before its successor
    starts) and resource constraints (i.e., resource availability is respected) are added to the model.
    The objective is to minimize the makespan, which is the time required to complete all jobs.

    Args:
        data (ProjectData): The project data containing job precedence relations, durations,
                            resource availability, and other information.

    Returns:
        tuple: A tuple containing:
            - model (cp_model.CpModel): The constraint programming model.
            - start_times (dict): A dictionary of start time variables for each job.
    """

    model: cp_model.CpModel = cp_model.CpModel()
    horizon = data.general_info.horizon

    # Define variables for start times
    start_times = {}
    end_times = {}
    intervals = {}

    # Create variables and intervals for each job
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

    # Add precedence constraints: Ensure each job finishes before its successor starts
    for job in data.precedence_relations:
        for successor in job.successors:
            model.Add(end_times[job.job_number] <= start_times[successor])

    # Add resource constraints: Ensure resource usage does not exceed availability
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

    # Define makespan variable and constrain it to be the maximum end time of all jobs
    makespan = model.NewIntVar(0, horizon, "makespan")
    for job in data.precedence_relations:
        model.Add(makespan >= end_times[job.job_number])

    # Set the objective to minimize makespan
    model.Minimize(makespan)

    return model, start_times


def extract_solution(solver, start_times, data: ProjectData):
    """
    Extracts the solution for job start times from the solver.

    After the solver has found a solution, this function extracts the start times
    for each job from the solver and returns them in a dictionary.

    Args:
        solver (cp_model.CpSolver): The solver used to solve the constraint programming model.
        start_times (dict): A dictionary of start time variables for each job.
        data (ProjectData): The project data (used here for job precedence relations).

    Returns:
        dict: A dictionary where keys are job names (e.g., "job_1") and values are the corresponding
            start times as determined by the solver.
    """

    solution = {}
    for job in data.precedence_relations:
        job_number = job.job_number
        start_time = solver.Value(start_times[job_number])
        solution[f"job_{job_number}"] = start_time

    return solution
