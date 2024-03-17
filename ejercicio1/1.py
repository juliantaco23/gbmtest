def palindrome(chain):
    return chain[::-1] == chain

# Lista de nombres de archivos de prueba
test_files = ['test_input_1.txt', 'test_input_2.txt', 'test_input_3.txt']

# Abrir archivo de salida
with open('./ejercicio1/output.txt', 'w') as output_file:
    for file_name in test_files:
        # Abrir archivo de prueba y leer el input
        with open(f'./ejercicio1/{file_name}', 'r') as test_file:
            test_input = test_file.read().strip()

        # Ejecutar la función con el input y guardar el resultado en el archivo de salida
        result = palindrome(test_input)
        output_file.write(f"Input: {test_input}, Result: {result}\n")
