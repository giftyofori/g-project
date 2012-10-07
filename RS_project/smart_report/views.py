from django.shortcuts import render_to_response, redirect
from django.template import context, loader
from django.http import HttpResponse,HttpResponseRedirect
from smart_report.models import Student, Bill, School, Teacher,Course,Report
from django.forms import ModelForm
from django import forms
from django.views.decorators.csrf import csrf_exempt
import datetime


def home(request):
    return render_to_response('smart_report/base.html',{'clock': datetime.datetime.now()})








