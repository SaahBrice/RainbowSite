# Generated by Django 4.2.3 on 2023-10-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.ImageField(blank=True, null=True, upload_to='results')),
                ('f2', models.ImageField(blank=True, null=True, upload_to='results')),
                ('f3', models.ImageField(blank=True, null=True, upload_to='results')),
                ('f4', models.ImageField(blank=True, null=True, upload_to='results')),
                ('f5', models.ImageField(blank=True, null=True, upload_to='results')),
                ('lss', models.ImageField(blank=True, null=True, upload_to='results')),
                ('lsa', models.ImageField(blank=True, null=True, upload_to='results')),
                ('usa', models.ImageField(blank=True, null=True, upload_to='results')),
                ('usl', models.ImageField(blank=True, null=True, upload_to='results')),
            ],
        ),
    ]
