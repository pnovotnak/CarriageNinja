# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carriage_ninja', '0003_driverslicense_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverslicense',
            name='validated',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
