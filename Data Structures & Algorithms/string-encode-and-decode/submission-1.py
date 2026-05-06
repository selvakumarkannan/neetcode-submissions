class Solution:

    def encode(self, strs: List[str]) -> str:
        resp=""
        for string in strs:
            resp += str(len(string))+"#"+string
            # print(resp)
        return resp

    def decode(self, s: str) -> List[str]:
        resp=[]
        i=0

        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            #     print(j)
            # print(s[i:j])
            # print("i is ",i)
            # print("j is", j)
            length = int(s[i:j])
            # print(length)
            i=j+1
            j=i+length
            resp.append(s[i:j])
            # print("resp is", resp)
            i=j

        return resp

