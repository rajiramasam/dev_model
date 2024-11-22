from django.shortcuts import render, redirect
from .forms import PatientForm

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')  # Replace with your desired redirect URL
    else:
        form = PatientForm()
    return render(request, 'form.html', {'form': form})
