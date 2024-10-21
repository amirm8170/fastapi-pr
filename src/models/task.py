from tortoise import Model, fields


class Task(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    created = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'task'
