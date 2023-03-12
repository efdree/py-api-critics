from models.model import GamePlatformModel
from schemas.gameplatform import GamePlatform


class GamePlatformService():

    def __init__(self, db) -> None:
        self.db = db

    def getGamesPlatforms(self):
        result = self.db.query(GamePlatformModel).all()
        return result

    def getGamePlatform(self, id: int):
        result = self.db.query(GamePlatformModel).filter(
            GamePlatformModel.id == id).first()
        return result

    def createGamePlatform(self, gameplatform: GamePlatform):
        new_gameplatform = GamePlatformModel(**gameplatform.dict())
        self.db.add(gameplatform)
        self.db.commit()
        return

    def updateGamePlatform(self, id: int, data: GamePlatform):
        gameplatform = self.db.query(GamePlatformModel).filter(
            GamePlatformModel.id == id).first()
        gameplatform.game_id = data.game_id
        gameplatform.platform_id = data.platform_id
        self.db.commit()
        return

    def deleteGamePlatform(self, id: int):
        self.db.query(GamePlatformModel).filter(
            GamePlatformModel.id == id).delete()
        self.db.commit()
        return
