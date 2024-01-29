from flask import Flask, render_template
import httpx

app = Flask(__name__)

@app.route("/")
def index():
    baker_username = "shikkiss"
    baker_details = fetch_baker_details(baker_username)
    cake_catalog = fetch_cake_catalog()
    
    return render_template(
        "index.html",
        baker_details=baker_details,
        cake_catalog=cake_catalog
    )

def fetch_baker_details(baker_username):
    # Fetch baker details from Instagram API or any other source
    # Replace the following placeholders with actual data
    baker_details = {
        "name": "HAI'S Bakery ",
        "instagram_username": baker_username
    }
    return baker_details

def fetch_cake_catalog():
    # Fetch cake catalog from the web or any other source
    # Replace the following placeholders with actual data
    cake_catalog = [
        {"name": "Chocolate Cake", "description": "Decadent chocolate cake",  "price": "$25"},
        {"name": "Vanilla Cupcakes", "description": "Classic vanilla cupcakes",  "price": "$20"},
        # Add more cakes as needed
    ]
    return cake_catalog

if __name__ == "__main__":
    app.run(debug=True)
