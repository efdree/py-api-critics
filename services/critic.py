from models.model import CriticModel
from schemas.critic import Critic


class CriticService():

    def __init__(self, db) -> None:
        self.db = db

    def getCritics(self):
        result = self.db.query(CriticModel).all()
        return result

    def getCritic(self, id: int):
        result = self.db.query(CriticModel).filter(
            CriticModel.id == id).first()
        return result

    def getCriticsByGame(self, game_id: int):
        result = self.db.query(CriticModel).filter(
            CriticModel.game_id == game_id).all()
        return result

    def getCriticsByCompany(self, company_id: int):
        result = self.db.query(CriticModel).filter(
            CriticModel.company_id == company_id).all()
        return result

    def createCritic(self, critic: Critic):
        new_critic = CriticModel(**critic.dict())
        self.db.add(new_critic)
        self.db.commit()
        return

    def updateCritic(self, id: int, data: Critic):
        critic = self.db.query(CriticModel).filter(
            CriticModel.id == id).first()
        critic.title = data.title
        critic.body = data.body
        critic.user_id = data.user_id
        critic.company_id = data.company_id
        critic.game_id = data.game_id
        self.db.commit()
        return

    def deleteCritic(self, id: int):
        self.db.query(CriticModel).filter(
            CriticModel.id == id).delete()
        self.db.commit()
        return
