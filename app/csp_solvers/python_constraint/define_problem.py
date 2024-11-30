from constraint import Problem
from data_parsing import project_data

from .successor_constraint import successor_constraint
from .resource_constraint import resource_constraint


def define_problem(data: project_data.ProjectData) -> Problem:
    longestProject = max(
        data.projects_summary, key=lambda summary: summary.due_date
    ).due_date

    domain = range(longestProject + 1)
    start_times = [f"job_{job.job_number}" for job in data.precedence_relations]

    problem = Problem()

    # Define variables for each job, and the domain are the available time on the horizon (20 days)
    for job in data.precedence_relations:
        number = job.job_number
        var_name = f"job_{number}"

        problem.addVariable(var_name, domain)

        for successor in job.successors:
            duration = data.durations_resources[number - 1].duration

            problem.addConstraint(
                lambda start_j, start_s, duration=duration: successor_constraint(
                    start_j, start_s, duration
                ),
                (f"job_{number}", f"job_{successor}"),
            )

    problem.addConstraint(
        lambda *start_times: resource_constraint(
            *start_times, time_slots=domain, project_data=data
        ),
        start_times,
    )

    return problem
