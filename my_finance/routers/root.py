"""
This module provides routes for authentication.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

from my_finance import templates
from my_finance.utils.auth import AuthCookie, get_auth_cookie

from fastapi import APIRouter, Depends, Request
from fastapi.responses import FileResponse, RedirectResponse
from typing import Optional


# --------------------------------------------------------------------------------
# Router
# --------------------------------------------------------------------------------

router = APIRouter()


# --------------------------------------------------------------------------------
# Routes
# --------------------------------------------------------------------------------

@router.get(
  path="/",
  summary="Redirects to the login or reminders pages",
  tags=["Pages"]
)
async def read_root(
  cookie: Optional[AuthCookie] = Depends(get_auth_cookie)
):
  path = '/login'
  return RedirectResponse(path, status_code=302)


@router.get(
  path="/favicon.ico",
  include_in_schema=False
)
async def get_favicon():
  return FileResponse("static/img/favicon.ico")
