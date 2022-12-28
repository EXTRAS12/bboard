from django.contrib.auth.models import AbstractUser
from django.db import models


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name="Прошел аткивацию?")
    send_messages = models.BooleanField(default=True, verbose_name="Слать оповещение о комментариях?")

    class Meta(AbstractUser.Meta):
        pass
