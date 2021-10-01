number = int(input())
message = ""

if number < 1:
    message = "no army"
elif 1 <= number <= 9:
    message = "few"
elif 10 <= number <= 49:
    message = "pack"
elif 50 <= number <= 499:
    message = "horde"
elif 500 <= number <= 999:
    message = "swarm"
elif number >= 1000:
    message = "legion"
    
print(message)
