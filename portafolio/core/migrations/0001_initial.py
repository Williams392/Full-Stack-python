# Generated by Django 4.2.1 on 2024-02-08 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiPortafolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.CharField(max_length=120)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(default='proyecto_img/img_2.jng', upload_to='proyecto_img/')),
                ('lenguaje', models.CharField(max_length=120)),
                ('tecnologia', models.CharField(blank=True, max_length=120, null=True)),
                ('año', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
