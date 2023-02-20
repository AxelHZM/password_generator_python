#!python3
import random as rd
import string
import pyperclip

digits = tuple(string.digits)
lowercase_letters = tuple(string.ascii_lowercase)
uppercase_letters = tuple(string.ascii_uppercase)
special_chars = ("!", "#", "@", "-", "=", "$", "&", "?", "*", "+")

#AxelTest

#Four functions that will each return a random character from each of the 4 lists above
# pass: tuple/list. Return: str
def give_random_char(list_of_chars):
    return rd.choice(list_of_chars)


#Main function that returns a complete password with specified parameters
def password_generator(include_digits = True, include_lowercase = True, include_uppercase = True, include_special_chars = True, length_of_password = 15):

    final_password = []

    for i in range(0, length_of_password):
        test_number = rd.randint(1, 4)

        if include_digits and test_number == 1:
            final_password.append(give_random_char(digits))

        elif include_lowercase and test_number == 2:
            final_password.append(give_random_char(lowercase_letters))

        elif include_uppercase and test_number == 3:
            final_password.append(give_random_char(uppercase_letters))

        elif include_special_chars and test_number == 4 :
            final_password.append(give_random_char(special_chars))
            
    
    return "".join(final_password)

def input_checker(input_choice):
    final_choice = True
    if input_choice == "2":
        final_choice = False
    elif input_choice != "1":
        print("Escribi una verga valida nojoda")
        final_choice = input_checker(input("Por favor escriba un número válido (1) o (2)"))
    return final_choice

#Main program line
if __name__ == "__main__":
    print("Hola. Si estas corriendo esto es porque eres marico")
    
    length_of_password = int(input("Por favor, ingrese la longitud deseada de su contraseña: "))

    include_digits = input_checker(input("Desea que su contraseña incluya caracteres numéricos?\n Escriba (1) para \"Si\"\n Escriba (2) para \"No\""))

    include_lowercase = input_checker(input("Desea que su contraseña incluya caracteres en minúscula?\n Escriba (2) para \"No\""))

    include_uppercase = input_checker(input("Desea que su contraseña incluya caracteres en mayúscula?\n Escriba (2) para \"No\""))

    include_special_chars = input_checker(input("Desea que su contraseña incluya caracteres especiales?\n Escriba (2) para \"No\""))

password = password_generator(include_digits, include_lowercase, include_uppercase, include_special_chars, length_of_password)

print(f"Se ha generado la contraseña {password}")
print("Esta contraseña se ha copiado a su \"clipboard\"")
pyperclip.copy(password)
