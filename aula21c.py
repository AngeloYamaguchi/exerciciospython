def tester(b):
    global a
    a = 7
    b += 3
    c = 5
    print(f"O A dentro recebe {a} ")
    print(f'O B  dentro recebe {b}')
    print(f' O C dentro recebe {c}')


a = 3
tester(a)
print(f'O a fora vale {a}')
