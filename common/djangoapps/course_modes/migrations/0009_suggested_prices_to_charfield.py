# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import
from django.db import migrations, models
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('course_modes', '0008_course_key_field_to_foreign_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemode',
            name='suggested_prices',
            field=models.CharField(default=b'', max_length=255, blank=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\d,]+\\Z'), 'Enter only digits separated by commas.', 'invalid')]),
        ),
    ]
