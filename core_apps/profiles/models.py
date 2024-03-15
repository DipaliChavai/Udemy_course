from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from core_apps.common.models import TimeStampModel


User = get_user_model()

class Profile(TimeStampModel):
    class Gender(models.TextChoices):
        MALE = "M", _("Male"),
        

