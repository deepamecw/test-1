try:
    f = open("C:\Users\User\myworkspace\text.txt")
except FileNotFoundError:
    print("file not found")
else:
    print(f.read())
