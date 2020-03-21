# Generated by Django 3.0.4 on 2020-03-11 15:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0005_contacts_zorder'),
        ('cohort', '0002_auto_20200103_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('summary', models.CharField(blank=True, default='', help_text='Title to use for the event (by default the course title)', max_length=255)),
                ('location', models.CharField(blank=True, default='', help_text='Location to specify for the event (by default the SCS address)', max_length=255)),
                ('description', models.CharField(blank=True, default='', help_text='Extra text describing the event', max_length=2000)),
                ('start', models.DateTimeField(blank=True, default=None, help_text='Date and time the calendar event starts', null=True)),
                ('end', models.DateTimeField(blank=True, default=None, help_text='Date and time the calendar event ends', null=True)),
                ('timezone', models.CharField(choices=[('E', 'America/New_York'), ('C', 'America/Chicago'), ('M', 'America/Denver'), ('P', 'America/Los_Angeles')], default='E', help_text='The time zone of both the start and end time', max_length=1)),
                ('is_holiday', models.BooleanField(default=False, help_text='If the event is an academic holiday (schedule blocked)')),
                ('attendees', models.ManyToManyField(blank=True, help_text='Faculty members attending this event', related_name='calendar_events', to='faculty.Faculty')),
                ('course', models.ForeignKey(blank=True, help_text='Optional course that is associated with this calendar event', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calendar_events', to='cohort.Course')),
            ],
            options={
                'verbose_name': 'Calendar Event',
                'verbose_name_plural': 'Calendar Events',
                'db_table': 'calendar',
                'ordering': ('start',),
            },
        ),
    ]