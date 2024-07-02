# Prompt for user input
score = input("Enter a score between 0.0 and 1.0: ")

# Convert input to a float
try:
    score = float(score)
except ValueError:
    print("Error: Please enter a numeric value.")
    exit()

try:
    score > 1
except ValueError:
    print("RTFM!")
    exit()

# Check if score is within range and assign grade
if score >= 0.9 and score <= 1.0:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
elif score >= 0.0 and score < 0.6:
    grade = 'F'
else:
    print("Error: Score is out of range. Please enter a score between 0.0 and 1.0.")
    exit()

# Print the grade
print(f"{grade}")
