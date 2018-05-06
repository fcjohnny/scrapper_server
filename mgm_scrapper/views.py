from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .mgm_scrapper import scrap
import datetime
import json
import sys

from django.views.generic import ListView,TemplateView

from mgm_scrapper.models import Quote

# Create your views here.

class Index(TemplateView):
  template_name = 'mgm_scrapper/index.html'

def day_query(request):
  try:
    if int(request.POST.get('day')) <= 31 and int(request.POST.get('day')) > 0:
      day = request.POST.get('day')
    if int(request.POST.get('month')) <= 12 and int(request.POST.get('month')) >0:
      month = request.POST.get('month')
    if int(request.POST.get('year')) > 0:
      year = request.POST.get('year')
    datetime.datetime.strptime(year+'-'+month+'-'+day,'%Y-%m-%d')
    return HttpResponseRedirect(reverse(
    'mgm_scrapper:mgm-day-history',args=(year,month,day)))
  except:
    return render(request, 'mgm_scrapper/index.html', {'error_message':
    'Please enter a valid date'})

def save_data(request):
  if request.POST.get('day'):
    day = request.POST.get('day')
    month = request.POST.get('month')
    year = request.POST.get('year')
    q = Quote.objects.filter(room_date=datetime.datetime.strptime(
      year+'-'+month+'-'+day,'%Y-%m-%d'))
  else:
    q = Quote.objects.all()
  l = []
  for quote in q:
    l.append([
      quote.quotation_date.strftime('%Y-%m-%d %H:%M'),
      quote.room_date.strftime('%Y-%m-%d'),
      quote.currency,
      str(quote.quoted_price),
      quote.availability
    ])
  json_data = json.dumps(l)
  response = HttpResponse(json_data, content_type='application/json')
  response['Content-Disposition'] = 'attachment;\
  filename="'+datetime.datetime.now().strftime('%Y-%m-%d')+'.json"'
  return response

class MgmDataView(ListView):
  model = Quote
  def get_queryset(self):
    try:
      date = datetime.date(self.kwargs['year'], self.kwargs['month'],
        self.kwargs['day'])
    except:
      return Quote.objects.all()
    return Quote.objects.filter(room_date=date)
  def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    try:
      data['year'] = self.kwargs['year']
      data['month'] = self.kwargs['month']
      data['day'] = self.kwargs['day']
    finally:
      return data
