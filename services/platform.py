from models.model import PlatformModel
from schemas.platform import Platform


class PlatformService():

    def __init__(self, db) -> None:
        self.db = db

    def get_platforms(self):
        result = self.db.query(PlatformModel).all()
        return result

    def get_platform(self, id: int):
        result = self.db.query(PlatformModel).filter(
            PlatformModel.id == id).first()
        return result

    def create_platform(self, platform: Platform):
        new_platform = PlatformModel(**platform.dict())
        self.db.add(new_platform)
        self.db.commit()
        return

    def update_platform(self, id: int, data: Platform):
        platform = self.db.query(PlatformModel).filter(
            PlatformModel.id == id).first()
        platform.name = data.name
        platform.category = data.category
        platform.platformgame_id = data.platformgame_id
        self.db.commit()
        return

    def delete_platform(self, id: int):
        self.db.query(PlatformModel).filter(PlatformModel.id == id).delete()
        self.db.commit()
        return
