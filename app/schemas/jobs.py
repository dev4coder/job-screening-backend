from pydantic import BaseModel, Field
from typing import Optional, List

class JobSchema(BaseModel):
    title: str = Field(..., description="Title of the job")
    description: str = Field(..., description="Description of the job")
    company: str = Field(..., description="Company offering the job")
    location: Optional[str] = Field(default=None, description="Location of the job")
    type: Optional[str] = Field(default=None, description="Type of the job (e.g., Full-time, Part-time)")
    salary: Optional[str] = Field(default=None, description="Salary for the job")
    requirements: List[str] = Field(default_factory=list, description="List of job requirements")

class JobCreateSchema(JobSchema):
    pass

class Job(JobSchema):
    id: int = Field(..., description="Unique identifier for the job")
    created_at: Optional[str] = Field(default=None, description="Creation timestamp of the job")
    updated_at: Optional[str] = Field(default=None, description="Last update timestamp of the job")   

    class Config:
        from_attributes = True