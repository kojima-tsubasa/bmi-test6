# Generated by Django 2.1.2 on 2020-08-13 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'スロット収支管理', 'verbose_name_plural': 'スロット収支管理'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_10',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_3',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_4',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_5',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_6',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_7',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_8',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_9',
        ),
        migrations.AddField(
            model_name='item',
            name='sample_1',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='機種名'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sample_2',
            field=models.TextField(blank=True, null=True, verbose_name='収支'),
        ),
    ]