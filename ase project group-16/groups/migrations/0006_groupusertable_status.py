# Generated by Django 3.0.2 on 2020-03-30 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_auto_20200328_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupusertable',
            name='status',
            field=models.IntegerField(max_length=1, null=True),
        ),
    ]