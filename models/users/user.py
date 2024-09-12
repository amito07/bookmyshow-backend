from tortoise import fields, models

class User(models.Model):
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=110)
    password = fields.CharField(max_length=255)

    def __str__(self) -> str:
        return self.email
