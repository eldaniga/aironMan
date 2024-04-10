
import compiler

while True:
    text = input("aironMan >>> ")
    result, error = compiler.run('<stdin>',text)
    
    if error: print(error.as_string())
    else:
           print(result) 