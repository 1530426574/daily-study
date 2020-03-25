# 关键在于加完之后与10整除得到的余数。
class Solution:
    def plusOne(self, digits: list) -> list:
        length = len(digits)
        for i in range(length - 1, -1, -1):
            # 最后一位+1
            digits[i] += 1
            # 如果余数小于等于9，则这轮直接返回，若等于0，则开始下一个
            # 开始进1位，和上一轮一样重新判断
            digits[i] = digits[i] % 10  # 等于余数，如果<9，这一轮直接返回。
            # 这一步判断这一位的位置是否为9，加1之后变为10，如果不为10，直接返回
            if digits[i] != 0:
                return digits
        # 如果遍历一遍
        digits[0] = 1
        return digits
