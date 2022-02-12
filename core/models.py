from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Sum


class User(AbstractUser):
    
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Habit(models.Model):
        user = models.ForeignKey(
            'User', on_delete=models.CASCADE, default=None,)
        name = models.CharField(max_length=100)
        duration = models.DurationField(null=True, )
        goal = models.IntegerField()
        goal_unit = models.CharField(max_length=100, null=True)
        created_at = models.DateTimeField(auto_now_add=True)

        class Meta:
            ordering = ('name',)

        def __str__(self):
            return self.name

        def __repr__(self):
            return f"<Habit name={self.name}>"




class Record(models.Model):
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, default=None, null=True)
    habit = models.ForeignKey(
        'Habit', on_delete=models.CASCADE, default=None, related_name="records")
    amount = models.IntegerField()
    date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Record for {self.habit.name}"

    def __repr__(self):
        return f"<Record name={self.user}>"



