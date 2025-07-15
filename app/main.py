from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.endpoints.jobs import router as jobs_router

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Include the jobs router
app.include_router(jobs_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# To run the application, use the command:
# uvicorn main:app --reload
