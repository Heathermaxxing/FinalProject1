class VotingController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def display_results(self):
        result_str = f"Cameron – {self.model.candidates['Cameron']}, Allison – {self.model.candidates['Allison']}, Diego – {self.model.candidates['Diego']}, Total – {sum(self.model.candidates.values())}"
        self.view.results_label.config(text=result_str)

    def vote(self):
        candidate_name = self.view.selected_candidate.get()

        if candidate_name:
            self.model.vote_for_candidate(candidate_name)
            self.display_results()
            print(f'Voted {candidate_name}')
        else:
            print('Please choose a candidate')

    def export_results(self):
        with open("voting_results.txt", "w") as file:
            file.write("Voting Results\n")
            file.write("----------------\n")
            for candidate, votes in self.model.candidates.items():
                file.write(f"{candidate}: {votes} votes\n")
            file.write("----------------\n")
            file.write(f"Total votes: {sum(self.model.candidates.values())}")
        print("Voting results exported to voting_results.txt")
