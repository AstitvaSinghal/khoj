from django.shortcuts import render
from guardian.models import *
from core import stats
import json

# Create your views here.
def get_analysis(request):
    lost_stats = stats.lost_stats()
    found_stats = stats.found_stats()
    lost_and_found_relation =  stats.lost_and_found_relation()
    # import pdb;pdb.set_trace()
    data = {'lost_stats': lost_stats,'found_stats' : found_stats,'lost_and_found_relation' : lost_and_found_relation}
    data = json.dumps(data)
    return render(request, 'analyze.html', {'json_string': data})

def police_dashboard(request):
    return render(request, 'police_dashboard.html')

def get_upload_lost_person_image_form(request):
    return render(request, 'upload_lost_person_image_form.html')


def display_heatmap(request):
	fp = open("core/police_stn_coordinates.json","r")
	data = json.load(fp)
	data = json.dumps(data)
	return render(request, 'heatmap.html', {'data': data})
