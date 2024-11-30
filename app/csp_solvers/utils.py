from data_parsing import ProjectData


def process_solution(solution, pData: ProjectData):
    has_preced = set()

    for job in pData.precedence_relations:
        for pId in job.successors:
            has_preced.add(f"job_{pId}")

    min_offset = min(solution[key] for key in solution if key not in has_preced)

    for key in solution:
        solution[key] -= min_offset

    return solution
