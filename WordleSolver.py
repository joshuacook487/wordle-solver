from WordleEngine import WordleEngine
from resolve_guess import resolve_guess
from wordle_data import pickle_load
from eliminate_answers import eliminate_answers


class WordleSolver:
    possible_solutions: list

    def __init__(self):
        self._possible_solutions = pickle_load("answer_words.pickle")
        self.log = {}

    def solve(self, game: WordleEngine):
        remaining_words = self.possible_solutions
        while not game.state == "22222":
            guess = self._next_guess(remaining_words)

    def _next_guess(self, words):
        best_word = ""
        return best_word

    def _score_greedy_elimination(self):
        pass

    def _score_average_elimination(self):
        pass
