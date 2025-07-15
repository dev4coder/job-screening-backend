from typing import Sequence
from schemas.jobs import Job, JobCreateSchema
from supabase_client import get_client

_table = "jobs"

def create_job(job: JobCreateSchema) -> Job:
    client = get_client()
    response = client.table(_table).insert(job.model_dump()).execute()
    if not response.data:
        raise ValueError("Failed to create job")
    return Job(**response.data[0])

def get_job(job_id: int) -> Job:
    client = get_client()
    response = client.table(_table).select("*").eq("id", job_id).execute()
    if not response.data:
        raise ValueError(f"Job with id {job_id} not found")
    return Job(**response.data[0])

def get_jobs() -> Sequence[Job]:
    client = get_client()
    response = client.table(_table).select("*").execute()
    if not response.data:
        return []
    return [Job(**item) for item in response.data]