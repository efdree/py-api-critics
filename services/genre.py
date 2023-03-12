from models.model import GenreModel
from schemas.genre import Genre


class GenreService():

    def __init__(self, db) -> None:
        self.db = db

    def getGenres(self):
        result = self.db.query(GenreModel).all()
        return result

    def getGenre(self, id: int):
        result = self.db.query(GenreModel).filter(
            GenreModel.id == id).first()
        return result

    def createGenre(self, genre: Genre):
        new_genre = GenreModel(**genre.dict())
        self.db.add(new_genre)
        self.db.commit()
        return

    def updateGenre(self, id: int, data: Genre):
        genre = self.db.query(GenreModel).filter(
            GenreModel.id == id).first()
        genre.name = data.name
        genre.genregame_id = data.genregame_id
        self.db.commit()
        return

    def deleteGenre(self, id: int):
        self.db.query(GenreModel).filter(
            GenreModel.id == id).delete()
        self.db.commit()
        return
