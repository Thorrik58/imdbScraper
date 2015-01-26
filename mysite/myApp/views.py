from django.shortcuts import render, render_to_response
from chartit import DataPool, Chart
from myApp.models import Movie

def homepage(request):
    ds = DataPool(
       series=
        [{'options': {
            'source': Movie.objects.all()},
          'terms': [
            'name',
            'ranking',
            'rating',
            'year',]}
         ])
    cht = Chart(
        datasource = ds,
        series_options =
          [{'options':{
              'type': 'line',
              'stacking': False},
            'terms':{
              'year': [
                'rating']
              }}],
        chart_options =
          {'title': {
               'text': 'Rating by year'},
           'xAxis': {
                'title': {
                   'text': 'Date'}}})
    return render_to_response('chart.html', {'movieChart': cht})

