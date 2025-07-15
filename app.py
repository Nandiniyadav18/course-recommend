from flask import Flask, render_template, request
import pandas as pd
from utils.recommender import CourseRecommender

app = Flask(__name__)

# Load the dataset
data = pd.read_csv("udemy_course_data.csv")
recommender = CourseRecommender(data)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recommend', methods=['POST'])
def recommend():
    query = request.form['query']
    results = recommender.recommend_from_query(query)
    return render_template("results.html", query=query, recommendations=results)

if __name__ == "__main__":
    app.run(debug=True)
