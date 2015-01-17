# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '__first__'),
        ('carriage_ninja', '0004_auto_20150117_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField()),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.ForeignKey(to='cities.PostalCode')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='carrier',
            name='user',
        ),
        migrations.AddField(
            model_name='trip',
            name='arrival_zip',
            field=models.ForeignKey(related_name='arrival_postal_code', default=1, to='cities.PostalCode'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='departure_zip',
            field=models.ForeignKey(related_name='departure_postal_code', default=1, to='cities.PostalCode'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trip',
            name='carrier',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Carrier',
        ),
    ]
