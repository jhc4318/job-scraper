from typing import Optional, List

class Job:
    def __init__(self, title: str, metadata: str, salary: Optional[int] = None):
        self.title = title
        self.metadata = metadata
        self.salary = salary

    def __repr__(self):
        return f"{self.title} - {self.salary}"

class Company:
    def __init__(self, name: str):
        self.name = name
        self.jobs: List[Job] = []

    def add_job(self, job: Job):
        self.jobs.append(job)

    def __repr__(self) -> str:
        return f"{self.name}: {self.jobs}"
