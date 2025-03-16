from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


# SQLite ma'lumotlar bazasiga bog'lanish
engine = create_engine('sqlite:///example.db', echo=True)

# Ma'lumotlar bazasini yaratish
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'  # SQL jadval nomi
	
    id = Column(Integer, primary_key=True)     
    name = Column(String, nullable=False)     
    age = Column(Integer)         


# Ma'lumotlar bazasiga bog'lanish
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

# new_user = User(name="Ali", age=25)
# session.add(new_user)
# session.commit()  # O‘zgarishlarni bazaga saqlash
# session.close()  # Sessionni yopish

# users = session.query(User).all()
# for user in users:
#     print(user.id, user.name, user.age)

user = session.query(User).filter_by(id=1).first()
print(user.name, user.age)



