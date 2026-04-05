from email import message

name = input("Introducing your name: ")
year_experience = int(input("Introducing your year experience: "))
skills = input("Introducing your skills: ")
message = ''

skills = skills.split(',')
skills = 'Python' or "Django" in skills




if skills and year_experience <= 3  :
    message = "Candidato optimo"
elif skills and year_experience <= 2 :
    message = "Buen Candidato"
elif skills:
    message = "posible candidato"
else:
    message = "CV Guardado"


print(message)
























