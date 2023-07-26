from typing import Optional

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from my_finance import templates
from my_finance.utils.auth import get_username_for_page
from my_finance.utils.exceptions import UnauthorizedPageException

router = APIRouter()


@router.get(path="/main", summary="Gets the main page", tags=["Pages", "Main"], response_class=HTMLResponse)
async def get_main(request: Request, username: str = Depends(get_username_for_page)):
    context = {"request": request, "username": username}
    return templates.TemplateResponse("main.html", context)
