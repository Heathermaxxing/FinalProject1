class VotingModel:
    def __init__(self):
        self.candidates = {'Cameron': 0, 'Allison': 0, 'Diego': 0}

    def vote_for_candidate(self, candidate_name):
        if candidate_name in self.candidates:
            self.candidates[candidate_name] += 1
