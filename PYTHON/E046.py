import time
print("-="*50)
print("CONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFÍCIO")
print("-="*50)
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
    if c == 1:
        print("\033[1;31mBOOOOOMMMM!!!\033[m")