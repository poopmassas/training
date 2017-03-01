pau = 0
loop_pau= True

while loop_pau:
    pau += 1
    if pau < 10:
    	print ("Hoje não bebo")
    if 10 <= pau < 20:
    	print ("Eu disse que não ia beber")

    if 20 <= pau < 25:
    	print("Onde há mais bebida, ainda tenho sede")

    if 25 <= pau < 75:
    	print(".")

    if 75 <= pau < 78:
    	print("Que aconteceu ontem?? Não me lembro de nada")

    if pau >= 78:
    	loop_pau = False