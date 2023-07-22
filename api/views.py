from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import FormModel
from .serializers import FormSerializer
from django.core.mail import send_mail
from django.conf import settings


def trigger_mail_alert(request):
    name = request.data['name']
    email = request.data['email']
    location = request.data['location']
    message = request.data['message']
    phone = request.data['phone']
    send_mail(
        "ScrapMe New Form - {} - {} - {} - {}".format(name, phone, email, location),
        " A new user has responded to the feedback form. \n \n Following are the details \n Name : {} \n Phone : {} \n Email : {} \n Address : {} \n Message : {}".format(name, phone, email, location, message),
        settings.EMAIL_HOST_USER,
        ['lokeshs.19ec@saividya.ac.in'],
        fail_silently=False,
    )


# Create your views here.
class FormListView(ListCreateAPIView):
    queryset = FormModel.objects.all()
    serializer_class = FormSerializer

    def post(self, request, *args, **kwargs):
        trigger_mail_alert(request)
        return self.create(request, *args, **kwargs)

