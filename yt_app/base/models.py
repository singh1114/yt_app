"""Base models that are going to be used everywhere."""

import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class BaseTimeModel(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(default=timezone.now)


class BaseUUIDModel(models.Model):

    class Meta:
        abstract = True

    uuid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)


class AbstractBaseModel(BaseTimeModel, BaseUUIDModel):

    class Meta:
        abstract = True
        ordering = ('-created_at',)
