<p align="center">
    <img src="https://github.com/GeeksHubsAcademy/2020-geekshubs-media/blob/master/image/logo.png" >	
</p>

    Considere el siguiente problema:

    Escriba un programa corto mediante 'recursión' para calcular la potencia de un número.

    Propiedades:
	Exponente 1, el resultado es la base.
	Exponente 0, el resultado es 1.
	Exponente 0 con base 0 es infinito.
	Exponente >=2 , el resultado es la Base por N veces el exponente.
	
    Valida:
	Exponentes positivos
	Exponentes negativos
	Base positiva
	Base negativa
    
    El resultado se debe de ser el cálculo de la operación.
    
    
    Se atiente al siguiente ejemplo:
   
    2^1 = 2
    3^1 = 3
    7^0 = 1
    8^0 = 1
    0^0 = Double.MAX_VALUE
    2^3 = 2*2*2
    
    En la carpeta 'src/kata.py' se encuentra el fichero con 
    la definición de nuestro método vacío.
    En la carpeta 'tests/test_kata.py' se encuentra el fichero con la suite de test.

    El modus operandi de trabajo es el siguiente:
    
    Debes 'forkear' el proyecto a tu cuenta.
    Puedes hacer PR's ilimitadas e ir validando poco a poco la solución contra nuestro respositorio con CI.
    Puedes trabajar en local y subir la solución haciendo un PR a nuestro repositorio.
    Cuando se envíe la PR final, debes indicar el tiempo de dedicación y los intentos que has hecho.
    También puedes añadir un comentario para dar cualquier tipo de feedback.
    
    En caso de duda, revisa en el apartado de 'Referencias'.

    tests/test_kata.py::Test_kata::test_apply_1 PASSED                       [  5%]
    tests/test_kata.py::Test_kata::test_apply_10 PASSED                      [ 11%]
    tests/test_kata.py::Test_kata::test_apply_11 PASSED                      [ 17%]
    tests/test_kata.py::Test_kata::test_apply_12 PASSED                      [ 23%]
    tests/test_kata.py::Test_kata::test_apply_13 PASSED                      [ 29%]
    tests/test_kata.py::Test_kata::test_apply_14 PASSED                      [ 35%]
    tests/test_kata.py::Test_kata::test_apply_15 PASSED                      [ 41%]
    tests/test_kata.py::Test_kata::test_apply_16 PASSED                      [ 47%]
    tests/test_kata.py::Test_kata::test_apply_17 PASSED                      [ 52%]
    tests/test_kata.py::Test_kata::test_apply_2 PASSED                       [ 58%]
    tests/test_kata.py::Test_kata::test_apply_3 PASSED                       [ 64%]
    tests/test_kata.py::Test_kata::test_apply_4 PASSED                       [ 70%]
    tests/test_kata.py::Test_kata::test_apply_5 PASSED                       [ 76%]
    tests/test_kata.py::Test_kata::test_apply_6 PASSED                       [ 82%]
    tests/test_kata.py::Test_kata::test_apply_7 PASSED                       [ 88%]
    tests/test_kata.py::Test_kata::test_apply_8 PASSED                       [ 94%]
    tests/test_kata.py::Test_kata::test_apply_9 PASSED                       [100%]


## Referencias

* [Tutorial - Testing Automatizado](https://github.com/GeeksHubsAcademy/2020-js-vanilla-testing-FFFF/blob/master/README.md)
