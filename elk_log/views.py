
from django.http import HttpResponse
from rest_framework import views

from elk_log.tasks import log_message


class CreateVMView(views.APIView):
    def get(self, request):
        log_message("This is a test log message.")
        return HttpResponse("Log message sent to Celery.")
