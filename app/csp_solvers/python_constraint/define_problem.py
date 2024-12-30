from constraint import Problem
from data_parsing import ProjectData

from .successor_constraint import successor_constraint
from .resource_constraint import resource_constraint


def define_problem(data: ProjectData) -> Problem:
    """
    Defines the constraint satisfaction problem (CSP) for scheduling jobs with precedence
    and resource constraints.

    Args:
        data (ProjectData): The project data containing job precedence relations,
                            durations, and resource information.

    Returns:
        Problem: The defined CSP with variables, constraints, and domains.
    """

    # Define the domain for the job start times, ranging from 0 to horizon (e.g., 20 days)
    domain = range(data.general_info.horizon)

    # Create a list of job start time variables (e.g., "job_1", "job_2", ...)
    start_times = [f"job_{job.job_number}" for job in data.precedence_relations]

    problem = Problem()

    # Define variables for each job, and the domain are the available time on the horizon
    for job in data.precedence_relations:
        number = job.job_number
        var_name = f"job_{number}"

        # Add the job variable with its possible start times (domain)
        problem.addVariable(var_name, domain)

        # Add precedence constraints between jobs and their successors
        for successor in job.successors:
            # Get the duration for the current job from the durations/resources data
            duration = data.durations_resources[number - 1].duration

            # Add a constraint to ensure that a job starts before its successor with a gap
            problem.addConstraint(
                lambda start_j, start_s, duration=duration: successor_constraint(
                    start_j, start_s, duration
                ),
                (f"job_{number}", f"job_{successor}"),
            )

    # Add a resource constraint to ensure that resources are not overbooked
    problem.addConstraint(
        lambda *start_times: resource_constraint(
            *start_times, time_slots=domain, project_data=data
        ),
        start_times,
    )

    return problem
