from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from .forms import JobForm
import subprocess

def home(request):
    jobs = Job.objects.all()
    return render(request, 'ci_app/home.html', {'jobs': jobs})

def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobForm()
    return render(request, 'ci_app/create_job.html', {'form': form})

def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobForm(instance=job)
    return render(request, 'ci_app/edit_job.html', {'form': form})

def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    job.delete()
    return redirect('home')

import os

def run_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    log_directory = 'job_logs'
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    
    log_file = os.path.join(log_directory, f'job_{job.name}.log')
    
    try:
        result = subprocess.run(['python', '-c', job.script], capture_output=True, text=True)
        output = result.stdout
        error = result.stderr
    except Exception as e:
        output = ''
        error = str(e)
    
    # Zapisz logi do pliku
    with open(log_file, 'a') as f:
        f.write(f"=== Job: {job.name} ===\n")
        f.write(f"Output:\n{output}\n")
        f.write(f"Error:\n{error}\n")
        f.write("=" * 20 + "\n")
    
    return render(request, 'ci_app/run_job.html', {'job': job, 'output': output, 'error': error})

def view_logs(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    log_directory = 'job_logs'
    log_file = os.path.join(log_directory, f'job_{job.name}.log')
    
    logs = ""
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            logs = f.read()
    
    return render(request, 'ci_app/view_logs.html', {'job': job, 'logs': logs})