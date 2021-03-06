# Generated by Django 3.2 on 2021-04-20 17:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated at')),
                ('physician_rating', models.PositiveIntegerField()),
                ('understanding', models.CharField(max_length=255)),
                ('understanding_notes', models.TextField(null=True)),
                ('patient_expression', models.TextField(null=True)),
                ('appointment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.appointment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
