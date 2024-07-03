from sqlalchemy import select

from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, ResumeModel, session_factory, WorkerModel


@line_separator
def join_from_func():
    """
    Take the columns from resume but from left side will be WorkerModel
    result[0].worker - will be a new query
     SELECT resumes.id, resumes.title, resumes.compensation, resumes.workload, resumes.worker_id,
     resumes.created_at, resumes.updated_at
    FROM workers JOIN resumes ON workers.id = resumes.worker_id
    We have in select resume but in from clouse we see first workers
    """
    query = select(ResumeModel).join_from(WorkerModel, WorkerModel.resumes)

    with session_factory() as session:
        resumes = session.execute(query).scalars().all()
        print(resumes)
        print(resumes[0].worker)


if __name__ == '__main__':
    create_table()
    fill_db()

    join_from_func()
