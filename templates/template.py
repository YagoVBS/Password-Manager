import sys, os

sys.path.append(os.path.abspath(os.curdir))

from models.password import Password
from views.password_views import Fernethasher

def clean_window():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def pause():
    print("\n\n")
    os.system('pause')

def menu():
    print("\n========= Menu ==========\n")
    print("1. Salvar senha")
    print("2. Verificar senha")
    print("3. Exit")
    
while True:
    clean_window()
    menu()
    
    action = input("\nDigite a opção desejada: ")    

    if action == '1':
        clean_window()
        if len(Password.get()) == 0:
            key, path = Fernethasher.create_key(archive=True)
            print('Sua chave foi criada com sucesso, salve-a em local seguro.')
            print(f'Chave: {key.decode("utf-8")}')
            
            if path:
                print('Chave salva no arquivo, lembre-se de remover o arquivo após o transferir de local')
                print(f'Arquivo criptografado salvo em: {path}')
                
        else:    
            key = input('Digite sua chave usada para criptografia, use sempre a mesma chave: ')
                    
        domain = input('Domínio: ')
        password = input('Senha: ')
        fernet_user = Fernethasher(key)
        p1 = Password(domain=domain, password=fernet_user.encrypt(password).decode('utf-8'))
        p1.save()
        print("\nDominio e Senha salvo com sucesso !")
        pause()
        
        
    elif action == '2':
        clean_window()
        domain = input('Domínio: ')
        key = input('Key: ')
        fernet_user = Fernethasher(key)
        data = Password.get()
        
        for i in data:
            if domain in i ['domain']:
                password = fernet_user.decrypt(i['password'])
                
        if password:
            print(f'Sua senha: {password}')
        else:
            print('Senha não encontrada')
        pause()  
                   
    elif action == '3':
        print("\nEncerrando ...")
        break
    else:
        print("\nOpção inválida")
        pause()