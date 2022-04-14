from wordle_data import pickle_load
from resolve_guess import resolve_guess
import numpy as np


# def score_words(words):
#     scores = {}
#
#     hit_score_best = 0
#     max_remaining_best = 2315
#     ave_remaining_best = 2315
#
#     for guess in words:
#
#         guess_responses = {}
#         hit_score = 0
#
#         for hypothetical_solution in words:
#             result = resolve_guess(guess, hypothetical_solution)
#
#             if result in guess_responses.keys():
#                 guess_responses[result] += 1
#
#             else:
#                 guess_responses[result] = 1
#
#         for response, instances in guess_responses.items():
#             hits = 0
#             for r in response:
#                 hits += int(r)
#
#             hits = hits * instances
#             hit_score += hits
#
#         max_remaining = max(guess_responses.values())
#         ave_remaining = sum(guess_responses.values()) / len(guess_responses)
#
#         score = (hit_score, max_remaining, ave_remaining)
#
#         if hit_score > hit_score_best:
#             scores[guess] = score
#             hit_score_best = hit_score
#
#         elif max_remaining < max_remaining_best:
#             scores[guess] = score
#             max_remaining_best = max_remaining
#
#         elif ave_remaining < ave_remaining_best:
#             scores[guess] = score
#             ave_remaining_best = ave_remaining
#
#     return scores


def score_words(words):
    scores = {}

    hit_score_best = 0
    max_remaining_best = 2315
    ave_remaining_best = 2315

    for guess in words:

        guess_responses = {}
        hit_score = 0

        for hypothetical_solution in words:
            result = resolve_guess(guess, hypothetical_solution)

            if result in guess_responses.keys():
                guess_responses[result] += 1

            else:
                guess_responses[result] = 1

        for response, instances in guess_responses.items():
            hits = 0
            for r in response:
                hits += int(r)

            hits = hits * instances
            hit_score += hits

        max_remaining = max(guess_responses.values())
        ave_remaining = sum(guess_responses.values()) / len(guess_responses)

        score = (hit_score, max_remaining, ave_remaining)

        if hit_score > hit_score_best:
            scores[guess] = score
            hit_score_best = hit_score

        elif max_remaining < max_remaining_best:
            scores[guess] = score
            max_remaining_best = max_remaining

        elif ave_remaining < ave_remaining_best:
            scores[guess] = score
            ave_remaining_best = ave_remaining

    return scores


if __name__ == "__main__":
    answer_words = pickle_load("answer_words.pickle")
    answer_scores = score_words(answer_words)

    for k, v in answer_scores.items():
        print(f"{k}\t::\t\tHS: {v[0]}\t\tMRS: {v[1]}\t\tARS: {v[2]}")
