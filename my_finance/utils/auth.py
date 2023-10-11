import secrets
from typing import Optional

import jwt
from fastapi import Cookie, Depends, Form
from fastapi.security import HTTPBasic
from pydantic import BaseModel

from my_finance.database.services.users import UserDBService

from my_finance.utils.exceptions import UnauthorizedException, UnauthorizedPageException
from my_finance.utils.settings import Settings

basic_auth = HTTPBasic(auto_error=False)
auth_cookie_name = "my_finance_session"
settings = Settings()


class AuthCookie(BaseModel):
    name: str
    token: str
    email: str


def serialize_token(email: str) -> str:
    return jwt.encode({"email": email}, settings.SECRET_KEY, algorithm="HS256")


def deserialize_token(token: str) -> str:
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return data["email"]
    except Exception:
        return None


def get_login_form_creds(email: str = Form(), password: str = Form()) -> Optional[AuthCookie]:
    user_db_service = UserDBService()
    cookie = None
    if user:= user_db_service.get_user_by_email(email=email):
        if user.check_password(password):
            token = serialize_token(email)
            cookie = AuthCookie(name=auth_cookie_name, email=email, token=token)

    return cookie


def get_auth_cookie(
    my_finance_session: Optional[str] = Cookie(default=None),
) -> Optional[AuthCookie]:
    cookie = None
    user_db_service = UserDBService()
    if my_finance_session:
        email = deserialize_token(my_finance_session)
        if user:= user_db_service.get_user_by_email(email=email):
            cookie = AuthCookie(name=auth_cookie_name, email=email, token=my_finance_session)

    return cookie


def get_email_for_api(cookie: Optional[AuthCookie] = Depends(get_auth_cookie)) -> str:
    if not cookie:
        raise UnauthorizedException()

    return cookie.email


def get_email_for_page(cookie: Optional[AuthCookie] = Depends(get_auth_cookie)) -> str:
    if not cookie:
        raise UnauthorizedPageException()

    return cookie.email
