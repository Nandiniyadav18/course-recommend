import pandas as pd

class CourseRecommender:
    def __init__(self, data):
        self.data = data

    def recommend_from_query(self, query):
        # Simple GenAI-like filter using lowercase keyword matching
        query = query.lower()
        matches = self.data[
            self.data['course_title'].str.lower().str.contains(query) |
            self.data['subject'].str.lower().str.contains(query) |
            self.data['level'].str.lower().str.contains(query)
        ]
        if matches.empty:
            return pd.DataFrame()
        # Sort by most popular
        return matches.sort_values(by='num_subscribers', ascending=False).head(5)
