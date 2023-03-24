#!/usr/bin/python3
"""This is the sortingSentence module"""


class Solution:
    """This class is for solutions of the 1859. Sorting the Sentence problem in LeetCode

    Description:

        A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
        Each word consists of lowercase and uppercase English letters.

        A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.
            For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".

        Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
    """
    def sortSentence(self, s: str) -> str:
        """Sorts a sentence based on tokens"""
        split = s.split(' ')
        for i in range(1, len(split)):
            key, j = split[i], i - 1
            while j >= 0 and int(split[j][-1]) > int(key[-1]):
                split[j + 1] = split[j]
                j -= 1
            split[j + 1] = key
        sorted_sentence = ' '.join([str(item[:-1]) for item in split])
        return sorted_sentence
