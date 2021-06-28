from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):#.order_by('-check_in')
  listings = Listing.objects.order_by('list_date').filter(is_published = True)[:3]
  #listings = Listing.objects.all()
  
  context = {
    'listings':listings
  }
  return render(request,'pages/index.html',context)

def about(request):
  realtors = Realtor.objects.order_by('-hire_date')
  # get MVP
  mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
  
  context = {
    'realtors':realtors,
    'mvp_realtors':mvp_realtors
  }
  return render(request,'pages/about.html',context)
