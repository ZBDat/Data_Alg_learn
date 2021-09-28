def reverseWords(s: str) -> str:
    list = s.split(" ")
    sentence = ""
    for word in list:
        new = word[::-1]
        sentence = sentence + new + " "
    return sentence


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print(reverseWords(s))
