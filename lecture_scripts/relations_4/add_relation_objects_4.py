from lecture_scripts.fill_db import line_separator
from lecture_scripts.models import create_table, ResumeModel, session_factory, WorkerModel


@line_separator
def add_resume_to_workers():
    """ """
    with session_factory() as session:
        worker_jack = WorkerModel(username='Jack')
        resume = ResumeModel(title='Resume1', compensation=2, workload='part_time')
        resume2 = ResumeModel(title='Resume2', compensation=3, workload='part_time')

        session.add(worker_jack)
        print(f'{worker_jack.resumes}=')
        worker_jack.resumes.extend([resume, resume2])
        session.commit()
        print('after commit*********************************************')

        print(f'{worker_jack=}')
        print(f'{worker_jack.resumes=}')


if __name__ == '__main__':
    create_table()
    add_resume_to_workers()
