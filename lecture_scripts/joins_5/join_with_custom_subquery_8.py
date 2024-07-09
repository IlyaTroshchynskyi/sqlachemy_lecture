from sqlalchemy import select

from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, ResumeModel, session_factory, WorkerModel


@line_separator
def join_with_subqueries():
    """
    SELECT workers.id, workers.username
    FROM workers JOIN (SELECT resumes.id AS id, resumes.title AS title, resumes.compensation AS compensation,
    resumes.workload AS workload, resumes.worker_id AS worker_id, resumes.created_at AS created_at,
    resumes.updated_at AS updated_at
    FROM resumes
    WHERE resumes.workload = %(workload_1)s) AS anon_1 ON workers.id = anon_1.worker_id
    """
    subquery = select(ResumeModel).where(ResumeModel.workload == 'part_time').subquery()
    query = select(WorkerModel).join(subquery, WorkerModel.id == subquery.c.worker_id)

    with session_factory() as session:
        workers = session.execute(query).scalars().all()
        print(f'{workers=}')
        print(len(workers))


if __name__ == '__main__':
    create_table()
    fill_db()

    join_with_subqueries()
