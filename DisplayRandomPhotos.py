import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Get a list of 10 random photos from Unsplash
    response = requests.get('https://api.unsplash.com/photos/random', params={
        'client_id': 'mwRJxBJVmgQENuAV7gKa9efOMrh5R5RICwWt4fUWrcM',
        #'topics': 'Fzo3zuOHN6w',
        'count': '10',
        'auto': 'format',
        'orientation': 'portrait',
        'query': 'bird',
    })
    data = response.json()

    # Extract the URLs of the photos
    photo_urls = [photo['urls']['thumb'] for photo in data]

    # Render the HTML template and pass the photo URLs to it
    return render_template('v1/index_with_CSS2.html', photo_urls=photo_urls)

if __name__ == '__main__':
    app.run(debug=True)