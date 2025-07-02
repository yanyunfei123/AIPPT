import requests, json, datetime
from app.config import URLS, API_KEYS, USER_ID, NODES

class DBService:
    def __init__(self):
        self.url = URLS['query']
        self.headers = {
            'Apikey': API_KEYS['workflow'],
            'Content-Type': 'application/json'
        }

    def _run_sql(self, sql: str):
        payload = json.dumps({"InputData": f'{{"sql":"{sql}"}}', "UserID": USER_ID})
        res = requests.get(self.url, headers=self.headers, data=payload)
        return res

    def fetch_pending_tasks(self):
        res = self._run_sql("SELECT * FROM cap_hiagent.hiagent_async_tasks;")
        data = res.json()['nodes'][NODES]['output']
        return eval(eval(data)['output'])

    def execute_sql(self, sql: str):
        self._run_sql(sql)

    def mark_failed(self, task_id, error_msg):
        msg = error_msg.replace("'", "").replace("\n", " ")[:500]
        sql = f"UPDATE cap_hiagent.hiagent_async_tasks SET status='failed', error_msg='{msg}', update_time=NOW() WHERE id='{task_id}';"
        self._run_sql(sql)