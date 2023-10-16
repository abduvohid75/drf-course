from celery import shared_task
from aiogram import Bot
from django.conf import settings
from habits.models import Habits
from datetime import datetime

bot = Bot(token=settings.TELEGRAM_TOKEN)

@shared_task
def send_notification():
    objects = Habits.objects.filter(can_send=True)
    for object in objects:
        current_time = datetime.now()
        if object.started == 0 and f"{current_time.hour:02d}:{current_time.minute:02d}" == f"{object.time.hour}:{object.time.minute}":
            if object.telegram_id != 0:
                if object.relhab: bot.send_message(object.telegram_id, f"Пора выполннять привычку {object.action} на протяжении {object.time_to_act} секунд в {object.place}, а затем {object.relhab}")
                elif object.reward: bot.send_message(object.telegram_id, f"Пора выполннять привычку {object.action} в {object.place}, а затем наградиться себя {object.reward}")
                object.started = 1440 * object.periodic
                object.save()
            else:
                object.can_send = False
                object.save()
        elif object.started > 0:
            object.started -= 1
            object.save()
