Usuario1 = "Rafael"
senha1 = 123
Usuario2 = "Gabriel"
senha2 = 1234
Usuario3 = "Marcia"
senha3 = 123456
tentativas = 0
limite = 3

user = input("informe o seu nome de usuario: ")
userT = user.title()

while tentativas < limite:
    if userT == Usuario1:
        password = int(input("Informe sua senha: "))
        if password == senha1:
            print("✅ Login bem-sucedido!")
            break
        else:
            print("❌ Senha incorreta!")
            tentativas += 1

    elif userT == Usuario2:
        password = int(input("Informe sua senha: "))
        if password == senha2:
            print("✅ Login bem-sucedido!")
            break
        else:
            print("❌ Senha incorreta!")
            tentativas += 1

    elif userT == Usuario3:
        password = int(input("Informe sua senha: "))
        if password == senha3:
            print("✅ Login bem-sucedido!")
            break
        else:
            print("❌ Senha incorreta!")
            tentativas += 1

    else:
        print("❌ Usuário não encontrado!")
        break

if tentativas == limite:
    print("⛔ Número máximo de tentativas alcançado. Acesso bloqueado.")