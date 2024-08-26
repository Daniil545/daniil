student=["Васичкин","Соболев","Воробев"]
marka=[5,4,3]
while True:
  answer=int(input("Ввыберите действие:\n\t1-Добавить студента\n\t2-Удалить студента по номеру\n\t3-Посмотреть список\n\t4-Удалить студента по имени\n\t0-Выход\n"))
  if answer not in[0,1,2,3,4]:
   print("Такой опирицации нет")
   continue
  elif answer==1:
    name=input("Введите фамилию:")
    student.append(name)
    mark=int(input("Введите оценку студенту:"))
    marka.append(mark)
  elif answer==2:
    index=int(input("Введите номер студента:"))
    student.pop(index-1)
    mark=int(input("Введите оценку:"))
    marka.remove(mark-1)
  elif answer == 3:
   print(student)
   i=int(input("Введите индекс студента:"))
   i -= 1
   print(student[i],marka[i])
  elif answer==4:
    name=input("Введите имя:")
    student.remove(name)
    mark=int(input("Введите оценку:"))
    marka.remove(mark)
  elif answer==0:
    break
