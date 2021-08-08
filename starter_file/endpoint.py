import requests
import json

# URL for the web service, should be similar to:
uri='http://f2043950-dd92-445e-9ceb-d81d9756f1e1.westeurope.azurecontainer.io/score'



# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "fixed acidity": 5, 
            "volatile acidity": 4, 
            "citric acid": 7,
            "residual sugar": 3,
            "chlorides": 2,
            "free sulfur dioxide": 6,
            "total sulfur dioxide": 8, 
            "density": 4, 
            "pH": 7, 
            "sulphates": 6, 
            "alcohol": 11
          },
          {
            "fixed acidity": 7.3, 
            "volatile acidity": 0.65, 
            "citric acid": 0.0,
            "residual sugar": 1.2,
            "chlorides": 0.065,
            "free sulfur dioxide": 15.0,
            "total sulfur dioxide": 21.0, 
            "density": 0.9946, 
            "pH": 3.39, 
            "sulphates": 0.47, 
            "alcohol": 10.0
          },
      ]
    }

# Convert to JSON string

input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}


# Make the request and display the response
resp = requests.post(uri, input_data, headers=headers)
print(resp.json())
