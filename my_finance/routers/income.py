from typing import Optional

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from my_finance import templates
from my_finance.database.models import TransactionType
from my_finance.services.transaction_service import TransactionService
from my_finance.utils.auth import get_email_for_page
from my_finance.utils.exceptions import UnauthorizedPageException

router = APIRouter()


@router.get(path="/income", summary="Gets the income page", tags=["Pages", "Income"], response_class=HTMLResponse)
async def get_income(request: Request, email: str = Depends(get_email_for_page)):
    context = {"request": request, "email": email}
    return templates.TemplateResponse("income.html", context)


@router.post(path="/income", summary="Posts the income", tags=["Pages", "Income"])
async def post_income(
    request: Request,
    email: str = Depends(get_email_for_page),
    date: str = Form(...),
    amount: float = Form(...),
    description: str = Form(...),
) -> dict:
    transaction_service = TransactionService()
    await transaction_service.create_transaction(
        email=email,
        date=date,
        amount=amount,
        description=description,
        type=TransactionType.INCOME
    )
    return RedirectResponse("/main", status_code=302)
