grade1 = int(input("1st grade: "))
grade2 = int(input("2nd grade: "))
grade3 = int(input("3rd grade: "))
Average = (grade1 + grade2 + grade3) / 3

"""
    Solution 1: Using round function
    Average = round((grade1 + grade2 + grade3) / 3)
"""

# Solution 2: Using "if" to do rounding
if (Average * 10) % 10 >= 5:
    Average = int(Average) + 1
else:
    Average = int(Average)

print(f"Average grade: {Average}")
