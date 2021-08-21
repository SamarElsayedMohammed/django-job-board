from  .models import Job
from .serializer import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET'])
def job_list_api(request):
    all_jobs = Job.objects.all()
    data = JobSerializer(all_jobs ,many=True).data
    return Response({'data': data})

@api_view(['GET'])
def job_detail_api(request,id):
    job_detail = Job.objects.get(id=id)
    data = JobSerializer(job_detail).data
    return Response({'data': data})