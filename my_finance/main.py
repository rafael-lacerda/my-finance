from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from my_finance.routers import expense, income, login, main, root, transactions
from my_finance.database import include_demo_user
app = FastAPI()

app.include_router(expense.router)
app.include_router(income.router)
app.include_router(login.router)
app.include_router(main.router)
app.include_router(root.router)
app.include_router(transactions.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

try:
    include_demo_user()
except:
    pass
