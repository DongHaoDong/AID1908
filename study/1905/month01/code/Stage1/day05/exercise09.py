"""
    英文单词翻转
    How are you --> you are How
"""
str01 = "How are you"
list_temp = str01.split(" ")
str_result = " ".join(list_temp[::-1])
print(str_result)
