from sqlalchemy import Column, create_engine, Integer, MetaData, String, Table

engine = create_engine('sqlite:///:memory:', echo=True)
metadata_obj = MetaData()

workers_table = Table(
    'workers',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String(64)),
)


metadata_obj.create_all(engine)
