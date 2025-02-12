
def nextGreatestLetter(letters:list, target: str) -> str:
    start = 0
    end = len(letters) - 1
    index = 0

    while start <= end:
        middle = (end - start) // 2 + start
        if target == letters[middle]:
            index = middle
            return letters[index + 1]
        
        elif target > letters[middle]:
            start = middle + 1
        
        elif target < letters[middle]:
            end = middle - 1
        
    return letters[index]


letters = ["c", "f", "j"]
target = "d"
print(nextGreatestLetter(letters, target))