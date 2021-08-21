from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def send_message(request):
    myInfo = Info.objects.first()

    if request.method == 'POST':
        subject=request.POST['subject']
        email1  =request.POST['email']
        message = request.POST['message']
        
        print(email1)

        # send_mail('subject', 'body of the message', 'flowerlotus026@gmail.com'samarelsayedmohammed12345@gmail.com, ['',])

        send_mail(
            subject,
            message,
            email1,
            [settings.EMAIL_HOST_USER],
              
        )
    context={'myInfo':myInfo}
    return render(request ,'contact\contact.html',context)
