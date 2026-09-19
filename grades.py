def analyze_grades(scores):
    # 1. Calculate class average
    if len(scores) == 0:
        print("No scores provided.")
        return
    average = sum(scores) / len(scores)

    # 2. Loop through each score and assign a letter grade
    grades = []
    for score in scores:
        if score >= 80:
            letter = "A"
        elif score >= 60:
            letter = "B"
        else:
            letter = "F"
        grades.append((score, letter))

    # 3. Count passing vs failing students
    passing = 0
    failing = 0
    for score in scores:
        if score >= 60:
            passing += 1
        else:
            failing += 1

    # Display results
    print(f"Class Average: {average:.2f}")
    print("-" * 25)
    for score, letter in grades:
        print(f"Score {score:>3} → Grade {letter}")
    print("-" * 25)
    print(f"Passing students: {passing}")
    print(f"Failing students: {failing}")


scores = [85, 45, 72, 90, 58, 60, 30, 77]
analyze_grades(scores)