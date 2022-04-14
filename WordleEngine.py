from random import randint
from wordle_data import pickle_load
from resolve_guess import resolve_guess

wordle_words = pickle_load("wordle_words.pickle")


class WordleEngine:
    def __init__(self, solution):
        self._solution = solution
        self._state = "00000"
        self._guess_count = 0

    @property
    def state(self):
        return self._state

    @property
    def guess_count(self):
        return self._guess_count

    def take_guess(self, attempt):
        if attempt not in wordle_words:
            return -1
        else:
            self._guess_count += 1

            new_state = resolve_guess(attempt, self._solution)

            self._state = new_state

            return self._state

    def game_with_human(self):
        print("Hello human, would you like to play wordle?")
        while self.guess_count < 6:

            human_guess = input()
            result = self.take_guess(human_guess)

            if not result == -1:
                self._print_response(human_guess)

            else:
                print("That guess is too shit for me...")

    def _print_response(self, guess):
        colour_translate = ("\u2B1B", "\U0001F7E8", "\U0001F7E9")
        for i in range(5):
            print(f"{guess[i]}", end='\t')
        print("")

        for i in range(5):
            print(f"{colour_translate[int(self._state[i])]}", end='\t')
        print("")


if __name__ == "__main__":
    test_word = input("Test: ")

    if test_word.strip() in wordle_words:
        a_word = test_word

    else:
        all_answers = pickle_load("answer_words.pickle")
        a_word = all_answers[randint(0, 2315)]

    a_wordle = WordleEngine(a_word)
    a_wordle.game_with_human()
    print(a_word)
