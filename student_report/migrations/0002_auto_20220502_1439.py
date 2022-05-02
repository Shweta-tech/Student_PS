# Generated by Django 3.2.13 on 2022-05-02 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='roll_no',
            field=models.ForeignKey(default='0000', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mark',
            name='subject_code',
            field=models.ForeignKey(default='000', on_delete=django.db.models.deletion.SET_DEFAULT, to='student_report.subject'),
        ),
    ]