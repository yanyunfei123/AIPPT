from dataclasses import dataclass
from typing import Optional, Dict
import json
from datetime import datetime

@dataclass
class Task:
    id: str
    uuid: str
    work_id: str
    token: str
    status: str
    task_type: str
    user_id: str
    created_at: datetime
    updated_at: datetime
    file_key: Optional[str]
    file_url: Optional[str]
    error_msg: Optional[str]
    params: Dict
    
    @classmethod
    def from_row(cls, row):
        return cls(
            id=row[0],
            uuid=row[1],
            work_id=row[11],
            token=row[12],
            status=row[2],
            file_url=row[3],
            file_key=row[4],
            error_msg=row[8],
            params=json.loads(row[6]),
            task_type=row[5],
            created_at=datetime.fromisoformat(row[9]),
            updated_at=datetime.fromisoformat(row[10]),
        )