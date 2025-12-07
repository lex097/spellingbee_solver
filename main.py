import json
from typing import Dict, Any, List
def loadData() -> Dict:
    with open('words_dictionary.json', 'r') as file:
        return json.load(file)
def checkPangram(word, chars) -> bool:
    freq = {}
    for i in word:
        freq[i] = freq.get(i, 0) + 1
    for char in chars:
        if char not in freq:
            return False
        if freq[char] >= 1:
            continue
        return False
    return True
def main():
    dictionary = loadData()
    chars = ['c', 'a', 'r', 'y', 'o', 'u', 't']
    centerChar = 'o'
    ret = []
    pangrams = []
    def backtrack(count, combo):
        nonlocal centerChar
        if count >= 4: #pangram can have 8
            if centerChar in combo:
                if "".join(combo) in dictionary:
                    ret.append("".join(combo))
                    if (count >= 7) and (checkPangram("".join(combo), chars)):
                        pangrams.append("".join(combo))

        if count == 8:
            return

        for i in chars:
            combo.append(i)
            backtrack(count + 1, combo)
            combo.pop()
        return
    backtrack(0, [])
    print(ret)
    print(f"Pangrams: {pangrams}")
if __name__ == '__main__':
    main()