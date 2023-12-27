from collections import defaultdict


def groupAnagrams(strs):
    # It creates a defaultdict where the default value for any key is an empty list
    # if you try to access a key that hasn't been used before,Instead of raising an error, it will create a new key  with an empty list as its default value.
    anagram_map = defaultdict(list)

    for word in strs:
        # the characters are concatenated without any space or other characters between them
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)

    return list(anagram_map.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
