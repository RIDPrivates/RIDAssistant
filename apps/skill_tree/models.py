
from django.conf import settings

from apps.core.models import BaseModel
from django.db import models

class SkillTree(BaseModel):
    name = models.CharField(max_length=64)