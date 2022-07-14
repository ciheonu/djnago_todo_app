import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_item = models.CharField(max_length=500)
    date_created = models.DateField(auto_now_add=True)
    date_to_begin = models.DateField(null=True, blank=True)

    @property
    def status(self):
        begin_date = self.date_to_begin
        date_of_today = self.date_created
        if begin_date == date_of_today:
            return "Today's Task"
        elif begin_date < date_of_today:
            return "Completed"
        else:
            return "UnCompleted"

    def __str__(self):
        return self.todo_item

    class Meta:
        ordering = ['date_created']
