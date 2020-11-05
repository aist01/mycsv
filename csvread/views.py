from django.shortcuts import render
import csv, io
from django.contrib import messages
# from .models import File
# from .models import Data
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse

# def index(request):
#     template_name = 'csfv/index.html'

#     return HttpResponse("Hello, world. You're at the csvf index.")

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    # declaring template
    template = 'csvread/index.html'

    # def csv_upload(self):
    # data = File.objects.all()
# prompt is a context variable that can have different values depending on their context
    prompt = {
        'order': 'Order of the CSV should be Service ID, Service Type, Description, Price per Hour or Incident'

              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    # data_set = csv_file.read().decode('UTF-8')
    # # setup a stream which is when we loop through each line we are able to handle a data in a stream
    # io_string = io.StringIO(data_set)
    # next(io_string)
    # print(io_string)
    # for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    #     _, created = Data.objects.update_or_create(
    #     service_id=column[0],
    #     service_type=column[1],
    #     description=column[2],
    #     price=column[3]
    # )
    context = {}
    return render(request, template, context)
# return redirect


def open_csv(request):
    template_name = 'csvread/lookup.html'
    csv_file = request.FILES['file']
    # input_file = open(csv_file, 'r')
    lines = csv_file.readlines()
    # thing = {1: lines}
    # for line in lines:
    #     dict.value = line
    # lines = {1: 'a', 2: 'b'}
    context = {}

    return render(request, template_name, {'lines': lines, 'csv_title': "csv file content."})
#     visas veiksmas cia
# turi isskleista faila ir files index
# request.FILES['file'],open,  paduoti masyva, print lines


