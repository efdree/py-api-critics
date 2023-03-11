from models.model import CompanyModel
from schemas.company import Company


class GameService():

    def __init__(self, db) -> None:
        self.db = db

    def get_companies(self):
        result = self.db.query(CompanyModel).all()
        return result

    def get_company(self, id: int):
        result = self.db.query(CompanyModel).filter(
            CompanyModel.id == id).first()
        return result

    def create_company(self, company: Company):
        new_company = CompanyModel(**company.dict())
        self.db.add(new_company)
        self.db.commit()
        return

    def update_company(self, id: int, data: Company):
        company = self.db.query(CompanyModel).filter(
            CompanyModel.id == id).first()
        company.name = data.name
        company.description = data.description
        company.start_date = data.start_date
        company.country = data.country
        company.cover = data.cover
        self.db.commit()
        return

    def delete_company(self, id: int):
        self.db.query(CompanyModel).filter(
            CompanyModel.id == id).delete()
        self.db.commit()
        return
