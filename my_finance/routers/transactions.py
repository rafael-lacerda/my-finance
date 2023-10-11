from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
import starlette.status as status

from my_finance import templates
from my_finance.services.transaction_service import TransactionService
from my_finance.utils.auth import get_email_for_page

router = APIRouter()


@router.get(path="/transactions", summary="Gets the transactions page", tags=["Pages", "Transaction"], response_class=HTMLResponse)
async def get_income(request: Request, email: str = Depends(get_email_for_page)):
    transaction_service = TransactionService()
    transactions, summary = await transaction_service.get_transactions_by_user_email(email=email)
    context = {
        "request": request,
        "email": email,
        "transactions": transactions,
        **summary
    }
    return templates.TemplateResponse("transactions.html", context)


@router.post("/transactions/{transaction_id}/remove")
async def remove_transaction(transaction_id: int, email: str = Depends(get_email_for_page)):
    transaction_service = TransactionService()
    await transaction_service.delete_transaction_by_id(transaction_id=transaction_id)
    return RedirectResponse(url="/transactions", status_code=status.HTTP_302_FOUND)
