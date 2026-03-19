import os
import httpx
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

async def analyze_with_ai(sector: str, data: str) -> str:
    """
    Analyze sector data using Gemini AI API with mock fallback.
    
    Args:
        sector: The sector name to analyze
        data: The data/news content about the sector
        
    Returns:
        str: Formatted analysis result with market insights
    """
    if not GEMINI_API_KEY:
        return get_mock_analysis(sector)

    # Create comprehensive prompt for AI
    prompt = f"""
You are a financial analyst specializing in Indian market trends.

Analyze the {sector} sector in India based on the data below:

{data}

Provide a comprehensive analysis in this exact format:

## Market Overview
[Provide 2-3 sentences about the current state of the {sector} sector]

## Key Trends
[List 3-4 key trends currently affecting the sector]

## Trade Opportunities
[Identify 3-4 promising investment or trading opportunities]

## Risks
[Identify 2-3 main risks investors should be aware of]

## Recommendations
[Provide actionable recommendations for traders/investors]
"""

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(url, json=payload)

            # Check HTTP error
            if response.status_code != 200:
                # Fallback to mock response on API failure
                return get_mock_analysis(sector)

            result = response.json()

            # Safe extraction from API response
            candidates = result.get("candidates", [])
            if not candidates:
                return get_mock_analysis(sector)

            content = candidates[0].get("content", {})
            parts = content.get("parts", [])

            if not parts:
                return get_mock_analysis(sector)

            analysis_text = parts[0].get("text", "").strip()
            
            if not analysis_text:
                return get_mock_analysis(sector)

            return analysis_text

    except (httpx.TimeoutException, Exception):
        # Fallback to mock response on any error
        return get_mock_analysis(sector)


def get_mock_analysis(sector: str) -> str:
    """
    Return mock analysis for demonstration and reliability.
    
    Args:
        sector: The sector to analyze
        
    Returns:
        str: Formatted mock analysis
    """
    mock_analysis = f"""## Market Overview
The {sector.capitalize()} sector in India is experiencing robust growth with increasing investments from both domestic and international players. Government initiatives and policy support have created favorable conditions for businesses and startups to thrive in this dynamic market.

## Key Trends
- Digital transformation and adoption of advanced technologies across the {sector} sector
- Increasing focus on sustainability and ESG compliance by major corporations
- Rising participation of startups and innovation hubs in the {sector} ecosystem
- Growing demand for skilled talent and competitive advantage through talent acquisition
- Expansion of operations in tier-2 and tier-3 cities to tap emerging markets

## Trade Opportunities
- Investment opportunities in emerging {sector} companies with strong growth potential
- Joint ventures and partnerships between Indian and global {sector} players
- Supply chain diversification creating opportunities for logistics and support services
- Technology-driven solutions addressing pain points in the traditional {sector} business models
- Export growth potential for {sector} products and services in Asian and global markets

## Risks
- Market volatility due to global economic uncertainties and geopolitical factors
- Regulatory changes that could impact {sector} operations and profitability
- Intense competition from both established players and new market entrants
- Talent shortage and rising operational costs impacting margins

## Recommendations
1. Diversify investments across established and emerging {sector} companies to balance risk and growth
2. Monitor regulatory developments and adapt business strategies accordingly
3. Leverage technology and digital platforms to improve efficiency and customer reach
4. Build strategic partnerships to enhance market presence and competitive advantage
5. Focus on sustainable growth practices to align with long-term market trends"""

    return mock_analysis