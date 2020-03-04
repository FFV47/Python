# Na iteração de listas e tuplas, 'i' recebe o valor da estrutura. Em dicionarios 'i' recebe o valor da 'key' e não do valor.
compras = ["Manteiga", "Pao", "Carne", "Sabao"]

dici = {"nome": "Fernando", "idade": 29, "estado": "Solteiro", "altura": 1.72}

for i in compras:
    print(i)

for i in dici:
    print(i)

# um 'set' só recebe valores unicos, valores duplicados são descartados
a = set("abracadabra")
print(a)

# a função 'zip' permite a iteração de varias estruturas ao mesmo tempo. Ela cria tuplas com os items recebidos de cada estrutura
a = [1, 2, 3]
b = [4, 5, 6]
d = ["i", "j", "k"]


c = zip(a, b, d)
print(*c)


# Criação de classes


class MyClass:
    """A simple example class"""

    i = 12345

    def f(self):
        return "hello world"


print(MyClass.i)
a = MyClass.__doc__  # retorna a docstring da classe
print(a)

# A classe criada funciona como um 'tipo de objeto', como um lista ou um dicionario, logo eu posso criar varias 'MyClass' e atribuir diferentes valores a variavel interna 'i' em cada instancia
x = MyClass()
y = MyClass()

x.i = 567
print(x.i)
print(y.i)


# A função '__init__' dentro da classe é sempre chamada quando uma nova instancia é criada. Quando um 'metodo' é chamado por um objeto, esse objeto é passado como o primeiro argumento nas funções da classe, por isso a existencia do 'self' nas funções da classe


class Teste:
    def __init__(self, real=0, imag=1):
        self.r = real
        self.i = imag

    def p(self):
        return "Hello"


x = complex()
print(x)
x = Teste()
print(x.r, x.i)
# um metodo pode ser guardado em uma variavel para ser usado depois com outro nome
y = x.p
print(y())
print(Teste.p(x))  # objeto é passado como parametro para os metodo

# variavel da classe é igual para todas as instancias


class Dog:

    kind = "cachorro"

    def __init__(self, name="Bingo"):
        self.name = name
        self._semiprivate = "semi"
        self.__private = "private"


d = Dog("Bingo")
e = Dog("Suca")

print(f"{d.name} é um {d.kind}")
print(f"{e.name} é um {e.kind}")

print(d._semiprivate)


class Human:

    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by Python but that live in user-controlled
    # namespaces. Methods(or objects or attributes) like: __init__, __str__,
    # __repr__ etc. are called special methods (or sometimes called dunder methods)
    # You should not invent such names on your own.
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

        # Initialize property
        self._age = 0

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    # Another instance method
    def sing(self):
        return "yo... yo... microphone check... one two... one two..."

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method age() into an read-only attribute of the same name.
    # There's no need to write trivial getters and setters in Python, though.
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age
