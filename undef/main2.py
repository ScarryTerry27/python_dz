import requests

params = {'prep_id': 2}
responce = requests.get('https://aurora.rlsnet/api/classes_prep/Get_prep_classes', params)
print(responce)