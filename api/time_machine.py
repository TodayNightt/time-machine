from pathlib import *
import requests
import json
import sys
import os


from backend import API_KEY
from dbs.history import writeHistory


class On_this_day:

    def __init__(self, date, year):
        self.date = date
        self.year = year

    def getData(self):
        url = f'https://en.wikipedia.org/api/rest_v1/feed/onthisday/all/{self.date}'

        headers = {
            'Authorization': 'Bearer' + API_KEY,
            'User-Agent': 'time_machine'
        }
        # Request info
        self.response = requests.get(url, headers=headers)

    # Births

    def getBirths(self):
        data_births = self.response.json()['births']

        # Extract the data needed from the raw json data
        births_name = [data["pages"][0]["normalizedtitle"]
                       for data in data_births if data["year"] == self.year]
        births_extract = [data["pages"][0]["extract"]
                          for data in data_births if data["year"] == self.year]
        births_urls = [data['pages'][0]['content_urls']['desktop']['page']
                       for data in data_births if data["year"] == self.year]
        birth_img_urls = []
        for data in data_births:
            if (data['pages'][0].get('thumbnail') == None and data["year"] == self.year):
                birth_img_urls.append(None)
            elif (data["year"] == self.year):
                birth_img_urls.append(data['pages'][0]['thumbnail']['source'])

        # Zip it to a tuple for iterate
        birth = zip(births_name, births_extract,
                    births_urls, birth_img_urls)
        self.dict_birth = []
        data = ""

        # Checks whether it got data that fulfils the condition using falsey object "[]"
        if births_name:
            for index in range(len(births_name)):
                self.dict_birth += [{'name': births_name[index], 'extract': births_extract[index],
                                    'urls': births_urls[index], 'image': birth_img_urls[index]}]
            for results in birth:
                data += "\n".join([str(item)for item in results])+"\n\n"
            return data
        self.dict_birth = 'Nrf'
        return "No result found\n"

    # Deaths
    def getDeaths(self):
        data_deaths = self.response.json()["deaths"]

        # Extract the data needed from the raw json data
        deaths_name = [data["pages"][0]["normalizedtitle"]
                       for data in data_deaths if data["year"] == self.year]
        deaths_extract = [data["pages"][0]["extract"]
                          for data in data_deaths if data["year"] == self.year]
        deaths_urls = [data["pages"][0]["content_urls"]["desktop"]["page"]
                       for data in data_deaths if data["year"] == self.year]
        death_img_urls = []
        for data in data_deaths:
            if (data['pages'][0].get('thumbnail') == None and data["year"] == self.year):
                death_img_urls.append(None)
            elif (data["year"] == self.year):
                death_img_urls.append(data['pages'][0]['thumbnail']['source'])

        # Zip it to a tuple for iterate
        deaths = zip(deaths_name, deaths_extract, deaths_urls)
        self.dict_death = []
        data = ""

        # Checks whether it got data that fulfils the condition using falsey object "[]"
        if deaths_name:
            for index in range(len(deaths_name)):
                self.dict_death += [{'name': deaths_name[index], 'extract': deaths_extract[index],
                                    'urls': deaths_urls[index], 'image': death_img_urls[index]}]

            for results in deaths:
                data += "\n".join([str(item) for item in results])+"\n\n"
            return data
        self.dict_death = 'Nrf'
        return "No result found\n"

    # Events
    def getEvents(self):
        data_events = self.response.json()["events"]

        # Extract the data needed from json data
        events_name = [data["pages"][0]["normalizedtitle"]
                       for data in data_events if data["year"] == self.year]
        events_extract = [data["pages"][0]["extract"]
                          for data in data_events if data["year"] == self.year]
        events_urls = [data["pages"][0]["content_urls"]["desktop"]["page"]
                       for data in data_events if data["year"] == self.year]
        event_img_urls = []
        for data in data_events:
            if (data['pages'][0].get('thumbnail') == None and data["year"] == self.year):
                event_img_urls.append(None)
            elif (data["year"] == self.year):
                event_img_urls.append(data['pages'][0]['thumbnail']['source'])

        # Zip it to a tuple for iterate
        events = zip(events_name, events_extract, events_urls)
        self.dict_event = []
        data = ""

        # Checks whether it got data that fulfils the condition using falsey object "[]"
        if events_name:
            for index in range(len(events_name)):
                self.dict_event += [{'name': events_name[index], 'extract': events_extract[index],
                                     'urls': events_urls[index], 'image': event_img_urls[index]}]
            for results in events:
                data += "\n".join([str(item) for item in results])+"\n\n"
            return data
        self.dict_event = 'Nrf'
        return "No result found\n"

    def getHolidays(self):
        data_holidays = self.response.json()['holidays']

        # Extract the data needed from json data
        holidays_name = [data["pages"][0]["normalizedtitle"]
                         for data in data_holidays]
        holidays_extract = [data["pages"][0]["extract"]
                            for data in data_holidays]
        holidays_urls = [data["pages"][0]["content_urls"]["desktop"]["page"]
                         for data in data_holidays]

        # Zip it to a tuple for iterate
        holidays = zip(holidays_name, holidays_extract, holidays_urls)
        self.dict_holiday = []
        data = ""

        # Checks whether it got data that fulfils the condition using falsey object "[]"
        if holidays_name:
            for index in range(len(holidays_name)):
                self.dict_holiday += [{'name': holidays_name[index], 'extract': holidays_extract[index],
                                       'urls': holidays_urls[index]}]

            for results in holidays:
                data += "\n".join([str(item) for item in results])+"\n\n"

            return data
        self.dict_holiday = 'Nrf'
        return "No result found\n"

    def returnJson(self):
        self.getData()
        self.getBirths()
        self.getDeaths()
        self.getEvents()
        self.getHolidays()
        self.exportDatabase()
        writeHistory()
        data = {'birth': self.dict_birth, 'death': self.dict_death,
                'event': self.dict_event, 'holiday': self.dict_holiday}
        return data

    def exportDatabase(self):
        # Get the search result and export it as json file
        date = f'\n{self.date}/{self.year}\n'
        birth = []
        death = []
        event = []
        holiday = []

        # iterate data to get name and urls only
        # birth
        if (self.dict_birth != 'Nrf'):
            for array in self.dict_birth:
                birth.append({'name': array['name'], 'urls': array['urls']})
        else:
            birth = ['No result found']

        # death
        if (self.dict_death != 'Nrf'):
            for array in self.dict_death:
                death.append({'name': array['name'], 'urls': array['urls']})
        else:
            death = ['No result found']

        # event
        if (self.dict_event != 'Nrf'):
            for array in self.dict_event:
                event.append({'name': array['name'], 'urls': array['urls']})
        else:
            event = ['No result found']

        # holiday
        if (self.dict_holiday != 'Nrf'):
            for array in self.dict_holiday:
                holiday.append({'name': array['name'], 'urls': array['urls']})
        else:
            holiday = ['No result found']

        data = [{'date': date,
                 'birth': f'{birth}', 'death': f'{death}', 'event': f'{event}', 'holiday': f'{holiday}'}]
        data_json = json.dumps(data)
        Path(os.getcwd() + '/data.json').write_text(data_json)
