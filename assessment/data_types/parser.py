import data_types.project_data as project_data
import data_types.parse_types as parse_types


def parse_data(file) -> project_data.ProjectData:
	data = project_data.ProjectData()
	# Track the file section
	section = None

	for line in file:
		line = line.strip()

		# Skip ornament and invalid
		if line.startswith("**") or not line:
			continue

		if line.startswith("#"):
			# Match the file section
			match line:
				case "#General Information":
					section = "general_info"
					continue
				case "#Projects summary":
					section = "projects_summary"
					continue
				case "#Precedence relations":
					section = "precedence_relations"
					continue
				case "#Duration and resources":
					section = "durations_resources"
					continue
				case "#Resource availability":
					section = "resource_availability"
					continue

		match section:
			case "general_info":
				if "projects" in line:
					data.general_info = parse_types.GeneralInformation(
						int(line.split(":")[1].strip()),
						jobs=0,
						horizon=0,
						renewable_resources=0,
						nonrenewable_resources=0,
						doubly_constrained_resources=0,
					)
				elif "jobs" in line:
					data.general_info.jobs = int(line.split(":")[1].strip())
				elif "horizon" in line:
					data.general_info.horizon = int(line.split(":")[1].strip())
				elif line.startswith("- renewable"):
					data.general_info.resources["renewable"] = int(
						line.split(":")[1].split()[0].strip()
					)
				elif line.startswith("- nonrenewable"):
					data.general_info.resources["nonrenewable"] = int(
						line.split(":")[1].split()[0].strip()
					)
				elif line.startswith("- doubly constrained"):
					data.general_info.resources["doubly_constrained"] = int(
						line.split(":")[1].split()[0].strip()
					)

			case "projects_summary":
				# Skip header line
				if line.startswith("pronr."):
					continue

				splits = line.split()
				if splits:
					data.projects_summary.append(
						parse_types.ProjectSummary(
							project_number=int(splits[0]),
							jobs=int(splits[1]),
							release_date=int(splits[2]),
							due_date=int(splits[3]),
							tardiness_cost=int(splits[4]),
							mpm_time=int(splits[5]),
						)
					)

			case "precedence_relations":
				# Skip header line
				if line.startswith("#jobnr."):
					continue

				splits = line.split()
				if splits:
					data.precedence_relations.append(
						parse_types.Job(
							job_number=int(splits[0]),
							successors=list(map(int, splits[3:])),
						)
					)

			case "durations_resources":
				# Skip header line
				if line.startswith("#jobnr."):
					continue

				splits = line.split()
				if splits:
					resourcesData = {}
					for i in range(len(splits) - 3):
						resourcesData[f"R{i+1}"] = int(splits[i + 3])

					data.durations_resources.append(
						parse_types.DurationResource(
							job_number=int(splits[0]),
							mode=int(splits[1]),
							duration=int(splits[2]),
							resources=resourcesData,
						)
					)

			case "resource_availability":
				# Skip header line
				if line.startswith("#resource"):
					continue

				splits = line.split()
				if splits:
					name = splits[0]

					data.resource_availability[name] = parse_types.ResourceAvailability(
						resource_name=name, quantity=int(splits[1])
					)

	return data


def process_solution(solution, pData: project_data.ProjectData):
	"""
	Adjusts the start times in the solution to remove unnecessary offsets, ensuring
    jobs start as early as possible while respecting precedence constraints.

    Args:
        solution (dict): A dictionary mapping job identifiers (e.g., "job_1") 
                        to their respective start times.
        pData (project_data.ProjectData): An object containing project data, 
                                          including precedence relationships 
                                          and general project settings.

    Returns:
        dict: The adjusted solution dictionary with start times shifted so that 
              the earliest start time for jobs without precedence constraints 
              is zero.
	"""
	has_preced = set() 

	for job in pData.precedence_relations:
		for pId in job.successors:
			has_preced.add(f"job_{pId}")

	min_offset = min(solution[key] for key in solution if key not in has_preced)

	for key in solution:
		solution[key] -= min_offset
	
	return solution;