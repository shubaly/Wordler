import json


def filter_fivers(data):
    wordlist = []
    for word in data:
        if len(word) == 5:
            wordlist.append(word)
    return wordlist


def dertermine_frequencies(wordlist):
    # figure out letter frequencies
    frequencies = []
    for i in range(5):
        frequencies.append({})
        for word in wordlist:
            if word[i] in frequencies[i].keys():
                frequencies[i][word[i]] += 1
            else:
                frequencies[i][word[i]] = 1
    return frequencies


def determine_knowns(current_knowns):
    positions = {}
    for i in range(len(current_knowns)):
        if current_knowns[i] == '.':
            continue
        else:
            positions[i] = current_knowns[i]

    return positions


def find_possibles(current_knowns, dead_letters, floating_knowns, wordlist):
    possible_words = []
    for word in wordlist:
        disqualified = False

        # handle known letters
        knowns = determine_knowns(current_knowns)
        num_matches = 0
        for k, v in knowns.items():
            if word[k] == v:
                num_matches += 1
        if num_matches != len(knowns):
            disqualified = True

        # handle dead letters
        if not disqualified:
            for letter in word:
                if letter in dead_letters:
                    disqualified = True

        # handle floating letters
        if not disqualified:
            num_matches = 0
            for letter in floating_knowns:
                if letter in word:
                    num_matches += 1

            if num_matches != len(floating_knowns):
                disqualified = True

        if not disqualified:
            possible_words.append(word)

    return possible_words


def main():
    # https://github.com/dwyl/english-words
    data = json.load(open("words_dictionary.json"))
    wordlist = filter_fivers(data)
    print(wordlist)
    print(len(wordlist))

    # frequencies = dertermine_frequencies(wordlist)
    # for frequency in frequencies:
    #     print({k: v for k, v in sorted(frequency.items(), key=lambda item: item[1])})

    # possible_words = find_possibles('.ri..', 'adeusoftybng', '', wordlist)
    possible_words = find_possibles('.ri..', 'housetalwngk', 'c', wordlist)
    print(possible_words)
    print(len(possible_words))


if __name__ == "__main__":
    main()
