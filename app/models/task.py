from dataclasses import dataclass
from typing import Optional, Dict
import json
from datetime import datetime

@dataclass
class Task:
    id: str
    task_id: str
    status: str
    file_url: Optional[str]
    file_key: Optional[str]
    task_type: str
    params: Dict
    user_id: str
    error_msg: str
    created_at: datetime
    updated_at: datetime
    work_id: str
    work_token: str
    @classmethod
    def from_row(cls, row):
        return cls(
            id=row[0],
            task_id=row[1],
            status=row[2],
            file_url=row[3],
            file_key=row[4],
            task_type=row[5],
            params=json.loads(row[6]),
            user_id=row[7],
            error_msg=row[8],
            created_at=row[9],
            updated_at=row[10],
            work_id=row[11],
            work_token=row[12]
        )