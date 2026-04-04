# if - else en una sola linea
is_student = True
#
# if is_student:
#     print("Licencia de estudiante")
# else:
#     print("No estudiante")

if is_student:
     print("Licencia de estudiante")
else:
    print("No estudiante")


get_license = "Licencia de estudiante" if is_student else "No estudiante"
print(get_license)
