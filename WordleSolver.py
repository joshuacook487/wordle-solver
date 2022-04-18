from WordleEngine import WordleEngine
from WordleInfo import SOLUTIONS, ALL_WORDS
# from resolve_guess import resolve_guess
# from eliminate_answers import eliminate_answers


class WordleSolver:
    def __init__(self):
        self.log = {}

    def solve(self, game: WordleEngine):
        remaining_words = SOLUTIONS
        while not game.state == "22222":
            guess = self._next_guess(remaining_words)

    def _next_guess(self, words):
        best_word = ""
        return best_word

    def _score_greedy_elimination(self):
        pass

    def _score_average_elimination(self):
        pass
