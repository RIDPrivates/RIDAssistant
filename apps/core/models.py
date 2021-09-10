from django.utils import timezone


from django.db import models



class BaseModel(models.Model):
    c_at = models.DateTimeField(default=timezone.now)
    u_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
