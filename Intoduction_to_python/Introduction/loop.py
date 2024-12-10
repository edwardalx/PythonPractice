# Loop through a list of exam scores and print grades based on a specific grading scale.
grades = [85, 92, 78, 99, 65]
for score in grades:
  if score >= 90:
    print(score, "is an A.")
  elif score >= 80:
    print(score, "is a B.")
  elif score >= 70:
    print(score, "grade C")
    
for i in range(5):
    print("Iteration", i)

