def resolve_guess(guess, solution):
    response = [0, 0, 0, 0, 0]
    unused_indices = []

    for i in range(5):
        if guess[i] == solution[i]:
            response[i] = 2
            solution = solution[:i] + " " + solution[i + 1:]
        else:
            unused_indices.append(i)

    for j in unused_indices:
        if guess[j] in solution:
            response[j] = 1
            for k in range(5):
                if solution[k] == guess[j]:
                    solution = solution[:k] + " " + solution[k + 1:]
                    break

    return "".join([str(r) for r in response])
