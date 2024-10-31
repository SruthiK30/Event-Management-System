from django.shortcuts import render,redirect,HttpResponse
from .models import EventPost
from .forms import EventPostForm

#for delete
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404  # Add get_object_or_404
from django.http import JsonResponse  # For AJAX responses


# Create your views here.
def base(request):
    return HttpResponse("Hello Event Coordinators")

def eventlist(request):
    events=EventPost.objects.all
    return render(request,'eventlist.html',{'events':events})

def create_event(request):
    if request.method=='POST':
        form=EventPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(eventlist)
    else:
        form=EventPostForm()
    return render(request,'create_event.html',{'form':form})

def delete_event(request, id):
    event = get_object_or_404(EventPost, id=id)  # Fetch event by ID or show 404
    event.delete()  # Delete the event
    return redirect('events')  # Redirect to event list