import time
import requests
import json
import threading


API_KEY="add-your-id"  
PROJECT_TOKEN="add-your-id"
RUN_TOKEN="add-your-id"



class Data:
  def __init__(self,api_key,project_token):
      self.api_key=api_key
      self.project_token=project_token
      self.params={
          'api_key':self.api_key
      }
      self.get_data()
  def get_data(self):
      response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={"api_key": API_KEY})
      self. data = json.loads(response.text)

  def get_total_cases(self):
      data = self.data['total']

      for content in data:
          if content['name'] == "Coronavirus Cases:":
              return content['value']

  def get_total_deaths(self):
      data = self.data['total']

      for content in data:
          if content['name'] == "Deaths:":
              return content['value']
  def get_total_recovery(self):
      data = self.data['total']

      for content in data:
          if content['name'] == "Recovered:":
              return content['value']

  def get_country_data(self, country):
      data = self.data["country"]

      for content in data:
          if content['name'].lower() == country.lower():
              return content

      return "0"

  def get_list_of_countries(self):
      countries = []
      for country in self.data['country']:
          countries.append(country['name'].lower())

      return countries

  def update_data(self):
      response = requests.post(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/run', params=self.params)

      def poll():
          time.sleep(0.1)
          old_data = self.data
          while True:
              new_data = self.get_data()
              if new_data != old_data:
                  self.data = new_data
                  print("Data updated")
                  break
              time.sleep(5)

      t = threading.Thread(target=poll)
      t.start()

data=Data(API_KEY,PROJECT_TOKEN)
print(data.get_country_data('india'))
