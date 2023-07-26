from typing import Optional

from fastapi import APIRouter, Depends, Request
from fastapi.responses import FileResponse, RedirectResponse

from my_finance.utils.auth import AuthCookie, get_auth_cookie

router = APIRouter()


@router.get(path="/", summary="Redirects to the login or main pages", tags=["Pages"])
async def read_root(cookie: Optional[AuthCookie] = Depends(get_auth_cookie)):
    path = "/main" if cookie else "/login"
    return RedirectResponse(path, status_code=302)


@router.get(path="/favicon.ico", include_in_schema=False)
async def get_favicon():
    return FileResponse("static/img/favicon.ico")
