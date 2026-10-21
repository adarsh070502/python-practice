class Solution(object):

    def combinations(self, dig, list_index, char_index, combination, res):
        if len(combination) == len(dig):
            res.append(combination)
            return

        for i in range(list_index, len(dig)):
            list_ele = dig[i]
            for j in range(char_index, len(list_ele)):
                char_ele = list_ele[j]
                combination += char_ele
                self.combinations(dig, list_index + 1, char_index, combination, res)
                if len(combination) == len(dig):
                    combination = combination[:-1]
            combination = combination[:-1]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        dic = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        if digits == "":
            return res
        if len(digits) == 1:
            return [ele for ele in dic[int(digits)]]

        dig = []
        for ele in digits:
            dig.append(dic[int(ele)])

        self.combinations(dig, 0, 0, "", res)
        return res


s = Solution()
res = s.letterCombinations("234")
print(res)