marks = [98, 97, 95, "man"]
print(marks)
print(marks[0])
print(marks[-1])
print(marks[0:2])
for score in marks:
    print(score)

marks.append(99)
print(marks)
marks.insert(0, 99)
print(marks)
print(99 in marks)
print(93 in marks)
print(len(marks))
#using while loop
i = 0
while i<len(marks):
    print(marks[i])
    i+=1
marks.clear()
print(marks)