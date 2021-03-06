# Generated by Django 2.1.3 on 2018-12-10 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gate', '0002_auto_20181210_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_visitor',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 448416)),
        ),
        migrations.AlterField(
            model_name='add_visitor',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 448705)),
        ),
        migrations.AlterField(
            model_name='attendence_tracker',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 486847)),
        ),
        migrations.AlterField(
            model_name='attendence_tracker',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 486910)),
        ),
        migrations.AlterField(
            model_name='attendence_tracker',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 487002)),
        ),
        migrations.AlterField(
            model_name='book_cab_details',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 475482)),
        ),
        migrations.AlterField(
            model_name='book_cab_details',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 475813)),
        ),
        migrations.AlterField(
            model_name='book_cab_details',
            name='time_of_depature',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 475351), null=True),
        ),
        migrations.AlterField(
            model_name='bring_groceries',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 480589)),
        ),
        migrations.AlterField(
            model_name='bring_groceries',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 480724)),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 485282)),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 485411)),
        ),
        migrations.AlterField(
            model_name='cooking',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 470783)),
        ),
        migrations.AlterField(
            model_name='cooking',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 470988)),
        ),
        migrations.AlterField(
            model_name='faculty_service_details',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 466361)),
        ),
        migrations.AlterField(
            model_name='faculty_service_details',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 466569)),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 451502)),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 451780)),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='from_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 451128)),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='to_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 451242)),
        ),
        migrations.AlterField(
            model_name='in_out',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 445272)),
        ),
        migrations.AlterField(
            model_name='in_out',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 445477)),
        ),
        migrations.AlterField(
            model_name='laundry_details',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 461958)),
        ),
        migrations.AlterField(
            model_name='laundry_details',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 462153)),
        ),
        migrations.AlterField(
            model_name='medical_sevices',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 482625)),
        ),
        migrations.AlterField(
            model_name='medical_sevices',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 482761)),
        ),
        migrations.AlterField(
            model_name='notify_gate',
            name='date_of_arrival',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 478210)),
        ),
        migrations.AlterField(
            model_name='notify_gate',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 478384)),
        ),
        migrations.AlterField(
            model_name='notify_gate',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 478509)),
        ),
        migrations.AlterField(
            model_name='student_service_details',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 456874)),
        ),
        migrations.AlterField(
            model_name='student_service_details',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 457050)),
        ),
        migrations.AlterField(
            model_name='student_service_details',
            name='work_completed_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 456716)),
        ),
        migrations.AlterField(
            model_name='student_service_details',
            name='worker_assigned_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 456593)),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 162571)),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 162695)),
        ),
        migrations.AlterField(
            model_name='worker_details',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 441240)),
        ),
        migrations.AlterField(
            model_name='worker_details',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 441483)),
        ),
        migrations.AlterField(
            model_name='worker_tracker',
            name='entry_created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 488751)),
        ),
        migrations.AlterField(
            model_name='worker_tracker',
            name='entry_last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 488841)),
        ),
        migrations.AlterField(
            model_name='worker_tracker',
            name='from_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 488600)),
        ),
        migrations.AlterField(
            model_name='worker_tracker',
            name='to_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 22, 40, 47, 488701)),
        ),
    ]
