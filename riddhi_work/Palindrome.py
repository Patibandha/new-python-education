# Write palindrome with following examplerace car
# 1) raceCAr ans: TRUE
# 2) race car! ans: TRUE
# 3) race ccar ans: False
# 4) 121 ans: TRUE

import re


def palindrome(ans):
    ans = ans.lower()
    # ans = re.sub('[^A-Za-z0-9]+', '', ans)
    ans = re.sub('\W+', '', ans)
    return ans == ans[::-1]


text = "raceCAr!"
print(palindrome(text))

text1 = "race car!"
print(palindrome(text1))

text2 = "race ccar"
print(palindrome(text2))

text3 = "121"
print(palindrome(text3))
