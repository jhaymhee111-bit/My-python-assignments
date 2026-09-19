# Function encapsulating logic
def calculate_status(score):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"

# Iterating through a list using a loop
scores = [45, 72, 88, 30]
for score in scores:
    status = calculate_status(score)
    print(f"Score {score}: {status}")