# Trade Opportunities API

## Features
- FastAPI backend
- JWT Authentication
- Rate Limiting
- Session Tracking
- Gemini AI Integration
- Real-time Market Data
- Markdown Reports

## Run
pip install -r requirements.txt
uvicorn app.main:app --reload

## Endpoints

### Login
POST /login

### Analyze
GET /analyze/{sector}

Header:
Authorization: <token>