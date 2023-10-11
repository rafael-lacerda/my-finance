from my_finance.database.services.users import UserDBService


def include_demo_user():
    user_db_service = UserDBService()

    user_db_service.create_user(
        name="Demo User",
        email="demo@example.com",
        password="demo123"
    )
