from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from new_trip.models import Trips, Fisherman, Catch
from django.db.models import Avg, Sum, Max, Count


class StatView(DetailView):
    model = Trips
    template_name = "stats/trip_stat.html"
    context_object_name = "stat"
    #queryset = Trips.objects.all().annotate(
    #    catch_count=Count("catch", distinct=True), # To count the number of catches
    #)    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get fishermen in the trip
        fishermen = Fisherman.objects.filter(trips=self.kwargs.get('pk')).order_by('-catch_sum_weight')

        # it does some aggregation    
        sum_weight = Catch.objects.filter(trip=self.kwargs.get('pk')).aggregate(s_weight=Sum('weight'))
        avg_weigth = Catch.objects.filter(trip=self.kwargs.get('pk')).aggregate(av_weight=Avg('weight'))
        num_catches = Catch.objects.filter(trip=self.kwargs.get('pk')).count()
        max_weight = Catch.objects.filter(trip=self.kwargs.get('pk')).order_by('-weight')[0:1]


        context = {
            "fishermen": fishermen,
            "sum_weight": sum_weight["s_weight"],
            "avg_weight": avg_weigth["av_weight"],
            "max_weight": max_weight,
            "num_catches": num_catches,
        }
        return context 


