import time
import random

# Ask user for their name
name = input("Your name: ").title().strip()

# Split user's name into first name and last name
# first,last = name.split()


# Say hi to user
def main():
   display_text_slowly( f"Hi, {name}, Welcome!") 
    
# define a function named print_hi
#def print_hi(to):
#    print(f"Hi, {to}")

# define a fucntion to output words one by one 
def display_text_slowly(text, delay = 0.1):
    for char in text:
        print(char, end='', flush = True)
        time.sleep(delay)


main()
# ^^^^close <def main():> REALLY IMPORTANT !!!!

time.sleep(1)
display_text_slowly("\nNow you'll play \033[1;33mEduardo Saverin\033[0m.")

time.sleep(0.3)
print(
    "\n!!! <\033[1;4;31mPlease keep Caps Lock on ALL THE TIME.\033[0m> !!!"
    "\n\n\033[34mMark\033[0m SET YOU UP, and you have to make choice.\n"
)

choices = [
    "A. coming back for everything",
    "B. without him",
    "C. find a lawyer"
        ]
for choice in choices:
    sorted(choice)
    print(choice.title())
    time.sleep(0.5)

time.sleep(1)
DONT = set('qwertyuiopasdfghjklzxcvbnm')


ANSWERS = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
ANSWER = ["A", "B", "C", "AB", "AC", "CB", "BC", "CA", "BA"]
LUCKLYegg = [
    "\033[1mDo you know WHO I am?\033[0m",
    "\033[1mI'm not a bad guy, Eduardo\033[0m\n"
    "\033[1mI'm just someone who wants to help you.\033[0m",
]

while True:
    choose = input("\nYou will: ").upper().strip()

    if choose in ANSWERS:
        print("\n\033[1mAh, Brilliant.\033[0m\n")
        time.sleep(0.5)

        LEX = random.choice(LUCKLYegg)
        display_text_slowly(f"\n{LEX}")

        while LEX == LUCKLYegg[0]:
            e = input("\nDo you wanna know who I am ?  YES or NO\nEnter: ").upper().strip()

            if e not in ["YES", "!NO", "NO", "!YES"]:
                print("\nNo,no,no, you're too bad,dudu. Please, Do as I said.\n")
                continue

            elif e in ["YES", "!NO"]:
                if e == "!NO":
                    print('\033[1m"YES" you mean?\033[0m\n')
                    time.sleep(1)
                    display_text_slowly(
                        "\033[1m\nI'm glad to knew you Eduardo. Welcome to LexCorp.\n\033[0m"
                    )
                else:
                    display_text_slowly(
                        "\033[1m\nI'm glad to knew you Eduardo. Welcome to LexCorp.\n\033[0m"
                    )
                    break

            elif e in ["NO", "!YES"]:
                if e == "!YES":
                    print('\033[1mYou mean "NO"? All right.\033[0m')
                    time.sleep(1)
                    display_text_slowly(
                        "\n\033[1mAs you wish. BUT I will have time.\n\nTime, time.\033[0m\n"
                        "\033[1mThat will all blow away, like sand in the desert.\033[0m\n"
                    )
                else:
                    display_text_slowly(
                        "\n\033[1mAs you wish. BUT I will have time."
                        "\n\nTime, time.\033[0m\n"
                        "\033[1mThat will all blow away, like sand in the desert.\033[0m\n"
                    )
                break

        if LEX != LUCKLYegg[0]:
            display_text_slowly("\n\033[1mYou'll know that. Just wait.\033[0m\n")
        break

    elif choose in DONT:
        print("!!! <\033[1;4;31mPlease keep Caps Lock on ALL THE TIME.\033[0m> !!!")

    elif choose not in ANSWER and ANSWERS:
        print("Follow the rules! Darling")

    else:
        print(
            "\noh. What a shame. Do you truly think that's all? \033[1m'EVERYTHING'\033[0m ?"
        )

        egg = [
            "\033[1mYou felw too close to the sun.\033[0m",
            "\033[1mMr.Saverin, take it easy.\033[0m",
            "\033[1mI m not a bad guy, Eduardo\033[0m",
            "\033[1mI see, It'cherry.\nUnfortunately, it will be rotten.\n"
            "\n'Cause time is the most cruel thing.\033[0m",
        ]
        final_egg = ("\n", random.choice(egg))
        display_text_slowly(final_egg)
