from WordleInfo import SOLUTIONS, parse_outcomes
from resolve_guess import resolve_guess
from eliminate_solutions import eliminate_solutions
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

        for r in parse_outcomes():
            remaining_words = len(eliminate_solutions(guess, r, words))

            guess_responses[
                int(r[0]), int(r[1]), int(r[2]), int(r[3]), int(r[4])
            ] = remaining_words

            if remaining_words >= max_remaining:
                max_remaining = remaining_words

        sum_remaining = guess_responses.sum()
        sum_responses = (guess_responses != 0).sum()

        mean_remaining = np.true_divide(
            sum_remaining, sum_responses
        )

        yield guess, max_remaining, mean_remaining


def _test():

    print("\n\t\t\tWorst-case Elim.\tAverage Elim.")
    for x, y, z in score_elimination(SOLUTIONS):

        if y <= 200:
            print(f"{x}\t\t{y}\t\t\t\t\t{z:.3f}")

        elif z <= 17:
            print(f"{x}\t\t{y}\t\t\t\t\t{z:.3f}")


if __name__ == "__main__":
    _test()
