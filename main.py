
expression=""
iteration=0

while expression.lower() != "стоп":
    print("Введите выражение или слово 'СТОП' для отмены: ")
    expression = input()
    if (expression.isalnum() is not True and eval(expression)):
        iteration = iteration + 1
        print("Ответ: ", str(eval(expression)))
    else:
        print("Введено неверное выражение. Попробуйте заново или введите слово 'СТОП' для отмены")

print("Кол-во проведенных итераций: " + (str(iteration)))