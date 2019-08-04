import sqlalchemy as sqa

from sqlalchemy.ext.declarative import declarative_base

""
Store data using SQLAlchemy.
"""

Base = declarative_base()

class Pet(Base):
    __tablename__ = "pet" 
    id = sqa.Column(sqa.Integer, primary_key=True) 
    type = sqa.Column(sqa.String(16)) 
    breed = sqa.Column(sqa.String(32)) 
    gender = sqa.Column(sqa.Enum("male", "female")) 
    name = sqa.Column(sqa.String(64))
    engine = sqa.create_engine("sqlite:///mydata.db")

Base.metadata.create_all(engine)
