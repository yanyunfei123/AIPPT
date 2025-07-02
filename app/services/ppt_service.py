import requests, random
from app.config import URLS, API_KEYS
from app.utils.retry import retry

class PPTService:
    def __init__(self, token):
        self.headers = {
            'x-api-key': API_KEYS['ppt'],
            'x-token': token,
            'x-channel': '',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.base_url = URLS['ppt_base']

    @retry()
    def request_outline(self, task_id):
        url = f"{self.base_url}/api/ai/chat/outline?task_id={task_id}"
        requests.get(url, headers=self.headers)

    @retry()
    def request_content(self, task_id):
        url = f"{self.base_url}/api/ai/chat/v2/content?task_id={task_id}"
        return requests.get(url, headers=self.headers).json()['data']

    @retry()
    def check_content(self, ticket):
        url = f"{self.base_url}/api/ai/chat/v2/content/check?ticket={ticket}"
        return requests.get(url, headers=self.headers).json()['data']['status']

    @retry()
    def pick_random_template(self):
        url = f"{self.base_url}/api/template_component/suit/search"
        suits = requests.get(url, headers=self.headers).json()['data']['list']
        return random.choice([s['id'] for s in suits])

    @retry()
    def save_design(self, task_id, template_id):
        url = f"{self.base_url}/api/design/v2/save"
        payload = f'task_id={task_id}&template_id={template_id}'
        return requests.post(url, headers=self.headers, data=payload).json()['data']['id']

    @retry()
    def export_file(self, file_id):
        url = f"{self.base_url}/api/download/export/file"
        payload = f'edit=true&files_to_zip=false&format=ppt&id={file_id}'
        return requests.post(url, headers=self.headers, data=payload).json()['data']

    @retry()
    def check_export(self, file_key):
        url = f"{self.base_url}/api/download/export/file/result"
        payload = f'task_key={file_key}'
        res = requests.post(url, headers=self.headers, data=payload).json()
        if res['msg'] == '导出成功':
            return res['data'][0]
        return None