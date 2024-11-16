from data_types.project_data import *
from data_types.parse_types import *

import csp_solver.defined_constraints as dConstraint

from constraint import *


def define_problem(data: ProjectData):
    domain = range(data.general_info.horizon + 1)
    start_times = [f"job_{job.job_number}" for job in data.precedence_relations];

    problem = Problem()

    # Define variables for each job, and the domain are the available time on the horizon (20 days)
    for job in data.precedence_relations:
        number = job.job_number
        var_name = f"job_{number}"

        problem.addVariable(var_name, domain)

    for job in data.precedence_relations:
        for successor in job.successors:
            duration = data.durations_resources[job.job_number].duration

            problem.addConstraint(
                lambda start_j, start_s, duration=duration: dConstraint.sucessor_constraint(
                    start_j, start_s, duration
                ),
                (f"job_{job.job_number}", f"job_{successor}"),
            )

    problem.addConstraint(
        lambda *start_times: dConstraint.resource_constraint(
            *start_times, time_slots=domain, project_data=data
        ),
        start_times,
    )

    # problem.addConstraint(lambda start : start == 0, ("job_1",))

    # problem.addConstraint(
    #     lambda *start_times: dConstraint.makespan_constraint(
    #         *start_times, project_data=data, horizon=data.general_info.horizon
    #     ),
    #     start_times
    # )

    # problem.addConstraint(
    #     lambda *start_times: dConstraint.full_resource_utilization_constraint(*start_times, time_slots=domain, project_data=data),
    #     start_times
    # )

    return problem
