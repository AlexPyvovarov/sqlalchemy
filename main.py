from sqlalchemy import create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker,
)


class Base(DeclarativeBase):
    pass


class Voltage(Base):
     __tablename__ = "voltage"

     id: Mapped[int] = mapped_column(primary_key=True)
     current: Mapped[int]
     voltage: Mapped[int]
     power: Mapped[int]


class Config:
    ENGINE = create_engine("sqlite://", echo=True)
    BASE = Base
    SESSION = sessionmaker(bind=ENGINE)

    @classmethod
    def up(cls):
        cls.BASE.metadata.create_all(cls.ENGINE)

def main():
    Config.up()
    voltage = Voltage(current=35, power=89, voltage=40,)
    with Config.SESSION.begin() as session:
        session.add(voltage)

if __name__ == "__main__":
    main()