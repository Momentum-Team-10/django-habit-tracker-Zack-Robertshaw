from django import forms
from .models import Habit, Record


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            "name",
            "goal",
            "goal_unit",
            "duration",

        ]


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [
            "amount",
            "date",
        ]
