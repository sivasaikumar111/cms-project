# Generated by Django 5.1.3 on 2024-11-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMSApp', '0004_rename_notes_weeklylog_work_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='total_units',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
