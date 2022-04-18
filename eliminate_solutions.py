from WordleInfo import SOLUTIONS, parse_outcomes


def eliminate_solutions(guess, response, remaining_words):

    unused_indices = []
    for i in range(5):

        if response[i] == "2":
            remaining_words = _green_eliminate(guess[i], i, remaining_words)

        else:
            unused_indices.append(i)

    for j in unused_indices:

        if response[j] == "1":
            remaining_words = _yellow_eliminate(guess[j], j, unused_indices, remaining_words)

        else:
            remaining_words = _black_eliminate(guess[j], unused_indices, remaining_words)

    return remaining_words


def _green_eliminate(letter, index, remaining_words):

    new_words = []
    for word in remaining_words:

        if word[index] == letter:
            new_words.append(word)

    return new_words


def _yellow_eliminate(letter, index, remaining_indices, remaining_words):

    new_words = []
    for word in remaining_words:

        if not word[index] == letter:
            for i in remaining_indices:

                if word[i] == letter:
                    new_words.append(word)

                    break

    return new_words


def _black_eliminate(letter, remaining_indices, remaining_words):

    new_words = []
    for word in remaining_words:

        for i in remaining_indices:
            if word[i] == letter:

                break
        else:
            new_words.append(word)

    return new_words


def _test():
    for w in SOLUTIONS:
        max_answer = 0
        words = eliminate_solutions("raise", "00000", SOLUTIONS)
        for r in parse_outcomes():
            reduced_answers = len(eliminate_solutions(w, r, words))

            if reduced_answers > 250:
                break

            elif reduced_answers >= max_answer:
                max_answer = reduced_answers

        else:
            print(w, max_answer)


if __name__ == "__main__":
    _test()
