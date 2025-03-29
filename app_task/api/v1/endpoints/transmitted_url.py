import pyshorteners
from fastapi import APIRouter, status
from api.v1.schemas.url_schema import answers, UrlModel
from core.config import service_setting

trans_url_router = APIRouter()


@trans_url_router.post(
    "/",
    summary="URL shortening method",
    description=
    """
    ## Shortens a given URL using the Bitly service.
    
    
    Note:
        Requires a valid Bitly API token configured in the service settings.
    
    Parameters:
    - url (str): The original URL to be shortened.
    
    Returns:
    - A JSON response containing the shortened URL and HTTP status 201 (Created).
    
    Example Request:
    POST /trans-url/
    {
        "url": "https://example.com/very/long/url"
    }
    
    Example Response:
    {
        "status": 201,
        "url": "https://bit.ly/3abc123"
    }
    
    Exceptions:
    - May raise a pyshorteners library exception if URL shortening fails.
    - An invalid or unreachable URL may cause an error.
    """
)
async def post_trans_url(
    url: UrlModel
):
    """
    The method accepts the URL string for shortening in the request body.


     :return
        url (str)
            shortened url
    """
    object = pyshorteners.Shortener(api_key=service_setting.token)
    link = object.bitly.short(url.url)
    return answers(
        code_status=status.HTTP_201_CREATED,
        url_text=link
    )


@trans_url_router.get(
    "/",
    summary="URL shortening method",
    description=
    """
    ## Expands a shortened Bitly URL to its original long URL.
    
    
    This endpoint accepts a Bitly shortened URL and returns the original long URL
    by calling Bitly's expand API. The response uses HTTP 307 (Temporary Redirect)
    status code to indicate the original destination.
    
    Note:
        Requires a valid Bitly API token configured in the service settings.
    
    Args:
        url (str): The Bitly shortened URL (e.g., "https://bit.ly/abc123")
    
    Returns:
        JSONResponse: A response object containing:
            - code_status (int): HTTP 307 (Temporary Redirect)
            - url_text (str): The original expanded URL
    
    Example:
        >>> GET /trans-url/?url=https://bit.ly/abc123
    
        Response:
        {
            "status": 307,
            "url": "https://original.example.com/long/path"
        }
    """
)
async def get_trans_url(
    url: str
):
    object = pyshorteners.Shortener(api_key=service_setting.token)
    link = object.bitly.expand(url)
    return answers(
        code_status=status.HTTP_307_TEMPORARY_REDIRECT,
        url_text=link
    )
