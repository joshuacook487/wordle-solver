from wordle_data import pickle_load, generate_responses
from resolve_guess import resolve_guess
from eliminate_answers import eliminate_answers
import numpy as np


def score_by_info(words):
    for guess in words:

        guess_responses = {}
        hit_score = 0

        for hypothetical_solution in words:
            guess_response = resolve_guess(guess, hypothetical_solution)

            if guess_response in guess_responses.keys():
                guess_responses[guess_response] += 1

            else:
                guess_responses[guess_response] = 1

        for response, instances in guess_responses.items():
            hits = 0
            for i in range(5):
                hits += (int(response[i]))

            hit_score += hits

        yield guess, hit_score


def score_elimination(words):
    for guess in words:

        guess_responses = np.ndarray(shape=(3, 3, 3, 3, 3))
        max_remaining = 0

        for r in generate_responses():
            remaining_words = len(eliminate_answers(guess, r, words))

            guess_responses[
                int(r[0])][int(r[1])][int(r[2])][int(r[3])][int(r[4])] \
                = remaining_words

            if remaining_words >= max_remaining:
                max_remaining = remaining_words

        sum_remaining = guess_responses.sum()
        sum_responses = (guess_responses != 0).sum()

        mean_remaining = np.true_divide(
            sum_remaining, sum_responses
        )

        pruned_mean = np.true_divide(
            (sum_remaining - max_remaining),
            (sum_responses - 1)
        )

        yield guess, max_remaining, mean_remaining, pruned_mean


def _test():
    answer_words = pickle_load("answer_words.pickle")
    high_score = 600

    # for v, w in score_by_info(answer_words):
    #     if w >= high_score:
    #         print(v, w)

    for x, y, z, z0 in score_elimination(answer_words):

        if y <= 200:
            print(x, y, z, z0, sep="\t\t")

        elif z <= 17:
            print(x, y, z, z0, sep="\t\t")




if __name__ == "__main__":
    _test()
