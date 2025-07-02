import time
from app.services.db_service import DBService
from app.models.task import Task
from app.core.task_processor import TaskProcessor
from app.utils.logger import logger

def main_loop():
    db = DBService()
    while True:
        try:
            rows = db.fetch_pending_tasks()
            tasks = [Task.from_row(row) for row in rows]
            for task in tasks:
                processor = TaskProcessor(task, db)
                processor.process()
        except Exception as e:
            logger.error(f"Main loop exception: {e}")
        time.sleep(10)

if __name__ == "__main__":
    main_loop()