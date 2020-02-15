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



def display_heatmap(request):
	fp = open("core/police_stn_coordinates.json","r")
	coord_data = json.load(fp)
	fp.close()

	lost_stats = stats.lost_stats()

	coord_data = json.dumps(coord_data)
	lost_stats = json.dumps(lost_stats)

	return render(request, 'heatmap.html', {'coord_data': coord_data , 'lost_stats' : lost_stats})