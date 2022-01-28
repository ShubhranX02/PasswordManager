import random
import json

def generate_password(cap, num, spe):
    letters = "abcdefghijklmnopqrstuvwxyz"
    nums = '1234567890'
    spe = '!@#$%^&*'
    password = []
    for i in range(1, 11):
        password.append(random.choice(letters))
    if cap == "y":
        password[random.randrange(len(password))] = random.choice(letters).upper()
        password[random.randrange(len(password))] = random.choice(letters).upper()
    if num == "y":
        password[random.randrange(len(password))] = random.choice(nums)
        password[random.randrange(len(password))] = random.choice(nums)
    if spe == "y":
        password[random.randrange(len(password))] = random.choice(spe)
        password[random.randrange(len(password))] = random.choice(spe)

    return "".join(password)

def main():
    with open("passwords.json", "r") as f:
        data = json.load(f)
        f.close()
    use = None
    while use != "q":
        use = input("Access, Create or Quit? (a/c/q): ")
        if use == "a":
            print("All files: ")
            for key in data.keys():
                print(key)
            key = input("Which file: ")
            try: 
                print(data[key])
            except:
                print("No such file")
        elif use == "c":
            c = input("Capital Letters? (y/n): ")
            n = input("Numbers? (y/n): ")
            s = input("Special Charecters? (y/n): ")
            password = generate_password(c, n, s)
            print(f"Password: {password}")
            save = input("Save? (y/n): ")
            if save == "y":
                filename = input("Filename: ")
                data[filename] = password
                with open("passwords.json", "w") as f:
                    json.dump(data, f)

if __name__ == "__main__":
    main()