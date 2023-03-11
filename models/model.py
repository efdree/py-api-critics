from config.database import Base
from sqlalchemy import ForeignKey, Column, Integer, String, Date, Boolean, Float
from sqlalchemy.orm import relationship


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)
    critics_count = Column(Integer)

    critics_users = relationship("CriticModel", back_populates="users_critics")


class CriticModel(Base):
    __tablename__ = "critics"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))
    game_id = Column(Integer, ForeignKey("games.id"))

    users_critics = relationship("UserModel", back_populates="critics_users")
    companies_critics = relationship(
        "CompanyModel", back_populates="critics_companies")
    games_critics = relationship("GameModel", back_populates="critics_games")


class CompanyModel(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    start_date = Column(Date)
    country = Column(String)
    cover = Column(String)

    critics_companies = relationship(
        "CompanyModel", back_populates="companies_critics")
    involvedcompanies_companies = relationship(
        "InvolvedCompanyModel", back_populates="companies_involvedcompanies")


class InvolvedCompanyModel(Base):
    __tablename__ = "involvedcompanies"

    id = Column(Integer, primary_key=True, index=True)
    developer = Column(Boolean)
    publisher = Column(Boolean)
    company_id = Column(Integer, ForeignKey("companies.id"))
    game_id = Column(Integer, ForeignKey("games.id"))

    companies_involvedcompanies = relationship(
        "CompanyModel", back_populates="involvedcompanies_companies")
    games_involvedcompanies = relationship(
        "GameModel", back_populates="involvedcompanies_games")


class GameModel(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    summary = Column(String)
    release_date = Column(Date)
    category = Column(Integer)
    rating = Column(Float)
    cover = Column(String)
    parent_id = Column(Integer, ForeignKey("games.id"))
    gameplatform_id = Column(Integer, ForeignKey("gameplatform.id"))
    gamegenre_id = Column(Integer, ForeignKey("gamegenre.id"))

    critics_games = relationship("CriticModel", back_populates="games_critics")
    involvedcompanies_games = relationship(
        "InvolvedCompanyModel", back_populates="games_involvedcompanies")

    parent_id = relationship("GameModel", back_populates="games.id")

    gamesplatforms_games = relationship(
        "GamePlatformModel", back_populates="games_gamesplatforms")
    gamesgenres_games = relationship(
        "GameGenreModel", back_populates="games_gamesgenres")


class GamePlatformModel(Base):
    __tablename__ = "gamesplatforms"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    platform_id = Column(Integer, ForeignKey("platforms.id"))

    games_gamesplatforms = relationship(
        "GamesModel", back_populates="gamesplatforms_games")
    platforms_gamesplatforms = relationship(
        "PlatformModel", back_populates="gamesplatforms_platforms")


class PlatformModel(Base):
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    category = Column(Integer)
    platformgame_id = Column(Integer, ForeignKey("gamesplatforms.id"))

    gamesplatforms_platforms = relationship(
        "GamePlatformModel", back_populates="platforms_gamesplatforms")


class GameGenreModel(Base):
    __tablename__ = "gamesgenres"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    genre_id = Column(Integer, ForeignKey("genres.id"))

    games_gamesgenres = relationship(
        "GamesModel", back_populates="gamesgenres_games")
    genres_gamesgenres = relationship(
        "GenreModel", back_populates="gamesgenres_genres")


class GenreModel(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    category = Column(Integer)
    genregame_id = Column(Integer, ForeignKey("gamesgenres.id"))

    gamesgenres_genres = relationship(
        "GameGenreModel", back_populates="genres_gamesgenres")
