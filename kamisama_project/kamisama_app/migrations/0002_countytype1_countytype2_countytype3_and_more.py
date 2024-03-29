# Generated by Django 4.0 on 2022-04-03 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kamisama_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountyType1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name': 'Type1群',
                'verbose_name_plural': 'Type1群',
                'db_table': 'type1county',
            },
        ),
        migrations.CreateModel(
            name='CountyType2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name': 'Type2群',
                'verbose_name_plural': 'Type2群',
                'db_table': 'type2county',
            },
        ),
        migrations.CreateModel(
            name='CountyType3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name': 'Type3群',
                'verbose_name_plural': 'Type3群',
                'db_table': 'type3county',
            },
        ),
        migrations.CreateModel(
            name='GroupType1County3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kamisama_app.countytype1')),
            ],
            options={
                'verbose_name': 'Type1County3グループ',
                'db_table': 'type1county3group',
            },
        ),
        migrations.CreateModel(
            name='GroupType2County3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kamisama_app.countytype2')),
            ],
            options={
                'verbose_name': 'Type2County3グループ',
                'db_table': 'type2county3group',
            },
        ),
        migrations.CreateModel(
            name='GroupType3County1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kamisama_app.countytype3')),
            ],
            options={
                'verbose_name': 'Type3County1グループ',
                'db_table': 'type3county1group',
            },
        ),
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='その他', max_length=20)),
            ],
            options={
                'verbose_name': 'その他',
                'verbose_name_plural': 'その他',
            },
        ),
        migrations.CreateModel(
            name='TypeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name': '類型',
                'verbose_name_plural': '類型',
                'db_table': 'type',
            },
        ),
        migrations.RenameModel(
            old_name='Narimasu',
            new_name='Type1',
        ),
        migrations.RenameModel(
            old_name='Umareru',
            new_name='Type2',
        ),
        migrations.RenameModel(
            old_name='Mibunrui',
            new_name='Type3',
        ),
        migrations.DeleteModel(
            name='Sonota',
        ),
        migrations.AlterModelOptions(
            name='daiichinarimasu',
            options={'verbose_name': '第一グループ', 'verbose_name_plural': '第一グループ'},
        ),
        migrations.AlterModelTable(
            name='daiichinarimasu',
            table='type1_group1',
        ),
        migrations.AlterModelTable(
            name='daisangunnarimasu',
            table='type1_county3',
        ),
        migrations.AlterModelTable(
            name='shindainanadai',
            table='type1_county2',
        ),
        migrations.AlterModelTable(
            name='type1',
            table='type1',
        ),
        migrations.AlterModelTable(
            name='zoukesanshin',
            table='type1_county1',
        ),
        migrations.AddField(
            model_name='countytype3',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kamisama_app.typecategory'),
        ),
        migrations.AddField(
            model_name='countytype2',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kamisama_app.typecategory'),
        ),
        migrations.AddField(
            model_name='countytype1',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kamisama_app.typecategory'),
        ),
    ]
