# Generated by Django 4.0.3 on 2022-05-21 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_exam_room_alter_exam_inv_exam_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.room'),
        ),
    ]
