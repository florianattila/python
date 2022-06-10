tallies = {
    "I":1,
    "V":5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
}

def RomanNumberToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) -1):
        left = romanNumeral[i]
        right = romanNumeral[i+1]
        if tallies[left] < tallies[right]:
            sum -= left
        else:
            sum += left
        right = left
    return sum

romanNumeral = input("Add meg a római számot! ")
print(f"A római szám értéke: {RomanNumberToDecimal(romanNumeral)}")