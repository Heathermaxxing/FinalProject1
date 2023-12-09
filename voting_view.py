import tkinter as tk


class VotingView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Voting App")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="VOTE MENU").pack()
        tk.Label(self.root, text="Choose a candidate:").pack()

        self.selected_candidate = tk.StringVar()
        for candidate in ['Cameron', 'Allison', 'Diego']:
            tk.Radiobutton(self.root, text=candidate, variable=self.selected_candidate, value=candidate).pack()

        tk.Button(self.root, text="Vote", command=self.controller.vote).pack()
        tk.Button(self.root, text="Export", command=self.controller.export_results).pack()
        tk.Button(self.root, text="Exit", command=self.root.destroy).pack()

        self.results_label = tk.Label(self.root, text="")
        self.results_label.pack()

        self.root.geometry("700x525")
        self.root.resizable(False, False)

        self.controller.view = self
