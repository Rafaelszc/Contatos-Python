# Contatos usando Python: customtkinter + sqlite3
Utilizando da biblioteca "customtkinter" e "sqlite3" criei uma interface que permite a criação e pesquisa de nomes, números e descrições. Semelhante ao aplicativo de contatos que há nos celulares.

### Criação de um número
![criacao1](https://github.com/Rafaelszc/Contatos-Python/blob/main/resources/images/gif1.gif?raw=true)

Há também a possibilidade de criar mais de um número associado a um mesmo nome e com descrições diversas.

![criacao2](https://github.com/Rafaelszc/Contatos-Python/blob/main/resources/images/gif2.gif?raw=true)

### Pesquisa

Com um sistema de pesquisa é possivel achar um determinado número pelo seu nome e/ou número.

![pesquisa](https://github.com/Rafaelszc/Contatos-Python/blob/main/resources/images/gif3.gif?raw=true)

## Interface

No código a interface é dividida em "principal", "frame1", "frame2", "frame3" e "tela2"

![interface](https://github.com/Rafaelszc/Contatos-Python/blob/main/resources/images/interface.gif?raw=true)

## Sqlite3

A biblioteca sqlite3 trabalha como a aplicação do banco de dados do programa. 
Na sua estrutura há três tabelas "nomes" (id, nome), "descs" (id, desc), "numeros" (id, numero, id_nome, id_desc)
A interação de três tabelas diferentes permite a criação de diversos números ligados ao mesmo nome.
Os nomes ficam armazenados na tabela "nomes" e seu id -do tipo integer primary key- é usado como ponto de referência na tabela "numeros" no campo "id_nome". O mesmo acontece para a interação entre a tabela "descs" e a tabela "numeros".
Então, se na tabela "nomes" o nome "Rafael" tiver id = 1, para criar outro número associado ao nome "Rafael", basta definir no campo numeros.id_nome = 1

### Tabela "nomes"
![tabelaNomes](https://github.com/Rafaelszc/Contatos-Python/blob/main/resources/images/tabelaNomes.png?raw=true)
### Tabela "numeros"
![tabelaNumeros](https://github.com/Rafaelszc/Contatos-Python/blob/main/resources/images/tabelaNumeros.png?raw=true)
### Tabela "descs"
![tabelaDescs](https://github.com/Rafaelszc/Contatos-Python/blob/main/resources/images/tabelaDescs.png?raw=true)

