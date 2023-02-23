import string
import random
from random import randint
"""Writ a function which generates a six digit/character random_user_id.
  print(random_user_id());
  '1ee33d'
Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input().
 One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
"""

"""class RandomCodeGenerator:
    def generate_code(self):
        numero_id = int(input("Ingrese un numero de Id a generar "))
        caracteres_solicitados = int(input("y los caracteres solicitados? "))
        for rep in range(numero_id):
            # Crea una lista con todos los dígitos y caracteres mayúsculas que quieres incluir en el código aleatorio
            characters = string.digits + string.ascii_lowercase

            # Utiliza la función random.sample para elegir 6 elementos aleatorios de la lista characters
            code = random.sample(characters, caracteres_solicitados)

            # Convierta la lista de caracteres elegidos aleatoriamente en una cadena y devuélvala como resultado
            id_generada = ''.join(code)
            print(id_generada)

generator = RandomCodeGenerator()
generator.generate_code()"""


#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

class RgbColorGen:
    def rgb_color_gen(self):
        reps = 0
        colors= []
        while reps != 3:
            selected_color = random.choice(range(0, 256))
            reps = reps + 1
            colors.append(selected_color)
        print(f"los colores obtenidos son : {colors} :D")


test = RgbColorGen()
test.rgb_color_gen()


#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
# (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 
# 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

class HexaGenerator:
    def generate_code(self):
        characters = string.hexdigits

        code = random.sample(characters, 6)

        id_generada = ''.join(code)
        print(f"#{id_generada}")

generator = HexaGenerator()
generator.generate_code()

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

class ListOfRgb:
    def list_of_rgb_colors(numero):
        rgb_reps = 0 
        reps = 0
        colors=[]
        colors_container = []
        while rgb_reps != numero:
            while reps != 3:
                selected_color = random.choice(range(0, 256))
                colors.append(selected_color)
                reps = reps + 1
            else:
                # guardamos los elementos con el formato adecuado
                colors_container.append(f"rgb: {colors[-3]}, {colors[-2]}, {colors[-1]}")
                reps = 0
            rgb_reps = rgb_reps + 1
        print(f"{colors_container}")

rgb_lst = ListOfRgb
rgb_lst.list_of_rgb_colors(4)

#Write a function generate_colors which can generate any number of hexa or rgb colors.

class GenerateColors:
    def generate_colors(numero, color_type="hexa or rgb"):
        if color_type == "hexa":
            hex_reps = 0
            hex_container = []
            while hex_reps != numero:
                characters = string.hexdigits
                code = random.sample(characters, 6)
                color_generado = "".join(code)
                hex_container.append(f"#{color_generado}")
                hex_reps = hex_reps + 1 
            else:
                print(hex_container)
        elif color_type == "rgb":
            rgb_reps = 0 
            reps = 0
            colors=[]
            colors_container = []
            while rgb_reps != numero:
                while reps != 3:
                    selected_color = random.choice(range(0, 256))
                    colors.append(selected_color)
                    reps = reps + 1
                else:
                    # guardamos los elementos con el formato adecuado
                    colors_container.append(f"rgb: {colors[-3]}, {colors[-2]}, {colors[-1]}")
                    reps = 0
                rgb_reps = rgb_reps + 1
            print(f"{colors_container}")
        else:
            print("please enter a rgb or hexa argument")

hexa_gen = GenerateColors
hexa_gen.generate_colors(4, "hexa")



#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
ages = [19, 22, 24, 20, 25, 26, 24, 25, 24]
print(ages)
class ShuffleList:
    def shuffle_list(list):
        random.shuffle(list)
        print(list)
shufling = ShuffleList
shufling.shuffle_list(ages)

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

class UniqueRandoms:
    def unique_randoms(self):
        randoms_container= set()
        while len(randoms_container) != 7:

            random_number = randint(0, 10)
            randoms_container.add(random_number)
        else:
            print(f"the 7 unique items are: {randoms_container}")

unique_getter = UniqueRandoms()
unique_getter.unique_randoms()



            