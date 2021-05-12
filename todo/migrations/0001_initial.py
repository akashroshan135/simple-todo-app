# Generated by Django 3.2.2 on 2021-05-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('taskName', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now=True)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
