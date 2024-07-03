from sqlalchemy import select
from sqlalchemy.orm import contains_eager

from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, ResumeModel, session_factory, WorkerModel


@line_separator
def load_only_some_columns():
    query = (
        select(WorkerModel)
        .join(WorkerModel.resumes, isouter=True)
        .options(contains_eager(WorkerModel.resumes).load_only(ResumeModel.title))
        .order_by(ResumeModel.title)
    )

    with session_factory() as session:
        workers = session.execute(query).unique().scalars().all()
        print(f'{workers=}')
        print(len(workers))


if __name__ == '__main__':
    create_table()
    fill_db()

    load_only_some_columns()
