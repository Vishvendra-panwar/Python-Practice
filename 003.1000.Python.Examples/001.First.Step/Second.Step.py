# We will discuss modules in this step
import sys

print ( "sys.executable = ", sys.executable)
print ( "sys.platform = ", sys.platform )
print ( "sys.argv [0] = ", sys.argv[0])
print ( "sys.version_info.manjor = ", sys.version_info.major)
print ( "sys.getsizeof (1)", sys.getsizeof(1))
print ( "sys.getsizeof (42)", sys.getsizeof(42))
print ( "sys.getsizeof(1.0)", sys.getsizeof(1.0))
print ( "sys.getsizeof("")", sys.getsizeof(""))
print ( "sys.getsizeof(\"a\")", sys.getsizeof("a"))
print ( "sys.getsizeof(\"ab\")", sys.getsizeof("ab"))
print ( "sys.getsizeof(\"Vishvendra\")", sys.getsizeof("Vishvendra"))

print ("hello")
print ("world")
print ("Foo", "Bar",)

sys.stdout.write("hello")
sys.stdout.write("world")

### Promting for user input in Python 2

def main():
    print ("We have a question!")
    name = input('Your name: ')
    print("Hello " + name + ", how are you?")
    a = input('First number: ')
    b = input("Second number: ")
    print (a + b)
    print (int(a) + int (b))
main()

a = "23"
print (a)
print (type(a))

b = int(a)
print (b)
print (type(b))