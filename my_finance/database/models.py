import enum
from sqlalchemy import Column, Date, Float, ForeignKey, String, Integer, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from bcrypt import hashpw, gensalt


Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True)
    password_hash = Column(String(255), nullable=False)

    def set_password(self, password):
        # Hash the password before saving it
        self.password_hash = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

    def check_password(self, password):
        # Check if the provided password matches the stored hash
        return hashpw(password.encode('utf-8'), self.password_hash.encode('utf-8')) == self.password_hash.encode('utf-8')

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"


class TransactionType(enum.Enum):
    INCOME = 'Income'
    EXPENSE = 'Expense'


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String(255), nullable=False)
    type = Column(Enum(TransactionType), nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', lazy='select')
