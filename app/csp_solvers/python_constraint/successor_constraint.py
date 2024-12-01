def successor_constraint(start_job: int, start_successor: int, duration: int):
    """
    Ensures that a job finishes before its successor starts.

    This constraint ensures that the start time of a successor job is after the completion
    time of the current job, considering the duration of the current job.

    Args:
        start_job (int): The start time of the current job.
        start_successor (int): The start time of the successor job.
        duration (int): The duration of the current job.

    Returns:
        bool: True if the current job finishes before the successor starts, False otherwise.
    """

    return start_job + duration <= start_successor
