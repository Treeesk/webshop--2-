# Generated by Django 4.2.3 on 2023-08-14 20:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoist', '0003_remove_today_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='today',
            name='edit_mode',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='today',
            name='tasks',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(1, 'Вы пропустили ввод задачи!')]),
        ),
    ]