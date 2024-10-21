from typing import Optional

from pydantic import BaseModel, create_model


class CreateTask(BaseModel):
    name: str


UpdateTask = create_model(
    "TaskUpdate",
    **{field: (Optional[CreateTask.__annotations__[field]], None) for field in CreateTask.__annotations__}
)
