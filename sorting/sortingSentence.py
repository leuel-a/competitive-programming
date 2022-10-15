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
        """Sorts a sentence

        Args:
            s (str): this is the sentence to be sorted
        """
        piece = s.split()
        
        sort = {}
        
        for i in piece:
            sort[int(i[-1])] = i[:-1]
            
        s_new = ""
        
        for j in range(1, len(piece) + 1):
            if j == 1:
                s_new = s_new + sort[j]
            else:
                s_new = s_new + " " + sort[j]
            
        return s_new
