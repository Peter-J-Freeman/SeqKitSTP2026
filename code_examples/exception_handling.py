import random

print("🎲 Welcome to the 'What Could Possibly Go Wrong?' simulator!")

try:
    # Randomly pick a situation
    chaos = random.choice(["number", "zero", "string", "missing"])

    if chaos == "number":
        result = 10 / 2
        print(f"✅ Smooth sailing! Result is {result}")

    elif chaos == "zero":
        result = 10 / 0  # Will raise ZeroDivisionError

    elif chaos == "string":
        number = int("not_a_number")  # Will raise ValueError

    elif chaos == "missing":
        print(undefined_variable)  # Will raise NameError

except ZeroDivisionError:
    print("🚫 You tried to divide by zero... even the universe said 'nope'.")

except ValueError:
    print("🔤 That wasn't a number! The calculator is judging you silently.")

except NameError:
    print("👻 That variable doesn't exist... it’s a ghost!")

except Exception as e:
    print(f"🤷 Something weird happened: {e}")

else:
    print("🎉 No errors! You broke the chaos cycle!")
    print("Take a moment to feel proud 😌")

finally:
    print("🧹 Cleaning up... because life moves on regardless of your bugs.")
