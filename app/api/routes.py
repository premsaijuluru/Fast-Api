from fastapi import APIRouter, HTTPException, Header
from app.core.security import create_token, verify_token
from app.services.scraper import fetch_market_data
from app.services.ai_service import analyze
from app.services.report_generator import format_report
from app.utils.session import track_user
from fastapi import Request

router = APIRouter()


# 🔐 LOGIN ROUTE
@router.post("/login")
def login(username: str):
    if not username:
        raise HTTPException(status_code=400, detail="Username required")

    token = create_token(username)
    return {"access_token": token}


# 🚀 ANALYZE ROUTE


@router.get("/analyze/{sector}")
def analyze_sector(sector: str, request: Request):

    # ✅ Get header manually (no Swagger issues)
    authorization = request.headers.get("authorization")

    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    # ✅ Remove Bearer
    if authorization.startswith("Bearer "):
        token = authorization.replace("Bearer ", "")
    else:
        token = authorization

    # ✅ Verify token
    user = verify_token(token)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")

    track_user(user)

    data = fetch_market_data(sector)
    ai_output = analyze(sector, data)
    report = format_report(sector, ai_output)

    return {
        "user": user,
        "sector": sector,
        "report": report
    }
