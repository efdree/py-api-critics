from models.model import GameGenreModel
from schemas.gamegenre import GameGenre


class GameGenreService():

    def __init__(self, db) -> None:
        self.db = db

    def get_gamesgenres(self):
        result = self.db.query(GameGenreModel).all()
        return result

    def get_gamegenre(self, id: int):
        result = self.db.query(GameGenreModel).filter(
            GameGenreModel.id == id).first()
        return result

    def create_gamegenre(self, gamegenre: GameGenre):
        new_gamegenre = GameGenreModel(**gamegenre.dict())
        self.db.add(new_gamegenre)
        self.db.commit()
        return

    def update_gamegenre(self, id: int, data: GameGenre):
        gamegenre = self.db.query(GameGenreModel).filter(
            GameGenreModel.id == id).first()
        gamegenre.game_id = data.game_id
        gamegenre.genre_id = data.genre_id
        self.db.commit()
        return

    def delete_gamegenre(self, id: int):
        self.db.query(GameGenreModel).filter(
            GameGenreModel.id == id).delete()
        self.db.commit()
        return
