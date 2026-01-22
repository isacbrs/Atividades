a = int(input("Digite o ano de nascimento do atleta:"))
n = 2025 - a
if n <= 9:
    print("\033[1;36mMIRIN\033[m")
elif n <= 14:
    print("\033[1;33mINFANTIL\033[m")
elif n <= 18:
    print("\033[1;34mJUNIOR\033[m") 
elif n <= 20:
    print("\033[1;35mSÊNIOR\033[m")
elif n > 20:
    print("\033[1;31mMASTER\033[m")              