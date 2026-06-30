# Mauricio | Lab 5 | Intro to Python

# Ticket 1
# PREDICT: Ages 17, 25, and 13 will get Access granted. Ages 11 and 9 will get Too young.
# EXPLAIN: The variable age stores one value from the ages list each time the loop runs.

print("Ticket 1")

ages = [17, 11, 25, 13, 9]

for age in ages:
    if age >= 13:
        print(f"{age} — Access granted ✅")
    else:
        print(f"{age} — Too young ❌")

print()


# Ticket 2
# PREDICT: If the user types "no" on the first check, the loop still runs once because keep_checking starts as "yes".
# EXPLAIN: A while loop is useful because we do not know ahead of time how many ages the user wants to check.

print("Ticket 2")

keep_checking = "yes"

while keep_checking == "yes":
    age = int(input("Enter an age: "))

    if age >= 13:
        print("Access granted ✅")
    else:
        print("Too young ❌")

    keep_checking = input("Check another age? (yes/no): ")

print()


# Ticket 3
# PREDICT: Without break, the loop would continue forever and never stop.
# EXPLAIN: Ticket 2 uses a condition to control the loop. Ticket 3 uses while True and exits with break.

print("Ticket 3")

while True:
    age_input = input("Enter an age or type 'stop': ")

    if age_input == "stop":
        break

    age = int(age_input)

    if age >= 13:
        print("Access granted ✅")
    else:
        print("Too young ❌")

print()


# Ticket 4
# PREDICT: The output will be the same as Ticket 1.
# EXPLAIN: The function lets us reuse the age-checking code instead of rewriting it.

print("Ticket 4")

def can_access(age):
    return age >= 13

ages = [17, 11, 25, 13, 9]

for age in ages:
    if can_access(age):
        print(f"{age} — Access granted ✅")
    else:
        print(f"{age} — Too young ❌")

print()


# Ticket 5
# PREDICT:
# --- StreamPass Signup Report ---
# Signup #1 | Age 22 — Access granted ✅
# Signup #2 | Age 10 — Too young ❌
# Signup #3 | Age 15 — Access granted ✅
# Signup #4 | Age 8 — Too young ❌
# Signup #5 | Age 19 — Access granted ✅
# Signup #6 | Age 13 — Access granted ✅
# Approved: 4 out of 6
#
# EXPLAIN: This function uses functions, parameters, return values, loops, conditionals, variables, counters, and enumerate().

print("Ticket 5")

def signup_report(ages):
    approved = 0

    print("--- StreamPass Signup Report ---")

    for number, age in enumerate(ages, start=1):
        if can_access(age):
            print(f"Signup #{number} | Age {age} — Access granted ✅")
            approved += 1
        else:
            print(f"Signup #{number} | Age {age} — Too young ❌")

    print(f"Approved: {approved} out of {len(ages)}")

signups = [22, 10, 15, 8, 19, 13]
signup_report(signups)
