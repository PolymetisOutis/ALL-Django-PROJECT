# Generated by Django 4.0 on 2022-04-03 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kamisama_app', '0007_taggeditem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daiichinarimasu',
            name='category',
        ),
        migrations.RemoveField(
            model_name='daisangunnarimasu',
            name='category',
        ),
        migrations.RemoveField(
            model_name='shindainanadai',
            name='category',
        ),
        migrations.DeleteModel(
            name='Type2',
        ),
        migrations.DeleteModel(
            name='Type3',
        ),
        migrations.RemoveField(
            model_name='zoukesanshin',
            name='category',
        ),
        migrations.DeleteModel(
            name='DaiichiNarimasu',
        ),
        migrations.DeleteModel(
            name='DaisangunNarimasu',
        ),
        migrations.DeleteModel(
            name='ShindaiNanadai',
        ),
        migrations.DeleteModel(
            name='Type1',
        ),
        migrations.DeleteModel(
            name='ZoukeSanshin',
        ),
    ]
