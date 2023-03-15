def welcome_mas():
    mas = []
    print("input the lenght of mas")
    n = int(input())
    for i in range(n):
        print("input new element")
        mas.append(input())
    print("that is it!")
    print(*mas)
    return mas


start_mas = welcome_mas()
fin_mas = []
for i in range(len(start_mas)):
    if len(start_mas[i]) <= 3:
        fin_mas.append(start_mas[i])
print("that's what we got here:")
print(*fin_mas)
