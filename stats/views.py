from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from new_trip.models import Trips, Fisherman, Catch
from django.db.models import Avg, Sum, Max, Count, Q


class StatView(DetailView):
    model = Trips
    template_name = "stats/trip_stat.html"
    context_object_name = "stat"
    #queryset = Trips.objects.all().annotate(
    #    catch_count=Count("catch", distinct=True), # To count the number of catches
    #)    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # aggregating catches    
        catch_aggregation = Catch.objects.filter(trip=self.kwargs.get('pk')).aggregate(Sum('weight'), Avg('weight'))
        context["weight_sum"] = catch_aggregation["weight__sum"] # total weight of catches
        context["weight_avg"] = catch_aggregation["weight__avg"] # average weigt of catches

        context["catches_num"] = Catch.objects.filter(trip=self.kwargs.get('pk')).count() # total number of cacthes
        context["catch_max"] = Catch.objects.filter(trip=self.kwargs.get('pk')).order_by('-weight')[0:1] # max catch in the trip

        # aggregating fishermen's catches in the trip.
        # Annoteting is being used for summorizing and counting catches. 
        context["fishermen_catches"] = Fisherman.objects.filter(
            trips=self.kwargs.get('pk')).annotate(sum_catch=Sum("catch__weight", distinct=True, filter=Q(catch__trip=self.kwargs.get('pk'))),
            num_catch=Count("catch__catch_id", distinct=True, filter=Q(catch__trip=self.kwargs.get('pk')))).order_by('-sum_catch')
        
        #print(fishermen_catches_sum[0].sum_catch)
        #min_max = Fisherman.objects.filter(trips=self.kwargs.get('pk')).annotate(min_catch=Min("catch__weight"), max_catch=Max("catch__weight"))
        #print(min_max[0].max_catch)
        #avg_catches = Trips.objects.aggregate(avg_c=Avg("catch__weight"))
        #print(avg_catches)
        return context 


