# daily_reminder.py

# Prompt user for the task description
task = input("Enter your task: ")

# Prompt user for the priority level
priority = input("Priority (high/medium/low): ").lower()

# Prompt if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to determine reminder message based on priority
match priority:
    case "high":
        base_msg = f"Reminder: '{task}' is a high priority task"
    case "medium":
        base_msg = f"Reminder: '{task}' is a medium priority task"
    case "low":
        base_msg = f"Note: '{task}' is a low priority task"
    case _:
        base_msg = f"Note: '{task}' has an unspecified priority"

# Adjust message based on time sensitivity
if time_bound == "yes":
    if priority in ["high", "medium"]:
        print(f"{base_msg} that requires immediate attention today!")
    else:
        # For low or unspecified priority but time-bound
        print(f"{base_msg} that is time-sensitive. Consider prioritizing it.")
else:
    if priority == "low":
        print(f"{base_msg}. Consider completing it when you have free time.")
    else:
        print(base_msg + ".")
