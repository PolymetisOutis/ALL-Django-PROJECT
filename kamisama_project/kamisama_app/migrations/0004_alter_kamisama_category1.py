# Generated by Django 4.0 on 2022-04-03 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kamisama_app', '0003_god_alter_countytype3_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kamisama',
            name='category1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kamisama_app.typecategory'),
        ),
    ]
