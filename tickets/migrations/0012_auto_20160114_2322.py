# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-14 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_auto_20160113_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni',
            name='tripos',
        ),
        migrations.AddField(
            model_name='request',
            name='access',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='diet',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='college',
            field=models.CharField(choices=[('Chr', "Christ's"), ('Chu', 'Churchill'), ('Cla', 'Clare'), ('ClH', 'Clare Hall'), ('Cor', 'Corpus Christi'), ('Dar', 'Darwin'), ('Dow', 'Downing'), ('Emm', 'Emmanuel'), ('Fit', 'Fitzwilliam'), ('Gir', 'Girton'), ('Gon', 'Gonville and Caius'), ('Hom', 'Homerton'), ('Hug', 'Hughes Hall'), ('Jes', 'Jesus'), ('Kin', "King's"), ('Luc', 'Lucy Cavendish'), ('Mag', 'Magdalene'), ('Mur', 'Murray Edwards'), ('New', 'Newnham'), ('Pem', 'Pembroke'), ('Pet', 'Peterhouse'), ('Que', "Queens'"), ('Rob', 'Robinson'), ('Sel', 'Selwyn'), ('Sid', 'Sidney Sussex'), ('SCa', "St Catharine's"), ('SEd', "St Edmund's"), ('SJo', "St John's"), ('Tri', 'Trinity College'), ('TrH', 'Trinity Hall'), ('Wol', 'Wolfson'), ('Alu', 'Alumni'), ('Sta', 'Staff')], max_length=3),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('H', 'Half'), ('C', 'Cancelled'), ('S', 'Standard'), ('Q', 'Queue Jump'), ('D', 'Dining')], max_length=1),
        ),
    ]
