from datetime import datetime
from fastapi import Request
from my_finance.database.models import TransactionType
from my_finance.database.services.transactions import TransactionDBService
from my_finance.database.services.users import UserDBService


class TransactionService:
    def __init__(self) -> None:
        self.transaction_db_service = TransactionDBService()
        self.user_db_service = UserDBService()

    async def create_transaction(
        self,
        email: str,
        date: str,
        amount: str,
        description: str,
        type: TransactionType
        ):
        user = self.user_db_service.get_user_by_email(email)
        date = datetime.strptime(date, "%Y-%m-%d")

        self.transaction_db_service.create_transaction(
            amount=amount,
            date=date,
            description=description,
            type=type,
            user_id=user.id,
        )

    async def get_transactions_by_user_email(self, email: str):
        user = self.user_db_service.get_user_by_email(email)
        transactions = self.transaction_db_service.get_transactions_by_user_id(
            user_id=user.id
        )
        transactions_json = []
        summary = {
            "total_income": 0,
            "total_expense": 0,
            "balance": 0,
            "balance_sign": "positive",
        }
        for transaction in transactions:
            transactions_json.append(
                {
                    "amount": transaction.amount,
                    "date": transaction.date.strftime("%d/%m/%Y"),
                    "description": transaction.description,
                    "type": transaction.type.value,
                    "id": transaction.id,
                }
            )
            if transaction.type == TransactionType.INCOME:
                summary["total_income"] += transaction.amount
            else:
                summary["total_expense"] += transaction.amount

        summary["balance"] = summary["total_income"] - summary["total_expense"]
        if summary["balance"] < 0:
            summary["balance"] = abs(summary["balance"])
            summary["balance_sign"] = "negative"
        return transactions_json, summary

    async def delete_transaction_by_id(self, transaction_id: int):
        self.transaction_db_service.delete_transaction(transaction_id)
