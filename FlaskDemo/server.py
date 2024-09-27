# To fake a database, the collection below will be our application's "data"
reviews = [
    {"book_title":"Confessions of a Python Programmer", "review_text":"A cautionary tale for all would-be programmers", "score":5, "id":"1"},
    {"book_title":"To Serve Man", "review_text":"Delicious recipes", "score":3, "id":"2"},
    {"book_title":"Pride and Prejudice", "review_text":"The pride is ok but the prejudice not so much", "score":4, "id":"3"},
]

from flask import Flask, render_template, request # import what we need to use from the flask library


app = Flask(__name__) # invoke the Flask class


# 1. Example template route
@app.route("/example")
def example_route():
    return render_template("example.html", adjective="fun")


# 2. Show route
# Create a route with the url reviews/ID, where ID is a route variable
# Render the show.html template, providing the review with the matching id
# In the show.html template, display the book_title and review_text information.
# The book_title should be an h2 element, while the review_text should be a paragraph element
# Hint: You will have to loop through the list to find the right review to provide
@app.route("/reviews/<id>")
def show(id):
    review = list(filter(lambda review: review['id'] == id, reviews))[0]
    return render_template("show.html", selected=review)

# 3. Index route
# Create a route with the url "reviews"
# Render the index.html template, providing the entire list of reviews as a keyword argument
# For each review, show the book title as an h2 element, score as an h5 element and review_text as a paragraph element.
@app.route("/reviews")
def index():
    return render_template("index.html", reviews=reviews)

# 4. Create route
# Create a route that accepts a POST request to "/reviews"
# The route should create a new_review dictionary that contains the attached request's data
# Add the new_review dictionary to the reviews list
# Return a dictionary as follows: { "status": 201, "data": reviews } as the response from this route
@app.route("/reviews", methods=["POST"])
def create():
    new_review = {
        "book_title": request.form["book_title"],
        "review_text": request.form["review_text"],
        'score': int(request.form["score"]),
        'id': str(len(reviews) + 1)
    }
    reviews.append(new_review)
    
    return { "status": 201, "data": reviews }

# if the post request was in raw JSON could use below
# new_review = request.get_json()
# new_review["id"] = new_id
# Use Postman or run the following code *in another notebook* to send the POST request 
# import requests

# new_review = {
#     "book_title": "War and Peace 2: Return of the Andrei",
#     "review_text": "Tolstoy should have stopped with the first one.",
#     'score': 2,
# }

# response = requests.post(url="http://127.0.0.1:5000/reviews", data=new_review)
# display(response)



if __name__ == '__main__':
    app.run(debug=True) # Start the server listening for requests