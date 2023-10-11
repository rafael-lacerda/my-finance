from typing import Optional

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from my_finance import templates
from my_finance.services.transaction_service import TransactionService
from my_finance.utils.auth import get_email_for_page
from my_finance.utils.exceptions import UnauthorizedPageException

router = APIRouter()


@router.get(path="/main", summary="Gets the main page", tags=["Pages", "Main"], response_class=HTMLResponse)
async def get_main(request: Request, email: str = Depends(get_email_for_page)):
    transaction_service = TransactionService()
    _, summary = await transaction_service.get_transactions_by_user_email(email=email)
    context = {"request": request, "email": email, **summary}
    return templates.TemplateResponse("main.html", context)
