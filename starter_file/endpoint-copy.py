import requests
import json
import pandas as pd

# URL for the web service, should be similar to:
uri='http://8c4c3158-d6a7-4531-956b-73dc5cc4a1f2.westeurope.azurecontainer.io/score'


test_df=pd.read_csv('test_wine_model.csv')
# Convert to JSON string

test_sample=json.dumps({'data': test_df.to_dict(orient='records')})

# Set the content type
headers = {'Content-Type': 'application/json'}


# Make the request and display the response
resp = requests.post(uri, test_sample, headers=headers)
print(resp.json())