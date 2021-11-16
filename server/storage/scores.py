class Scores:
    def __init__(self, db_file='top_scores'):
        self.db_file = db_file
        self.top_scores = [{'user': 'ryan', 'score': 50}]
        self.min_score = -1

    def add_score(self, data):
        # data : {score: number, username: string}

        if data['score'] < self.min_score:
            return False

        if len(self.top_scores) == 10:
            self.top_scores.pop(0)

        self.top_scores.append(data)
        sorted(self.top_scores, key=lambda x: x["score"])

        self.min_score = self.top_scores[0]["score"]

        return True

    def get_scores(self):
        return self.top_scores