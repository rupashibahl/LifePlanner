
from sqlalchemy import create_engine, Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()
engine = create_engine('sqlite:///lifeplannerdatabase.db')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    tasks = relationship('Task', back_populates='user', cascade='all, delete')
    def __repr__(self):
        return f'<User(id={self.id}, name={self.name})>'

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='tasks')
    date = Column(Date, nullable=False)
    time = Column(Time)
    title = Column(String, nullable=False)
    description = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
new_user=User(name='Arav')
session.add(new_user)
session.commit()

