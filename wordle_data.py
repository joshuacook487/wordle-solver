import pickle


def extract_word_list(filename):
    with open(filename) as file:
        words_from_file = [line.strip() for line in file]
    return words_from_file


def pickle_dump(data, filename):
    with open(f"pickled_data/{filename}", 'wb') as file:
        pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)


def pickle_load(filename):
    with open(f"pickled_data/{filename}", 'rb') as file:
        return pickle.load(file)


def group_words_by_letter(words):
    groups = {}
    for w in words:
        letters = set(w)
        for x in letters:
            if x not in groups:
                groups[x] = [w]
            else:
                groups[x].append(w)

    return groups


def sort_dict_by_value(d):
    return {key: value for key, value in sorted(d.items(), key=lambda x: x[1])}


def generate_responses():
    for i0 in range(3):
        for i1 in range(3):
            for i2 in range(3):
                for i3 in range(3):
                    for i4 in range(3):
                        r = str(i0) + str(i1) + str(i2) + str(i3) + str(i4)
                        if not r == "22222":
                            yield r


if __name__ == "__main__":
    answers = extract_word_list("word_lists/wordle-answers-alphabetical.txt")
    allowed_guesses = extract_word_list("word_lists/wordle-allowed-guesses.txt")
    wordle_words = allowed_guesses + answers

    words_by_letter = group_words_by_letter(answers)

    pickle_dump(answers, "answer_words.pickle")
    pickle_dump(wordle_words, "wordle_words.pickle")
    pickle_dump(words_by_letter, "words_by_letter.pickle")
