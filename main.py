import tkinter as tk
from voting_model import VotingModel
from voting_view import VotingView
from voting_controller import VotingController


def main():
    model = VotingModel()
    root = tk.Tk()
    controller = VotingController(model, None)
    VotingView(root, controller)
    controller.view.controller = controller

    root.mainloop()


if __name__ == "__main__":
    main()
