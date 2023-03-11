from models.model import InvolvedCompanyModel
from schemas.involvedcompany import InvolvedCompany


class InvolvedCompanyService():

    def __init__(self, db) -> None:
        self.db = db

    def get_involvedcompanies(self):
        result = self.db.query(InvolvedCompanyModel).all()
        return result

    def get_involvedcompany(self, id: int):
        result = self.db.query(InvolvedCompanyModel).filter(
            InvolvedCompanyModel.id == id).first()
        return result

    def create_involvedcompany(self, involvedcompany: InvolvedCompany):
        new_involvedcompany = InvolvedCompanyModel(**involvedcompany.dict())
        self.db.add(new_involvedcompany)
        self.db.commit()
        return

    def update_involvedcompany(self, id: int, data: InvolvedCompany):
        involvedcompany = self.db.query(InvolvedCompanyModel).filter(
            InvolvedCompanyModel.id == id).first()
        involvedcompany.developer = data.developer
        involvedcompany.publisher = data.publisher
        involvedcompany.company_id = data.company_id
        involvedcompany.game_id = data.game_id
        self.db.commit()
        return

    def delete_involvedcompany(self, id: int):
        self.db.query(InvolvedCompanyModel).filter(
            InvolvedCompanyModel.id == id).delete()
        self.db.commit()
        return
