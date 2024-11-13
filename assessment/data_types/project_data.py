# Definition for data loaded
class ProjectData:
	def __init__(self):
		self.general_info = None
		self.projects_summary = []
		self.precedence_relations = []
		self.durations_resources = []
		self.resource_availability = {} 

	def __str__(self):
		result = []

		# General Info
		result.append("General Information:")
		if self.general_info:
				result.append(str(self.general_info))
		else:
				result.append("  None")
		
		# Projects Summary
		result.append("\nProjects Summary:")
		if self.projects_summary:
				for summary in self.projects_summary:
						result.append(str(summary))
		else:
				result.append("  None")
		
		# Precedence Relations
		result.append("\nPrecedence Relations:")
		if self.precedence_relations:
				for relation in self.precedence_relations:
						result.append(str(relation))
		else:
				result.append("  None")
		
		# Durations and Resources
		result.append("\nDurations and Resources:")
		if self.durations_resources:
				for resource in self.durations_resources:
						result.append(str(resource))
		else:
				result.append("  None")
		
		# Resource Availability
		result.append("\nResource Availability:")
		if self.resource_availability:
				for name, resource in self.resource_availability.items():
						result.append(str(resource))
		else:
				result.append("  None")
		
		return "\n".join(result)