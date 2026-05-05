class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resp = defaultdict(list)

        for string in strs:
            charCount = [0]*26


            for character in string:
                charCount[ord(character)-ord("a")] += 1
            resp[tuple(charCount)].append(string)
            # print(resp)
        return list(resp.values())


