import requests
import json
import os.path
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    # Handle the form submission when it's a POST request
    if request.method == "POST":
        
        # Retrieve the search query from the form data. I.e. User submit input from search bar
        query = request.form.get('query')

        print(query)

        try:
            # Get a list of 10 random photos from Unsplash
            response = requests.get('https://api.unsplash.com/photos/random', params={
                'client_id': 'mwRJxBJVmgQENuAV7gKa9efOMrh5R5RICwWt4fUWrcM',
                'count': '20',
                'auto': 'format',
                'orientation': 'landscape',
                'query': query,
            })
            data = response.json()

            # Inform user when receive error from Unsplash API that "No photos found."
            try:
                # print(data['errors'][0] == 'No photos found.')
                data['errors'][0] == 'No photos found.'
                # print("Your search query is invalid. Please try another.")
                error_msg = "Your search query is invalid. Please try another."
                return render_template('index_searchbar_added2.html', error_msg = error_msg)
            
            except:

                # Inform user that they have maxed Unsplash API calls for the day or hour. 
                # print("Rate limit remaining", response.headers['X-Ratelimit-Remaining'])
                if(response.headers['X-Ratelimit-Remaining'] == '0'):
                    # print("You have maxed out API calls to Unsplash database. Please come back in 1 hour.")
                    error_msg = "You have maxed out API calls to Unsplash database. Please come back in 1 hour."
                    return render_template('index_searchbar_added2.html', error_msg = error_msg)
            

                # Extract the URLs of the photos
                photo_urls = [photo['urls']['thumb'] for photo in data]
                
                # Save the data to file
                filepath = r"C:\Users\Benjamin\Desktop\Python Projects\DisplayBirdPhotos\data\bird_data.json"
                with open(filepath, "w") as f:
                    json.dump(data, f)
        
        # When unable to call Unsplash API, display photos stored in bird_data.json to webpage
        except Exception as e:
            print("Error", e)
            # If an error is thrown, extract URLs of the photos from file
            filepath = r"C:\Users\Benjamin\Desktop\Python Projects\DisplayBirdPhotos\data\bird_data.json"
            with open(filepath, "r") as f:
                data = json.load(f)
                photo_urls = [photo['urls']['thumb'] for photo in data]

        # Render the HTML template and pass the photo URLs to it
        return render_template('index_searchbar_added2.html', photo_urls=photo_urls)
        
    # Handle the initial GET request. I.e. render the search form
    else:
        return render_template('index_searchbar_added2.html',)

if __name__ == '__main__':
    app.run(debug=True)

