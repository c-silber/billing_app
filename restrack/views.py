from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Facility, Residents

def index(request):
	facility=Facility.objects.order_by('facility_name')[:5]
	template=loader.get_template('restrack/index.html')
	context = {
		'facility': facility,
	}
	return HttpResponse(template.render(context, request))

def facility(request, facility_id):
	facility = get_object_or_404(Facility, pk=facility_id)
	template=loader.get_template('restrack/facility.html')
	context = {
		'facility': facility,
	}
	return HttpResponse(template.render(context, request))

def resident(request, facility_id):
	facility=get_object_or_404(Facility, pk=facility_id)
	residents=get_list_or_404(Residents, facility_id=facility_id)
	template=loader.get_template('restrack/residents.html')
	context = {
		'residents': residents,
		'facility': facility,
	}
	return HttpResponse(template.render(context, request))