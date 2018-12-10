# Generated by Django 2.1.3 on 2018-12-10 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gate', '0005_auto_20181210_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_visitor',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 379976)),
        ),
        migrations.AlterField(
            model_name='add_visitor',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 380107)),
        ),
        migrations.AlterField(
            model_name='attendence_tracker',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 395118)),
        ),
        migrations.AlterField(
            model_name='attendence_tracker',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 395160)),
        ),
        migrations.AlterField(
            model_name='attendence_tracker',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 395269)),
        ),
        migrations.AlterField(
            model_name='book_cab_details',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 389389)),
        ),
        migrations.AlterField(
            model_name='book_cab_details',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 389456)),
        ),
        migrations.AlterField(
            model_name='book_cab_details',
            name='time_of_depature',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 389347), null=True),
        ),
        migrations.AlterField(
            model_name='bring_groceries',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 391925)),
        ),
        migrations.AlterField(
            model_name='bring_groceries',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 391999)),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 394213)),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 394280)),
        ),
        migrations.AlterField(
            model_name='cooking',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 388091)),
        ),
        migrations.AlterField(
            model_name='cooking',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 388161)),
        ),
        migrations.AlterField(
            model_name='faculty_service_details',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 386117)),
        ),
        migrations.AlterField(
            model_name='faculty_service_details',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 386231)),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 381471)),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 381601)),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='from_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 381257)),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='to_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 381319)),
        ),
        migrations.AlterField(
            model_name='in_out',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 378837)),
        ),
        migrations.AlterField(
            model_name='in_out',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 378906)),
        ),
        migrations.AlterField(
            model_name='laundry_details',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 384471)),
        ),
        migrations.AlterField(
            model_name='laundry_details',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 384539)),
        ),
        migrations.AlterField(
            model_name='medical_sevices',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 393043)),
        ),
        migrations.AlterField(
            model_name='medical_sevices',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 393115)),
        ),
        migrations.AlterField(
            model_name='notify_gate',
            name='date_of_arrival',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 390593)),
        ),
        migrations.AlterField(
            model_name='notify_gate',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 390685)),
        ),
        migrations.AlterField(
            model_name='notify_gate',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 390751)),
        ),
        migrations.AlterField(
            model_name='student_service_details',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 382902)),
        ),
        migrations.AlterField(
            model_name='student_service_details',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 382986)),
        ),
        migrations.AlterField(
            model_name='student_service_details',
            name='work_completed_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 382847)),
        ),
        migrations.AlterField(
            model_name='student_service_details',
            name='worker_assigned_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 382808)),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 355446)),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 355528)),
        ),
        migrations.AlterField(
            model_name='worker_details',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 377688)),
        ),
        migrations.AlterField(
            model_name='worker_details',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 377769)),
        ),
        migrations.AlterField(
            model_name='worker_tracker',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 396359)),
        ),
        migrations.AlterField(
            model_name='worker_tracker',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 396421)),
        ),
        migrations.AlterField(
            model_name='worker_tracker',
            name='from_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 396286)),
        ),
        migrations.AlterField(
            model_name='worker_tracker',
            name='to_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 43, 33, 396326)),
        ),
    ]