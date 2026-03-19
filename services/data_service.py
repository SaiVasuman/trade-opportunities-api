import httpx

async def fetch_sector_news(sector: str) -> str:
    """
    Fetch news data for a specific sector.
    
    Args:
        sector: The sector name to search for
        
    Returns:
        str: News data about the sector (limited to 1000 characters)
    """
    query = f"{sector} sector India news latest"

    url = f"https://duckduckgo.com/?q={query}&format=json"

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            
            if response.status_code == 200:
                data = response.text

                # Return limited data to keep response size reasonable
                return data[:1000] if data else "No data found"
            else:
                return f"Error: Failed to fetch news (Status {response.status_code})"

    except httpx.TimeoutException:
        return "Error: News fetch request timed out"
    except Exception as e:
        return f"Error: Failed to fetch data - {str(e)}"