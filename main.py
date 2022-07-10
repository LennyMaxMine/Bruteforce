import itertools
import string
import sys

print("")
print("  _                              _     ")
print(" | |                            | |    ")
print(" | |     __ ___  ____      _____| |__  ")
print(" | |    / _` \ \/ /\ \ /\ / / _ \ '_ \ ")
print(" | |___| (_| |>  <  \ V  V /  __/ |_) |")
print(" |______\__,_/_/\_\  \_/\_/ \___|_.__/ ")
print("                                       ")

#EULA
print("")
print("This project was created only for good purposes and personal use.")
print("By using Laxweb-Discord-Nitro-Generator, you agree that you hold responsibility and accountability of any consequences caused by your actions.")
print("Do not pass this programme off as yours. When using the programme for social media content, link my Discord profile (LennyMaxMine).")
print("By pressing Enter you agree the EULA of Laxweb-Discord-Nitro-Generator and Github-Eula.")
input("")

password = input("Password: ")
letters = string.ascii_letters + string.punctuation + string.digits

def bruteforce(password: str) -> str:
    na = 0
    for n in range(1,10):
        for test in itertools.product(letters, repeat=n):
            test = "".join(test)
            na += 1
            print(f"Trying:{test}  |  Number of trys: {na}")
            if test == password:
                print(f"Password found. Password: {test} with {na} trys.")
                return

bruteforce(password)