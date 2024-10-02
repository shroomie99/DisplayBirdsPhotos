import requests
from flask import Flask, render_template
import json
import os

# Obtain all topics from Unsplash.com
response = requests.get('https://api.unsplash.com/topics', headers={
    'Authorization': 'Client-ID mwRJxBJVmgQENuAV7gKa9efOMrh5R5RICwWt4fUWrcM'
}, params= {
    'page': "1",
    'per_page': "100"
})

# Print all topics (viewed by their slug and ID) from Unsplash.com
data = response.json()
for i in range(len(data)):
    topic_slug_list = data[i]['slug']
    topic_id_list = data[i]['id']
    print("Slug: " + topic_slug_list + ", ID: " + topic_id_list)

# # Write the data to a file
# with open('picture_data.json', 'w') as f:
#     json.dump(data, f)

# # Location of file created
# print(os.getcwd())