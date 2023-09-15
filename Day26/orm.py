#ORM stands for Object Relational Mapping
#It is an interface provided by the language to query the database using objects rather than a raw query
#There are different packages in different languages to support ORM.
#For python 'sqlalchemy' is a famous tool for ORM. (pip install sqlalchemy)
from sqlalchemy import create_engine, Column, String, Integer, CHAR
from sqlalchemy.orm import sessionmaker, declarative_base   

Base = declarative_base()
class student(Base):
    __tablename__ = "student"
    id = Column('ir', Integer, primary_key=True)
    name = Column("name",String)
    age = Column('age',Integer)
    gender = Column('gender',CHAR)

    def __init__(self,id,name, age, gender):
        self.id = id
        self.name= name
        self.age= age
        self.gender = gender

    def __str__(self):
        return self.name
    
engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
print("Connection Established!!")

