from django.shortcuts import render
from rest_framework.views import APIView
import requests
import json


# Create your views here.
class InfectiousVenues(APIView):

    def get(self, request, hku_id, date, format=None):

        url = "http://blooming-beach-58892.herokuapp.com/api/trace/visits/" + hku_id + "/" + date
        response = requests.get(url)
        result = response.json()

        if response.status_code == 200:
            venues = []
            for i in range(len(result)):
                if result[i]["venue"] not in venues:
                    venues.append(result[i]["venue"])

            venues.sort()
            context = {"venues": venues,
                       "subject": hku_id,
                       "date": date}
            return render(request, 'venues.html', context=context)


class CloseContacts(APIView):

    def get(self, request, hku_id, date, format=None):

        url = "http://blooming-beach-58892.herokuapp.com/api/trace/contacts/" + hku_id + "/" + date
        response = requests.get(url)
        result = response.json()

        if response.status_code == 200:
            contacts = []
            for i in range(len(result)):
                if result[i]["hku_id"] not in contacts:
                    contacts.append(result[i]["hku_id"])

            contacts.sort()
            context = {"contacts": contacts,
                       "subject": hku_id,
                       "date": date
                       }
            return render(request, 'contacts.html', context=context)
