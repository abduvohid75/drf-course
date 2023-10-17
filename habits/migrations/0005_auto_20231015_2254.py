# Generated by Django 3.2.20 on 2023-10-15 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_alter_habits_periodic'),
    ]

    operations = [
        migrations.AddField(
            model_name='habits',
            name='cicles',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='habits',
            name='started',
            field=models.IntegerField(blank=True, default=86400, null=True),
        ),
        migrations.AddField(
            model_name='habits',
            name='telegram_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Telegram-id'),
        ),
    ]