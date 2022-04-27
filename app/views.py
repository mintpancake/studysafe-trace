from django.shortcuts import render
from django.views.generic import TemplateView
import requests
import json


# Create your views here.
class InfectiousVenues(TemplateView):
    template_name = "venues.html"

    def get_context_data(self, **kwargs):
        hku_id = self.kwargs.get('hku_id')
        date = self.kwargs.get('date')

        url = "http://blooming-beach-58892.herokuapp.com/api/trace/visits/" + hku_id + "/" + date
        try:
            response = requests.get(url)
            result = response.json()
        except (requests.exceptions.RequestException, json.decoder.JSONDecodeError):
            return {}

        if response.status_code == 200:
            venues = []
            for i in range(len(result)):
                if result[i]["venue"] not in venues:
                    venues.append(result[i]["venue"])

            venues.sort()
            context = {
                "venues": venues,
                "subject": hku_id,
                "date": date,
            }
            return context
        return {}


class CloseContacts(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        hku_id = self.kwargs.get('hku_id')
        date = self.kwargs.get('date')

        url = "http://blooming-beach-58892.herokuapp.com/api/trace/contacts/" + hku_id + "/" + date
        try:
            response = requests.get(url)
            result = response.json()
        except (requests.exceptions.RequestException, json.decoder.JSONDecodeError):
            return {}

        if response.status_code == 200:
            contacts = []
            for i in range(len(result)):
                if result[i]["hku_id"] not in contacts:
                    contacts.append(result[i]["hku_id"])

            contacts.sort()
            context = {
                "contacts": contacts,
                "subject": hku_id,
                "date": date,
            }
            return context
        return {}
