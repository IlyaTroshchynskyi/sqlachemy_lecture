from sqlalchemy import select
from sqlalchemy.orm import raiseload

from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, session_factory, WorkerModel


@line_separator
def raise_load():
    query = select(WorkerModel).options(raiseload(WorkerModel.resumes))

    with session_factory() as session:
        result = session.execute(query).unique().scalars().all()
        print(result)
        print(result[0].resumes)


if __name__ == '__main__':
    create_table()
    fill_db()

    raise_load()
