from models.model import GameModel, InvolvedCompanyModel
from schemas.game import Game


class GameService():

    def __init__(self, db) -> None:
        self.db = db

    def getGames(self):
        result = self.db.query(GameModel).all()
        return result

    def getGame(self, id: int):
        result = self.db.query(GameModel).filter(
            GameModel.id == id).first()
        return result

    def getGamesByCompany(self, company_id: int):
        result = self.db.query(InvolvedCompanyModel).filter(
            InvolvedCompanyModel.company_id == company_id).all()
        return result

    def createGame(self, game: Game):
        new_game = GameModel(**game.dict())
        self.db.add(new_game)
        self.db.commit()
        return

    def updateGame(self, id: int, data: Game):
        game = self.db.query(GameModel).filter(
            GameModel.id == id).first()
        game.name = data.name
        game.summary = data.summary
        game.release_date = data.release_date
        game.category = data.category
        game.rating = data.rating
        game.cover = data.cover
        game.parent_id = data.parent_id
        game.gameplatform_id = data.gameplatform_id
        game.gamegenre_id = data.gamegenre_id
        self.db.commit()
        return

    def deleteGame(self, id: int):
        self.db.query(GameModel).filter(
            GameModel.id == id).delete()
        self.db.commit()
        return
