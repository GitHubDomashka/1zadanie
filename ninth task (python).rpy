x=input("Введите численное значение")
y=input("Текущая величина(Неделя,Сутки,Час)")
z=input("Во что конвертировать(Неделя,Сутки,Час)")

if y=="Неделя":
    if z=="Неделя":
        print(x)
    else:
        pass

    if z=="Сутки":
        print(x*7)
    else:
        pass
 
    if z=="Час":
        print(x*168)
    else:
        pass
else:
    pass


if y=="Сутки":
    if z=="Неделя":
        print(float(x)/7)
    else:
        pass
    
    if z=="Сутки":
        print(x)
    else:
        pass
 
    if z=="Час":
        print(x*24)
    else:
        pass
else:
    pass     


if y=="Час":
    if z=="Неделя":
        print(x/168)
    else:
        pass
    
    if z=="Сутки":
        print(x/24)
    else:
        pass
 
    if z=="Час":
        print(x)
    else:
        pass
else:
    pass
