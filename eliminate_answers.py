from wordle_data import pickle_load, generate_responses, sort_dict_by_value


def eliminate_answers(guess, response, answers):

    unused_indices = []
    for i in range(5):

        if response[i] == "2":
            answers = _green_elimate(guess[i], i, answers)

        else:
            unused_indices.append(i)

    for j in unused_indices:

        if response[j] == "1":
            answers = _yellow_eliminate(guess[j], j, unused_indices, answers)

        else:
            answers = _black_eliminate(guess[j], unused_indices, answers)

    return answers


def _green_elimate(letter, index, answers):

    new_words = []
    for word in answers:

        if word[index] == letter:
            new_words.append(word)

    return new_words


# def _yellow_elim(letter, index, remaining_indices, answers):
#     new_words = []
#
#     for word in answers:
#         word_letters = ""
#
#         for i in range(5):
#             if i == index:
#
#                 word_letters += "_"
#
#             elif i in remaining_indices:
#                 word_letters += word[i]
#
#             else:
#                 word_letters += "_"
#
#         if letter in word_letters:
#             new_words.append(word)
#
#     return new_words

def _yellow_eliminate(letter, index, remaining_indices, answers):
    new_words = []

    for word in answers:
        if not word[index] == letter:
            for i in remaining_indices:
                if word[i] == letter:
                    new_words.append(word)
                    break

    return new_words


def _black_eliminate(letter, remaining_indices, answers):
    new_words = []

    for word in answers:
        for i in remaining_indices:
            if word[i] == letter:
                break
        else:
            new_words.append(word)

    return new_words


if __name__ == "__main__":
    answer_words = pickle_load("answer_words.pickle")

    answer_words = eliminate_answers("raise", "00000", answer_words)
    answer_words = eliminate_answers("godly", "02000", answer_words)
    answer_words = eliminate_answers("mount", "02001", answer_words)

    max_answers = {}
    for w in answer_words:
        max_answer = 0
        max_r = ""
        for r in generate_responses():
            reduced_answers = len(eliminate_answers(w, r, answer_words))
            if reduced_answers >= max_answer:
                max_answer = reduced_answers
                max_r = r

        key = (w, max_r)

        max_answers[key] = max_answer

    sorted_max_answers = sort_dict_by_value(max_answers)

    for k, v in sorted_max_answers.items():
        print(k[0], k[1], v)

    # print(len(answer_words))
    # print("")
    # for e, a in enumerate(answer_words):
    #     s = "\t"
    #     if e % 5 == 4:
    #         s = "\n"
    #     print(a, end=s)
