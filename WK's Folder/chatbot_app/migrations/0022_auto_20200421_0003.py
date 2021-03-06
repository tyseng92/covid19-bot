# Generated by Django 2.2.5 on 2020-04-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_app', '0021_auto_20200420_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='userDiagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('chat_ID', models.CharField(max_length=100, unique=True)),
                ('diagnosis_result', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('check_in', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='feedbacklist',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userlist',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
