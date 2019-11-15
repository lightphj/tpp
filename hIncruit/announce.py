from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max
from django.http import JsonResponse
from hIncruit.models import *
from django.utils import timezone
import json
import logging
logger = logging.getLogger(__name__)
# Create your views here.

@csrf_exempt
def makeAnnouncement(request):
    dosomething = 1