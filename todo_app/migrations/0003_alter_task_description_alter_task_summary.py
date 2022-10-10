# Generated by Django 4.1.1 on 2022-10-10 13:43

from django.db import migrations, models
import todo_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_alter_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True, validators=[todo_app.validators.min_length_validation, todo_app.validators.max_length_validation]),
        ),
        migrations.AlterField(
            model_name='task',
            name='summary',
            field=models.CharField(max_length=200, validators=[todo_app.validators.min_length_validation]),
        ),
    ]