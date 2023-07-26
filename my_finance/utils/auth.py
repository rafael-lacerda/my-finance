import secrets
from typing import Optional

import jwt
from fastapi import Cookie, Depends, Form
from fastapi.security import HTTPBasic
from pydantic import BaseModel

from my_finance.utils.exceptions import UnauthorizedException, UnauthorizedPageException
from my_finance.utils.settings import Settings

basic_auth = HTTPBasic(auto_error=False)
auth_cookie_name = "my_finance_session"
settings = Settings()


class AuthCookie(BaseModel):
    name: str
    token: str
    username: str


def serialize_token(username: str) -> str:
    return jwt.encode({"username": username}, settings.SECRET_KEY, algorithm="HS256")


def deserialize_token(token: str) -> str:
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return data["username"]
    except Exception:
        return None


def get_login_form_creds(username: str = Form(), password: str = Form()) -> Optional[AuthCookie]:
    cookie = None

    if username in settings.USERS:
        if secrets.compare_digest(password, settings.USERS[username]):
            token = serialize_token(username)
            cookie = AuthCookie(name=auth_cookie_name, username=username, token=token)

    return cookie


def get_auth_cookie(
    my_finance_session: Optional[str] = Cookie(default=None),
) -> Optional[AuthCookie]:
    cookie = None

    if my_finance_session:
        username = deserialize_token(my_finance_session)
        if username in settings.USERS:
            cookie = AuthCookie(name=auth_cookie_name, username=username, token=my_finance_session)

    return cookie


def get_username_for_api(cookie: Optional[AuthCookie] = Depends(get_auth_cookie)) -> str:
    if not cookie:
        raise UnauthorizedException()

    return cookie.username


def get_username_for_page(cookie: Optional[AuthCookie] = Depends(get_auth_cookie)) -> str:
    if not cookie:
        raise UnauthorizedPageException()

    return cookie.username
