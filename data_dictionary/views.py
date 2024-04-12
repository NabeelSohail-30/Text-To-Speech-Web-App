from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DataEntry
from .forms import DataEntryForm


@login_required
def data_dictionary(request):
    entries = DataEntry.objects.all()
    form = DataEntryForm()
    if request.method == 'POST':
        form = DataEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_dictionary')
    return render(request, 'data_dictionary.html', {'entries': entries, 'form': form})
