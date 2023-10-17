from django.db import models
from users.models import User


class Habits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="Автор")
    place = models.CharField(max_length=50, verbose_name="Место")
    time = models.TimeField(verbose_name="Время")
    action = models.CharField(max_length=100, verbose_name="Действие")
    nicehab = models.BooleanField(verbose_name="Признак приятной привычки",
                                  null=True, blank=True)
    relhab = models.CharField(max_length=150,
                              verbose_name="Связанная привычка", null=True,
                              blank=True)
    reward = models.CharField(max_length=100,
                              verbose_name="Вознаграждение",
                              null=True, blank=True)
    periodic = models.IntegerField(verbose_name="Периодичность", default=1)
    time_to_act = models.IntegerField(verbose_name="Время на выполнение")
    is_public = models.BooleanField(default=False,
                                    verbose_name="Признак публичности")

    started = models.IntegerField(default=0, null=True, blank=True)
    cicles = models.IntegerField(default=0,
                                 null=True, blank=True)
    telegram_id = models.IntegerField(default=0,
                                      verbose_name="Telegram-id",
                                      null=True, blank=True)
    can_send = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.id} {self.place} ' \
               f'{self.time} {self.time_to_act} {self.is_public}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
