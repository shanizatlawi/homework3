##start
grade = int(input("enter your grade:"));

if 0 <= grade <= 40:
    print("try harder next time...");
elif 41 <= grade <= 60:
    print("you're getting there, need some more work")
elif 61 <= grade <= 80:
    print("good pretty")
elif 81 <= grade <= 95:
    print("awesome!")
elif 95 <= grade <= 100:
    print("excellent!!! You're a Star!")
else:
    print("grade illegal")
