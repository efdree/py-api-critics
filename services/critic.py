from models.model import CriticModel
from schemas.critic import Critic


class GameService():

    def __init__(self, db) -> None:
        self.db = db

    def get_critics(self):
        result = self.db.query(CriticModel).all()
        return result

    def get_critic(self, id: int):
        result = self.db.query(CriticModel).filter(
            CriticModel.id == id).first()
        return result

    def create_critic(self, critic: Critic):
        new_critic = CriticModel(**critic.dict())
        self.db.add(new_critic)
        self.db.commit()
        return

    def update_critic(self, id: int, data: Critic):
        critic = self.db.query(CriticModel).filter(
            CriticModel.id == id).first()
        critic.title = data.title
        critic.body = data.body
        critic.user_id = data.user_id
        critic.company_id = data.company_id
        critic.game_id = data.game_id
        self.db.commit()
        return

    def delete_critic(self, id: int):
        self.db.query(CriticModel).filter(
            CriticModel.id == id).delete()
        self.db.commit()
        return
