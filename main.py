API_KEY = "123456"
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.data_service import fetch_sector_news
from services.ai_service import analyze_with_ai
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi import Query
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Trade Opportunities API")
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded. Try again later."},
    )

# Response model
class AnalysisResponse(BaseModel):
    sector: str
    analysis: str


@app.get("/")
def home():
    return {"message": "Trade Opportunities API is running."}


@app.get("/analyze/{sector}", response_model=AnalysisResponse)
@limiter.limit("5/minute")
async def analyze_sector(request: Request, sector: str, api_key: str = Query(..., description="Enter your API Key")):
    # ✅ API key validation
    if api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    try:
        # ✅ Input validation
        sector = sector.strip().lower()

        if not sector.isalpha():
            raise HTTPException(
                status_code=400,
                detail="Sector must contain only alphabets (e.g., technology)"
            )

        # ✅ Fetch sector data
        data = await fetch_sector_news(sector)

        if not data:
            raise HTTPException(
                status_code=500,
                detail="Failed to fetch sector data"
            )

        # ✅ AI analysis
        analysis = await analyze_with_ai(sector, data)
        # ✅ Save as markdown file
        filename = f"{sector}_analysis.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {sector.capitalize()} Sector Analysis\n\n")
            f.write(analysis)
        if not analysis:
            raise HTTPException(
                status_code=500,
                detail="AI analysis failed"
            )

        # ✅ FINAL CLEAN RESPONSE (only once)
        return {
            "sector": sector,
            "analysis": analysis
        }

    except HTTPException as http_err:
        raise http_err

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )


        

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)