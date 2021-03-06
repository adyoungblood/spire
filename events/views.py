import pytz
from dal import autocomplete

from rest_framework import status
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse,Http404
from rest_framework.decorators import detail_route, list_route
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,render_to_response
from .models import Event, EventAttendance,EventPricing, Product
from .serializers import *
from members.serializers import MemberSerializer
from members.models import Member

import datetime

from spire.decorators import member_access

from django.db.models import Count, Value, F
from django.db.models.functions import TruncMonth

from django.contrib.auth import authenticate, login

def index(request):
    """
    Events Index Page
    """
    events = Event.objects.all()
    return render(request, 'events/event_detail.html', {'events': events})


def event_detail(request,slug):

    try:
        event = Event.objects.get(slug=slug)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")

    #dont get pricing if user is not logged in
    if request.user.is_authenticated():
        try:
            member = Member.objects.get(user=request.user)
        except Member.DoesNotExist:
            messages.error(request, 'Membership not found')
            return redirect('/accounts/logout')

        #if already registered
        if EventAttendance.objects.filter(member=member, event=event).count() > 0:
            registered = True
        else:
            registered = False

        membership_level = member.membership_level
        #make sure it only returns 1 object
        event_price = EventPricing.objects.filter(event=event,level=membership_level).order_by('event_price').first()

        #get addtional products for event
        event_gifts = Product.objects.filter(event=event, category="GIFTS")
        event_tribute = Product.objects.filter(event=event, category="TRIBUTE")
        event_sponsors = Product.objects.filter(event=event, category="SPONSORSHIP")

        return render(request, 'events/event_detail.html', {'event': event, 'price': event_price, 'registered': registered, 'gifts':event_gifts, 'tributes': event_tribute, 'sponsors': event_sponsors})

    else:
        #get addtional products for event
        event_gifts = Product.objects.filter(event=event, category="GIFTS")
        event_tribute = Product.objects.filter(event=event, category="TRIBUTE")
        event_sponsors = Product.objects.filter(event=event, category="SPONSORSHIP")

    return render(request, 'events/event_detail.html', {'event': event, 'gifts':event_gifts, 'tributes': event_tribute, 'sponsors': event_sponsors})


def event_register(request,slug):
    try:
        event = Event.objects.get(slug=slug)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    return render(request, 'events/event_detail.html', {'event': event})



class EventViewSet(viewsets.ModelViewSet):
    """
        Event Viewset for api
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @detail_route(methods=['get'])
    def get_attendance(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        #members = Members.objects.filter()
        members = EventAttendance.objects.filter(event=event)

        serializer = EventAttendanceSerializer(members, many=True)
        return Response(serializer.data)


    @list_route()
    def get_attendance_by_month_count(self, request):
        members = EventAttendance.objects.annotate(name=TruncMonth('event__start')) \
            .values('name')  \
            .annotate(value=Count('member__id'))  \
            .values('name', 'value')

        serializer = AggregateSerilizer(members, many=True)
        return Response(serializer.data)


    @list_route()
    def get_upcoming(self, request):

        time_frame = request.GET.get('days', '')
        current_date = datetime.datetime.now()

        if(time_frame != ''):
            events = Event.objects.filter(start__lte=current_date+datetime.timedelta(days=int(time_frame)), start__gte=current_date)
        else:
            events = Event.objects.filter(start__gte=current_date)



        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    @list_route()
    def get_past(self, request):

        time_frame = request.GET.get('days', '')
        current_date = datetime.datetime.now()

        if(time_frame != ''):
            events = Event.objects.filter(start__gte=current_date-datetime.timedelta(days=int(time_frame)), start__lte=current_date)
        else:
            events = Event.objects.filter(start__lte=current_date)


        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)



class EventAttendanceViewSet(viewsets.ModelViewSet):
    """
        Event Attendance Viewset for api
    """
    queryset = EventAttendance.objects.all()
    serializer_class = EventAttendanceSerializer





class EventAttendanceAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Member.objects.none()

        qs = Member.objects.all()

        if self.q:
            qs = qs.filter(user__username__icontains=self.q)

        return qs
