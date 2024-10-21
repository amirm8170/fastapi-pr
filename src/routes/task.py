from fastapi import APIRouter, HTTPException
from tortoise.exceptions import DoesNotExist

from dto.task import CreateTask, UpdateTask
from models import Task

router = APIRouter(tags=["Tasks"], prefix="/task")


@router.post("")
async def root(task: CreateTask):
    return await Task.create(**task.model_dump())


@router.get("")
async def root():
    return await Task.get()


@router.get("/{task_id}")
async def root(task_id: int):
    try:
        return await Task.get(id=task_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Task not found")


@router.put('/{task_id}')
async def root(task_id: int, updated_task: UpdateTask):
    try:
        task = await Task.get(id=task_id)
        await task.update_from_dict(updated_task.dict())

        await task.save()
        return task
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/{task_id}")
async def root(task_id: int):
    try:
        task = await Task.get(id=task_id)
        await task.delete()
        return {"message": "Task deleted successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Task not found")
