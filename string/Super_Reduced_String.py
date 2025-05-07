def returnIndexAdj(s):
    result = float("inf")
    for index in range(len(s)-1):
        if s[index] == s[index+1]:
            result = index
            break
    return result
    

def superReducedString(s):
    # Write your code here
    character = s
    while True:
        if len(character) == 0:
            return "Empty String"
        index = returnIndexAdj(character)
        if index == float("inf"):
            return character
        character = character[0:index] + character[index+2:]
