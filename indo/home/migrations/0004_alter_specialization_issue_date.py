# Generated by Django 4.0.7 on 2022-10-18 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_specialization_issue_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialization',
            name='issue_date',
            field=models.DateField(default=''),
        ),
    ]
