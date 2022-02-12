from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Habit, Record
from .forms import HabitForm, RecordForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


@login_required
def home(request):
    user = request.user
    habits = Habit.objects.filter(user=user.pk)

    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user_id = user.pk
            habit.save()
            return redirect(to='home')


    return render(request, "tracker/home.html", {
        "user": user, "habits": habits, "form": form})



@login_required
def habit_records(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    records = Record.objects.filter(habit_id=habit.pk)
    total = Record.objects.filter(habit_id=habit.pk).aggregate(Sum('amount'))
    if request.method == 'GET':
        form = RecordForm()
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.habit_id = habit.pk
            record.save()
            return redirect(to='habit_records', pk=pk)


    return render(request, "tracker/habit_records.html", {
        "form": form, "records": records, "habit": habit, "total":total})



@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='/')
    return render(request, "tracker/delete_habit.html",
                  {"habit": habit})


def add_record(request,pk):
    habit = get_object_or_404(Habit, pk=pk)
    records = Record.objects.filter(pk=habit.pk)
    if request.method == 'GET':
        form = RecordForm()
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.habit_id = habit.pk
            record.save()
            return redirect(to='habit_records', pk=pk)

    return render(request, "tracker/add_record.html", {
        "habit": habit, "form": form, "records": records})


@login_required
def delete_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    habit = get_object_or_404(Habit, pk=pk)

    if request.method == 'POST':
        record.delete()
        return redirect(to='habit_records', pk=pk)

    return render(request, "tracker/delete_record.html",
                  { "habit": habit, "record": record})


