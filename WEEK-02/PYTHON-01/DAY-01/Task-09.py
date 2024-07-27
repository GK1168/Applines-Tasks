'''Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"]
       and the object is in ["Hockey","Football"].'''




subject = ['I','You','']
verb = ['play','Love']
object = ['Hockey','Football','']
def clearSpaces(list):
    for i in list:
        if i == '' or i == ' ':
            list.remove(i)
    return list

verb = clearSpaces(verb)
subject = clearSpaces(subject)
object = clearSpaces(object)
print(verb)

if(len(subject) == len(verb) == len(object)):
    for i in range(len(subject)):
        print(f"{subject[i]} {verb[i]} {object[i]}")
else:
    print("Lists has unmatchable no.of strings")