# Generated by Django 4.0 on 2021-12-08 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_habit_duration_habit_goal_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.user'),
        ),
    ]