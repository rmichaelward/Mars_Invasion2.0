import json

class Scores:
    def __init__(self, file='topscores.json'):
        self.file = file

        self.top_scores = self.readTopScores()

        self.min_score = -1

    def readTopScores(self):
        with open(self.file, "r") as file:
            data = json.load(file)

        return data

    def saveTopScores(self):
        with open(self.file, "w+") as outfile:
            json.dump(self.top_scores, outfile)

    def add_score(self, data):
        # data : {score: number, username: string}

        if data["score"] >= self.min_score:
            if len(self.top_scores) == 10:
                self.top_scores.pop(0)

            self.top_scores.append(data)
            sorted(self.top_scores, key=lambda x: x["score"])

            self.min_score = self.top_scores[0]["score"]
            self.saveTopScores()
            return True

        return False

    def get_scores(self):
        return self.top_scores