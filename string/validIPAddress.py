"""Leetcode Problem #468 --> Validate IP Address"""
from typing import List
from collections import defaultdict


class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        def checkIPV4(query: str) -> bool:
            segments = query.split('.')
            if len(segments) != 4:
                return False

            for segment in segments:
                if not segment.isdigit():
                    return False

                int_val = int(segment)
                if str(int_val) != segment or not (0 <= int_val <= 255):
                    return False

            return True

        def checkIPV6(query: str) -> bool:
            segments = query.split(':')
            if len(segments) != 8:
                return False

            valid_hex_chars = set("0123456789abcdefABCDEF")
            for segment in segments:
                if 1 <= len(segment) <= 4:
                    for char in segment:
                        if char not in valid_hex_chars:
                            return False
                else:
                    return False
            return True

        if checkIPV4(queryIP):
            return "IPv4"
        elif checkIPV6(queryIP):
            return "IPv6"
        return "Neither"
