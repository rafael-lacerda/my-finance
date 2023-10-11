from my_finance.database.models import User
from my_finance.database.session import Session


class UserDBService:
    def create_user(self, name, email, password):
        with Session() as session:
            new_user = User(name=name, email=email)
            new_user.set_password(password)
            session.add(new_user)
            session.commit()
            return new_user

    def get_user_by_id(self, user_id):
        with Session() as session:
            return session.query(User).filter_by(id=user_id).first()

    def get_user_by_email(self, email):
        with Session() as session:
            return session.query(User).filter_by(email=email).first()

    def update_user(self, user_id, name=None, email=None, password=None):
        with Session() as session:
            user = self.get_user_by_id(user_id)
            if user:
                if name is not None:
                    user.name = name
                if email is not None:
                    user.email = email
                if password is not None:
                    user.set_password(password)
                session.commit()
                return user
            return None

    def delete_user(self, user_id):
        with Session() as session:
            user = self.get_user_by_id(user_id)
            if user:
                session.delete(user)
                session.commit()
                return True
            return False
