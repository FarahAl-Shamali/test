# q1
my_list=["Tarteel","Asmaa","Ahmed"]
my_list.insert(0,"Sabrin")           # add an item at the
print(my_list)
my_list.pop()        # removes the last item and returns its value
print(my_list)
my_list.append("Hamda")
print(my_list)
del my_list[2]                     # or use my_list.remove("Asmaa")
print(my_list)


# Q2
print()
print("______________________")
friends = ["Adel","Ahmed"]
employees = ["Samah","Amjad"]
school = ["Ali","Basma"]
employees.extend(school)
friends.extend(employees)
print(friends)


# Q3
print()
print("______________________")
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)




# Q4
print()
print("______________________")
my_dict={}
s=1
for a in range(1,16):
   for n in range(1,3):
       s*=a
       n+=1
   my_dict[a]=s
   s=1
   a+=1
print(my_dict)



# Q5
print()
print("______________________")
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 150, 'b': 200, 'd': 400}
new_dic={}
for k in d1:
    for k2 in d2:
        if k==k2:
           new_dic[k]=d1[k]+d2[k2]
        else:
            new_dic[k]=d1[k]
            new_dic[k2]=d2[k2]

print(new_dic)


# Q6
print()
print("______________________")
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
d5={}
for v in range(len(keys)):
    d5.update({keys[v]:values[v]})


print(d5)




# Q7
print()
print("______________________")
sampleDict= {
    "class": {
          "student": {
              "name": "Mike",
              "marks": {
                   "physics": 70,
                   "history": 80
               }

          }
    }
}
print(sampleDict['class']['student']['marks']['history'])



# Q8
print()
print("______________________")
myDict= {1: "Alaa", 5: "Hadeel", 7:"Hanin", 13: "Malak"}
a=''
for i in myDict:
    if i<10:
        a+=myDict[i]+"->"
print(a)









echo "# test" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/FarahAl-Shamali/test.git
git push -u origin main