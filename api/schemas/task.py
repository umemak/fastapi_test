from typing import Optional

from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "クリーニングを取りに行く"
            }
        }
    }

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    model_config = {
        "from_attributes": True,
    }

class TaskCreateResponse(TaskCreate):
    id: int

    model_config = {
        "from_attributes": True,
    }
