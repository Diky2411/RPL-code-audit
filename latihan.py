data = []

def a(x):
    if x == 1:
        n = input("Masukkan catatan: ")
        data.append(n)
    elif x == 2:
        for i in range(len(data)):
            print(str(i) + data[i])
    elif x == 3:
        i = int(input("Index: "))
        del data[i]