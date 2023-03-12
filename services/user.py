from models.model import UserModel
from schemas.user import User


class UserService():

    def __init__(self, db) -> None:
        self.db = db

    def getUsers(self):
        result = self.db.query(UserModel).all()
        return result

    def getUser(self, id: int):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result

    def createUser(self, user: User):
        new_user = UserModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        return

    def updateUser(self, id: int, data: User):
        user = self.db.query(UserModel).filter(UserModel.id == id).first()
        user.username = data.username
        user.email = data.email
        user.password = data.password
        user.role = data.role
        user.critics_count = data.critics_count
        self.db.commit()
        return

    def deleteUser(self, id: int):
        self.db.query(UserModel).filter(UserModel.id == id).delete()
        self.db.commit()
        return
