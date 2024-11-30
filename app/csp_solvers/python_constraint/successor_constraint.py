def successor_constraint(start_job: int, start_successor: int, duration: int):
    return start_job + duration <= start_successor
