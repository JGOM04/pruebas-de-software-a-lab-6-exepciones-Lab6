import pytest
from Exceptions import ExceptionsDemo


@pytest.fixture
def demo():
    return ExceptionsDemo()


def salida(capsys):
    return capsys.readouterr().out


def test_divide_ok(demo, capsys):
    demo.divide(10, 2)
    assert "5.0" in salida(capsys)

def test_divide_entre_cero(demo, capsys):
    demo.divide(10, 0)          # ya no truena
    assert "dividir entre cero" in salida(capsys)

def test_divide_tipo_incorrecto(demo, capsys):
    demo.divide("10", 2)
    assert "numéricos" in salida(capsys)

def test_lista_indice_fuera_de_rango(demo, capsys):
    demo.access_list([1, 2, 3], 5)
    assert "fuera de rango" in salida(capsys)

def test_lista_no_es_lista(demo, capsys):
    demo.access_list(1, 0)
    assert "no es una lista" in salida(capsys)

def test_dict_clave_inexistente(demo, capsys):
    demo.access_dict({"a": 1}, "d")
    assert "no existe" in salida(capsys)

def test_dict_no_es_dict(demo, capsys):
    demo.access_dict("not_a_dict", "b")
    assert "no es un diccionario" in salida(capsys)

def test_archivo_no_existe(demo, capsys):
    demo.read_file("text_2.txt")
    assert "no existe" in salida(capsys)

def test_archivo_existe(demo, capsys):
    demo.read_file("text.txt")
    assert "Hola Mundo" in salida(capsys)

def test_atributo_inexistente(demo, capsys):
    demo.access_attribute(object())
    assert "no tiene ese atributo" in salida(capsys)

def test_numero_negativo(demo, capsys):
    demo.check_positive(-5)
    assert "Custom error" in salida(capsys)

def test_numero_positivo(demo, capsys):
    demo.check_positive(7)
    assert "Valid number: 7" in salida(capsys)

def test_flujo_completo_no_se_detiene(capsys):
    """Prueba de sistema: corre todo el main sin que truene."""
    import runpy
    runpy.run_path("Exceptions.py", run_name="__main__")
    assert "Fin del programa" in salida(capsys)