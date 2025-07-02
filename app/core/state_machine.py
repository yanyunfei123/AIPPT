from app.utils.logger import logger
import random

class InvalidState(Exception): pass

class TaskStateMachine:
    def __init__(self, task):
        self.task = task

    def next_status(self):
        transitions = {
            "submitted": "outlining",
            "outlining": "content_creating",
            "content_creating": "merging",
            "merging": "exporting",
            "exporting": "success",
        }
        return transitions.get(self.task.status)

    def transition(self, new_status, ppt):
        tid = self.task.id
        work_id = self.task.work_id

        if self.task.status == "submitted":
            ppt.request_outline(work_id)
            return f"UPDATE cap_hiagent.hiagent_async_tasks SET status='outlining', update_time=NOW() WHERE id='{tid}';"

        if self.task.status == "outlining":
            ticket = ppt.request_content(work_id)
            return f"UPDATE cap_hiagent.hiagent_async_tasks SET status='content_creating', file_key='{ticket}', update_time=NOW() WHERE id='{tid}';"

        if self.task.status == "content_creating":
            status = ppt.check_content(self.task.file_key)
            if status == 2:
                return f"UPDATE cap_hiagent.hiagent_async_tasks SET status='merging', update_time=NOW() WHERE id='{tid}';"

        if self.task.status == "merging":
            suit_id = ppt.pick_random_template()
            file_id = ppt.save_design(work_id, suit_id)
            key = ppt.export_file(file_id)
            return f"UPDATE cap_hiagent.hiagent_async_tasks SET status='exporting', file_key='{key}', update_time=NOW() WHERE id='{tid}';"

        if self.task.status == "exporting":
            url = ppt.check_export(self.task.file_key)
            if url:
                return f"UPDATE cap_hiagent.hiagent_async_tasks SET status='success', file_url='{url}', update_time=NOW() WHERE id='{tid}';"
