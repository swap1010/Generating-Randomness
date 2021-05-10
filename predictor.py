import random
import re

string = ""
capital = 1000
print('''Please give AI some data to learn...
The current data length is 0, 100 symbols left''')
while len(string) < 100:
    user = input("Print a random string containing 0 or 1:\n\n")
    for s in user:
        if s == "0" or s == "1":
            string += s
    if len(string) < 100:
        print(f"Current data length is {len(string)}, {100 - len(string)} symbols left")

print("\nFinal data string:")
print(f'{string}\n')
lst = ['000', '001', '010', '011', '100', '101', '110', '111']
my_dic_0 = {}
my_dic_1 = {}
for comb in lst:
    my_dic_0[comb] = len(re.findall(f'(?={comb}0)', string))
    my_dic_1[comb] = len(re.findall(f'(?={comb}1)', string))
cnt_0 = sum(my_dic_0.values())
cnt_1 = sum(my_dic_1.values())
print('''You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!''')
test = input(f"\nPrint a random string containing 0 or 1:\n").strip()
while test != "enough":
    if re.match('^[0-1]*$', test):
        print("prediction:")
        pred = random.choice(lst)
        for i in range(len(test) - 3):
            chunk = "".join(test[i:i + 3])
            pred += '0' if my_dic_0[chunk] > my_dic_1[chunk] else '1'
        print(pred)
        correct = 0
        wrong = 0
        for index in range(3, len(pred)):
            if test[index] == pred[index]:
                correct += 1
            else:
                wrong += 1
        total = correct + wrong
        capital -= (correct - wrong)
        print(f'\nComputer guessed right {correct} out of {total} symbols ({round(100 * correct / total, 2)} %)')
        print(f"Your capital is now ${capital}")
    test = input(f"\nPrint a random string containing 0 or 1:\n").strip()
print("Game over!")
