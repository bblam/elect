# Generated by Django 2.0.5 on 2018-05-02 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0002_auto_20180502_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='election.Party'),
        ),
    ]
