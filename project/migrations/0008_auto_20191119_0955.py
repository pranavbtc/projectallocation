# Generated by Django 2.2.7 on 2019-11-19 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_projectallocation_allocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('underprogress', 'Under progress'), ('created', 'Created'), ('closed', 'Closed')], default=4, max_length=200),
        ),
    ]