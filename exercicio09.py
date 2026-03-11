while True:
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    
    if usuario == "admin" and senha == "123456":
        print("Login bem-sucedido!")
        break
    else:
        print("Usuário ou senha incorretos. Tente novamente.")