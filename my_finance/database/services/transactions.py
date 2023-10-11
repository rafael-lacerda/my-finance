from sqlalchemy import asc
from my_finance.database.models import Transaction
from my_finance.database.session import Session


class TransactionDBService:
    def create_transaction(self, amount, date, description, type, user_id):
        with Session() as session:
            new_transaction = Transaction(
                amount=amount,
                date=date,
                description=description,
                type=type,
                user_id=user_id
            )
            session.add(new_transaction)
            session.commit()
            return new_transaction

    def get_transaction_by_id(self, transaction_id):
        with Session() as session:
            return session.query(Transaction).filter_by(id=transaction_id).first()

    def get_transactions_by_user_id(self, user_id):
        with Session() as session:
            return session.query(Transaction).filter_by(user_id=user_id).order_by(asc(Transaction.date)).all()

    def update_transaction(self, transaction_id, amount=None, date=None, description=None, type=None):
        with Session() as session:
            transaction = self.get_transaction_by_id(transaction_id)
            if transaction:
                if amount is not None:
                    transaction.amount = amount
                if date is not None:
                    transaction.date = date
                if description is not None:
                    transaction.description = description
                if type is not None:
                    transaction.type = type
                session.commit()
                return transaction
            return None

    def delete_transaction(self, transaction_id):
        with Session() as session:
            transaction = self.get_transaction_by_id(transaction_id)
            if transaction:
                session.delete(transaction)
                session.commit()
                return True
            return False
