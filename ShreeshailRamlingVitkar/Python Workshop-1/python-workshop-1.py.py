import os
from datetime import datetime, date
from dataclasses import replace
# Q1
list1 = [23, 67, 45, 9, 256, 11, 99]
print("______________________Q-1__________________________")
# remove using index
print(list1)
list1.remove(256)
list1.append(256)
list1.insert(2, 256)
print("Q-1:-  ", list1)

# Q2
list2 = [11, 45, 8, 11, 40, 45, 23, 45, 40, 11, 11]
count_dict = dict()
for item in list2:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print("______________________Q-2__________________________")
print("Original List", list2)
print("Count  ", count_dict)

# Q-3
print("______________________Q-3__________________________")
def function1(a, b, c):
    print(a)
    print(b)
    print(c)
# use *args
function1(5, 15, 25)


# Q-4

set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}
print("______________________Q-4__________________________")
print(set1)
print(set2)
# Need to dry run
# print intersections too
set1, set2 = set1-set2, set2-set1
print("Updated Set 1", set1)

# Q-5
str1 = "Pandemic{}{}will{}{}end{}{}soon"
print("______________________Q-5__________________________")
print(str1.format('$', '$', '$', '$', '$', '$'))
#print(str1)
#print(str1.replace(' ', '$$'))
# try to use single bracket

# Q-6
print("______________________Q-6__________________________")
no_of_lines = " "
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
DATA_DIR = os.path.join(BASE_DIR, "workshop-1")
print(DATA_DIR)
text_file_path = os.path.join(DATA_DIR, "test.txt")
print(text_file_path)
file_ = open(text_file_path, "r")
lines = file_.readlines()[0:4]
print(lines)
no_of_lines = lines

file = open(text_file_path, "r")
lines1 = file.readlines()[5:7]
print(lines1)
no_of_lines = no_of_lines+lines1
print(no_of_lines)

# Write no_of_lines to new file


print("___________________________________________________")
# Q-7
print("______________________Q-7__________________________")
with open(text_file_path, 'r', newline="") as file_:
    first_line = file_.read(1)
    if not first_line:
        print("File is empty")
    else:
        print("File is not Empty")

# Q-8
print("______________________Q-8__________________________")
date_string = "May 21 2021 1:30PM"
print("Date String", date_string)
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print("Date Time Object",datetime_object)

# Q-9
print("______________________Q-9__________________________")
date1 = date(2019, 2, 25)
date2 = date(2020, 9, 17)
days_are = date2-date1
print(days_are.days)
# need if else for negative values

# Q-10
print("______________________Q-10__________________________")

def function2(a, b):
    def add():
        return a+b
    return add()+5

print(function2(5,5)) 

# Q-11
print("______________________Q-11__________________________")

string1 = "Cybage Software PVT. LTD"

for i in range(0, len(string1), -1):
    print(i)
