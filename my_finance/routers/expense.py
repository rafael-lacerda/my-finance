from typing import Optional

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from my_finance import templates
from my_finance.database.models import TransactionType
from my_finance.services.transaction_service import TransactionService
from my_finance.utils.auth import get_email_for_page
from my_finance.utils.exceptions import UnauthorizedPageException

router = APIRouter()


@router.get(path="/expense", summary="Gets the expense page", tags=["Pages", "Expense"], response_class=HTMLResponse)
async def get_expense(request: Request, email: str = Depends(get_email_for_page)):
    context = {"request": request, "email": email}
    return templates.TemplateResponse("expense.html", context)


@router.post(path="/expense", summary="Posts the expense", tags=["Pages", "Expense"])
async def post_expense(
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
        type=TransactionType.EXPENSE
    )
    return RedirectResponse("/main", status_code=302)
