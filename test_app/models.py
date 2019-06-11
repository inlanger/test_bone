from django.db import models

# Create your models here.


class Perm(models.Model):

    class Meta:
        permissions = [
            ("view1", "Can view view1"),
            ("view2", "Can view view2"),
        ]
