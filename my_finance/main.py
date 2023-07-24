"""
This module is the main module for the FastAPI app.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

#from app.utils.exceptions import UnauthorizedPageException
from my_finance.routers import login, root

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


# --------------------------------------------------------------------------------
# App Creation
# --------------------------------------------------------------------------------

app = FastAPI()
app.include_router(root.router)
app.include_router(login.router)


# --------------------------------------------------------------------------------
# Static Files
# --------------------------------------------------------------------------------

app.mount("/static", StaticFiles(directory="static"), name="static")
