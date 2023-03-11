from models.model import GameModel
from schemas.game import Game


class GameService():

    def __init__(self, db) -> None:
        self.db = db

    def get_games(self):
        result = self.db.query(GameModel).all()
        return result

    def get_game(self, id: int):
        result = self.db.query(GameModel).filter(
            GameModel.id == id).first()
        return result

    def create_game(self, game: Game):
        new_game = GameModel(**game.dict())
        self.db.add(new_game)
        self.db.commit()
        return

    def update_game(self, id: int, data: Game):
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

    def delete_game(self, id: int):
        self.db.query(GameModel).filter(
            GameModel.id == id).delete()
        self.db.commit()
        return
