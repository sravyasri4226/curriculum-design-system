from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from ai_engine import generate_curriculum

# Load environment variables
load_dotenv()

app = FastAPI(title="CurricuForge API")

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class CurriculumRequest(BaseModel):
    topic: str
    level: str  # beginner, intermediate, advanced
    duration_weeks: int
    learning_style: str  # visual, auditory, kinesthetic, reading

# Response model
class CurriculumResponse(BaseModel):
    curriculum: str
    status: str

@app.get("/")
async def root():
    """Root endpoint - API is running"""
    return {"message": "CurricuForge API is running"}

@app.post("/generate-curriculum")
async def generate(request: CurriculumRequest):
    """Generate a personalized curriculum based on input parameters"""
    try:
        curriculum = generate_curriculum(
            topic=request.topic,
            level=request.level,
            duration_weeks=request.duration_weeks,
            learning_style=request.learning_style
        )
        return CurriculumResponse(curriculum=curriculum, status="success")
    except Exception as e:
        return CurriculumResponse(curriculum="", status=f"error: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "CurricuForge API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
