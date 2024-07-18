from sqlalchemy.orm import DeclarativeBase , sessionmaker
from sqlalchemy import Column, Integer , String , Text
from enum import Enum
from config.database import engine

class Base(DeclarativeBase) : 
    pass 

# class StatusTodo(Enum) :
#     accepted = 'Accept'
#     pending = 'Pending'
#     rejected = 'Rejected'


class Todo(Base) : 
    __tablename__ = 'todo' 
    
    id          = Column(Integer, primary_key=True, unique=True, nullable=False)
    description = Column(Text , nullable=False)
    status      = Column(String , nullable=False)



Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
