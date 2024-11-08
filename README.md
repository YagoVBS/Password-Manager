# Password-Manager

Este projeto é um Gerenciador de Senhas Seguras desenvolvido para converter senhas comuns em senhas criptografadas, garantindo a segurança e a integridade dos dados armazenados.

# Descrição

O Password Manager armazena as senhas em um banco de dados com criptografia avançada, protegendo os dados de acesso de maneira confiável. As senhas só podem ser recuperadas utilizando um token primário, o que proporciona um nível adicional de segurança para o usuário.

# Funcionalidades

Criptografia de Senhas: As senhas são criptografadas antes de serem salvas no banco de dados.

Recuperação Segura: Somente o token primário pode recuperar a senha criptografada.

Armazenamento Seguro: Todas as senhas são armazenadas em um banco de dados seguro.

# Como Utilizar
Insira o dominio para ser armazenado no arquivo txt

Insira a senha comum para ser criptografada.

Use o token primário para recuperar a senha quando solicitado.

# Tecnologias Utilizadas
100% - Python

Banco de Dados (Password.txt)

Biblioteca de Criptografia (cryptography)

# Instalação e Execução
Clone este repositório.

bash

git clone https://github.com/YagoVBS/Password-Manager.git

Instale a biblioteca -> pip install cryptography

Execute o projeto -> python3 templates\templates.py

# Contribuições
Sinta-se à vontade para contribuir com melhorias, relatando problemas ou enviando pull requests.
