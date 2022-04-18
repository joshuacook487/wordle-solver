def _read_into_list(filename):
    with open(filename) as file:
        return [line.strip() for line in list(file)]


def sort_dict_by_value(d):
    return {key: value for key, value in sorted(d.items(), key=lambda x: x[1])}


def parse_outcomes():
    for i0 in range(3):
        for i1 in range(3):
            for i2 in range(3):
                for i3 in range(3):
                    for i4 in range(3):
                        r = str(i0) + str(i1) + str(i2) + str(i3) + str(i4)
                        if not r == "22222":
                            yield r


SOLUTIONS = _read_into_list("data/wordle-answers-alphabetical.txt")

NON_SOLUTIONS = _read_into_list("data/wordle-allowed-guesses.txt")

ALL_WORDS = SOLUTIONS + NON_SOLUTIONS


if __name__ == "__main__":
    for i, word in enumerate(SOLUTIONS):
        if i % 8 == 0 and i != 0:
            print("")
        print(word, end=" ")
