# Generated by Django 4.1.3 on 2022-12-15 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_reviews_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Negizgi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тағам аты:')),
                ('photo', models.ImageField(upload_to='negizgi/', verbose_name='Фото:')),
                ('definition', models.TextField(verbose_name='Анықтама:')),
                ('money', models.PositiveIntegerField(default=0, verbose_name='Ақшасы:')),
            ],
        ),
        migrations.CreateModel(
            name='Susyn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тағам аты:')),
                ('photo', models.ImageField(upload_to='Susyn/', verbose_name='Фото:')),
                ('definition', models.TextField(verbose_name='Анықтама:')),
                ('money', models.PositiveIntegerField(default=0, verbose_name='Ақшасы:')),
            ],
        ),
        migrations.CreateModel(
            name='Tatty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тағам аты:')),
                ('photo', models.ImageField(upload_to='Tatty/', verbose_name='Фото:')),
                ('definition', models.TextField(verbose_name='Анықтама:')),
                ('money', models.PositiveIntegerField(default=0, verbose_name='Ақшасы:')),
            ],
        ),
        migrations.CreateModel(
            name='Un',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тағам аты:')),
                ('photo', models.ImageField(upload_to='un/', verbose_name='Фото:')),
                ('definition', models.TextField(verbose_name='Анықтама:')),
                ('money', models.PositiveIntegerField(default=0, verbose_name='Ақшасы:')),
            ],
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
