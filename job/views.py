from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from .models import Job
from .form import ApplyForm ,JobForm
from django.urls import reverse
from django.contrib.auth.decorators  import login_required
from .filters import JobFilter



# Create your views here.
def jop_list(request):
    job_list1 =Job.objects.all()

    myfilter = JobFilter(request.GET,queryset=job_list1)
    job_list = myfilter.qs

    paginator = Paginator(job_list, 2) # Show 25 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context ={'jobs':page_obj,'myfilter':myfilter}
    return render(request, 'job/job_list.html',context)

def jop_details(request ,slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method == 'POST':
        form =ApplyForm(request.POST , request.FILES)
        print('test')
        if form.is_valid():
            print('test2')
            myform =form.save(commit=False)
            myform.job = job_detail
            myform.save()
            print('done')
    else:
         form = ApplyForm()
    
    context ={'job':job_detail,'form':form}
    return render(request, 'job/job_details.html',context)
@login_required
def add_job(request):

    if request.method == 'POST':
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form =JobForm()
    context={'form':form}
    return render(request,'job/add_job.html',context)

