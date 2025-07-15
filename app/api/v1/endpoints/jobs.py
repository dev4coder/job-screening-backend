from fastapi import APIRouter, HTTPException, status
from typing import Sequence
from schemas.jobs import Job, JobCreateSchema
from services.jobs_service import create_job, get_job, get_jobs

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.post("/", response_model=Job, status_code=status.HTTP_201_CREATED)
async def create_new_job(job: JobCreateSchema):
    try:
        return create_job(job)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/{job_id}", response_model=Job)
async def read_job(job_id: int):
    try:
        return get_job(job_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
@router.get("/", response_model=Sequence[Job])
async def read_jobs():
    return get_jobs()