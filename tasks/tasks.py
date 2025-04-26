from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .models import Task
from django.conf import settings

@shared_task
def send_email_reminders():
    # Calculate the time 24 hours before the deadline
    reminder_time = timezone.now() + timedelta(days=1)
    
    # Get tasks that have deadlines within the next 24 hours
    tasks_to_remind = Task.objects.filter(deadline__lte=reminder_time, reminder_sent=False)
    
    # Loop through the tasks and send email reminders
    for task in tasks_to_remind:
        # Send an email reminder to the task's owner
        send_mail(
            'Reminder: Task Deadline Approaching',
            f'Your task "{task.title}" is due in 24 hours.',
            settings.DEFAULT_FROM_EMAIL,
            [task.owner.email],
            fail_silently=False,
        )
        
        # Mark the task as reminder sent
        task.reminder_sent = True
        task.save()

    return f"{len(tasks_to_remind)} reminders sent!"
