# Trade Opportunities API

## Overview
This is a backend API built using FastAPI that provides market analysis for different sectors in India.

## Features
- Analyze sectors like technology, pharma, agriculture
- Uses AI (Gemini API) for insights
- Fetches latest market/news data
- Generates structured analysis
- Saves output as markdown file
- API key authentication
- Rate limiting

## Project Structure
trade_api/
│── main.py
│── services/
│   ├── ai_service.py
│   ├── data_service.py
│── README.md

## How to Run the Project

### Step 1: Open terminal
Go to project folder:
cd C:\trade_api

### Step 2: Activate virtual environment
venv\Scripts\activate

### Step 3: Install dependencies
pip install fastapi uvicorn httpx python-dotenv slowapi

### Step 4: Run server
uvicorn main:app --reload

### Step 5: Open in browser
http://127.0.0.1:8000/docs

## API Endpoint

GET /analyze/{sector}

Example:
/analyze/technology?api_key=123456

## Output
- Returns analysis in JSON format
- Saves a .md file in project folder

## Security
- API Key required
- Rate limit: 5 requests per minute

## Author
C Sai Vasuman# Trade Opportunities API

## Overview
This is a backend API built using FastAPI that provides market analysis for different sectors in India.

## Features
- Analyze sectors like technology, pharma, agriculture
- Uses AI (Gemini API) for insights
- Fetches latest market/news data
- Generates structured analysis
- Saves output as markdown file
- API key authentication
- Rate limiting

## Project Structure
trade_api/
│── main.py
│── services/
│   ├── ai_service.py
│   ├── data_service.py
│── README.md

## How to Run the Project

### Step 1: Open terminal
Go to project folder:
cd C:\trade_api

### Step 2: Activate virtual environment
venv\Scripts\activate

### Step 3: Install dependencies
pip install fastapi uvicorn httpx python-dotenv slowapi

### Step 4: Run server
uvicorn main:app --reload

### Step 5: Open in browser
http://127.0.0.1:8000/docs

## API Endpoint

GET /analyze/{sector}

Example:
/analyze/technology?api_key=123456

## Output
- Returns analysis in JSON format
- Saves a .md file in project folder

## Security
- API Key required
- Rate limit: 5 requests per minute

## Author
Sai Vasuman
