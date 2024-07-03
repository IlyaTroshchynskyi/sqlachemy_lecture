from sqlalchemy import and_, DECIMAL, func, select

from lecture_scripts.fill_db import fill_db
from lecture_scripts.models import create_table, ResumeModel, session_factory


def select_resumes_avg_compensation(like_language: str = 'Python'):
    """
    select workload, avg(compensation) as avg_compensation
    from resumes
    where title like '%Python%' and compensation > 40000
    group by workload
    having avg(compensation) > 70000
    """
    query = (
        select(ResumeModel.workload, func.avg(ResumeModel.compensation).cast(DECIMAL(10, 2)).label('avg_compensation'))
        .select_from(ResumeModel)
        .filter(and_(ResumeModel.title.contains(like_language), ResumeModel.compensation > 40000))
        .group_by(ResumeModel.workload)
        .having(func.avg(ResumeModel.compensation) > 70000)
    )

    with session_factory() as session:
        # show a query with args
        print(query.compile(compile_kwargs={'literal_binds': True}))
        result = session.execute(query).all()
        print(f'{result=}')


if __name__ == '__main__':
    create_table()
    fill_db()
    select_resumes_avg_compensation()
