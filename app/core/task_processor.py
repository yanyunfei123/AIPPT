from app.services.ppt_service import PPTService
from app.core.state_machine import TaskStateMachine
from app.utils.logger import logger

class TaskProcessor:
    def __init__(self, task, db):
        self.task = task
        self.db = db
        self.ppt = PPTService(task.work_token)

    def process(self):
        try:
            sm = TaskStateMachine(self.task)
            new_status = sm.next_status()
            sql = sm.transition(new_status, self.ppt)
            if sql:
                self.db.execute_sql(sql)
        except Exception as e:
            logger.exception(f"Error processing task {self.task.id}")
            self.db.mark_failed(self.task.id, str(e))