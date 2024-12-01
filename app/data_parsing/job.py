class Job:
    """
    Represents a job and its precedence relationships.

    Attributes:
        job_number (int): The unique identifier for the job.
        successors (list[int]): A list of job numbers that must follow this job.
    """
    def __init__(self, job_number, successors):
        self.job_number = job_number
        self.successors = successors
