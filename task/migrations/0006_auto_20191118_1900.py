# Generated by Django 2.2.7 on 2019-11-18 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_taskallocation_allocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskallocation',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taskallocation', to='task.Task'),
        ),
    ]
