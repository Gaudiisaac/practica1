name=["luis","javier","aldo","aljandro"]
print name
name.insert(1,"edgar")
print name
name.append("dariana")
print name
name.insert(4,"aldair")
print name
name.append(["alberto","abigail"])
print name
name.insert(7,"margarita")
print name

"""mensaje para amigos"""
print (name[0]+' amigo ya bañate')
print (name[1]+' todos sabemos que te gusta ')
print (name[2]+' ya pagame')
print (name[3]+' ¿por qué ya casi no vienes?')
print (name[5]+' me caes mal')
print (name[7]+' eres la niña de mis ojos')
print (name[6]+' Te amo <3')

Deseos=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in Deseos: 
    if i==1:
        print 'Deseo',i,': aprender programacion'
    elif i==2:
        print 'Deseo',i,':aprender ingles'
    elif i==3:
        print 'Deseo',i,': mejorar mi promedio'
    elif i==4:
        print 'Deseo',i,': ver mas a mis mascotas'
    elif i==5:
        print 'Deseo',i,': mejorar mi velocidad de calculo'
    elif i==6:
        print 'Deseo',i,': ver mas a mis amigos'
    elif i==7:
        print 'Deseo',i,': pasar mas tiempo con mi novia'
    elif i==8:
        print 'Deseo',i,': practicar mas deporte'
    elif i==9:
        print 'Deseo',i,': pasar mi materia de recurse'
    elif i==10:
        print 'Deseo',i,': comprar una computadora mejor'
    elif i==11:
        print 'Deseo',i,': alimentarme mejor'
    elif i==12:
        print 'Deseo',i,': aprender bien las bases de fisica '
    elif i==13:
        print 'Deseo',i,': no reprobar materias'
    elif i==14:
        print 'Deseo',i,': salir mas'
    else:
        print 'Deseo',i,': mejorar mis habitos de sueño'
        