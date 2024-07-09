from sqlalchemy import select

from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, ResumeModel, session_factory, WorkerModel


@line_separator
def any_func():
    query = select(WorkerModel).where(WorkerModel.resumes.any(ResumeModel.title.like('%Python%')))

    with session_factory() as session:
        workers = session.execute(query).scalars().all()
        print(query.compile(compile_kwargs={'literal_binds': True}))

        print(workers)
        print(len(workers))


if __name__ == '__main__':
    create_table()
    fill_db()

    any_func()
