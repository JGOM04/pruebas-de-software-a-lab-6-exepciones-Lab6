class MyException(Exception):
    """Excepción personalizada para reglas propias del programa."""
    pass


class ExceptionsDemo:

    def divide(self, a, b):
        try:
            result = a / b
            print("Division result:", result)
        except ZeroDivisionError:
            print("Error: no se puede dividir entre cero.")
        except TypeError:
            print("Error: los valores deben ser numéricos.")

    def access_list(self, lst, index):
        try:
            print("Element:", lst[index])
        except IndexError:
            print("Error: índice fuera de rango.")
        except TypeError:
            print("Error: el objeto no es una lista o el índice no es válido.")

    def access_dict(self, dic, key):
        try:
            print("Value:", dic[key])
        except KeyError:
            print(f"Error: la clave '{key}' no existe.")
        except TypeError:
            print("Error: el objeto no es un diccionario.")

    def read_file(self, filename):
        try:
            with open(filename, "r") as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print(f"Error: el archivo '{filename}' no existe.")
        except IOError:
            print(f"Error: no se pudo leer el archivo '{filename}'.")

    def access_attribute(self, obj):
        try:
            print(obj.tnonexistent_attribue)
        except AttributeError:
            print("Error: el objeto no tiene ese atributo.")

    def check_positive(self, number):
        try:
            if number < 0:
                raise MyException("The number must be positive.")
            print("Valid number:", number)
        except MyException as e:
            print("Custom error:", e)
        except TypeError:
            print("Error: el valor debe ser numérico.")


if __name__ == "__main__":
    demo = ExceptionsDemo()

    demo.divide(10, 0)
    demo.divide("10", 2)

    demo.access_list([1, 2, 3], 5)
    demo.access_list(1, 0)

    demo.access_dict({"a": 1, "b": 2, "c": 3}, "d")
    demo.access_dict("not_a_dict", "b")

    demo.read_file("text_2.txt")
    demo.read_file("text.txt")

    demo.access_attribute(object())

    demo.check_positive(-5)

    print("Fin del programa: el flujo continuó sin detenerse.")