import requests
import json
import os.path
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Get a list of 10 random photos from Unsplash
        response = requests.get('https://api.unsplash.com/photos/random', params={
            'client_id': 'mwRJxBJVmgQENuAV7gKa9efOMrh5R5RICwWt4fUWrcM',
            'count': '20',
            'auto': 'format',
            'orientation': 'landscape',
            'query': 'bird',
        })
        data = response.json()
        
        # Extract the URLs of the photos
        photo_urls = [photo['urls']['thumb'] for photo in data]
        
        # Save the data to file
        filepath = r"C:\Users\Benjamin\Desktop\Python Projects\DisplayBirdPhotos\data\bird_data.json"
        with open(filepath, "w") as f:
            json.dump(data, f)
            
    except:
        # If an error is thrown, extract URLs of the photos from file
        filepath = r"C:\Users\Benjamin\Desktop\Python Projects\DisplayBirdPhotos\data\bird_data.json"
        with open(filepath, "r") as f:
            data = json.load(f)
            photo_urls = [photo['urls']['thumb'] for photo in data]

    # Render the HTML template and pass the photo URLs to it
    return render_template('index_selected_background_color.html', photo_urls=photo_urls)

if __name__ == '__main__':
    app.run(debug=True)

