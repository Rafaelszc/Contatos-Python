# Contatos usando Python: customtkinter + sqlite3
Utilizando da biblioteca "customtkinter" e "sqlite3" criei uma interface que permite a criação e pesquisa de nomes, números e descrições. Semelhante ao aplicativo de contatos que há nos celulares.

### Criação de um número
![criacao1](https://github.com/Rafaelszc/Contatos-Python/blob/main/fotos/gif1.gif?raw=true)

Há também a possibilidade de criar mais de um número associado a um mesmo nome e com descrições diversas.

![criacao2](https://github.com/Rafaelszc/Contatos-Python/blob/main/fotos/gif2.gif?raw=true)

### Pesquisa

Com um sistema de pesquisa é possivel achar um determinado número pelo seu nome e/ou número.

![pesquisa](https://github.com/Rafaelszc/Contatos-Python/blob/main/fotos/gif3.gif?raw=true)

## Interface

No código a interface é dividida em "principal", "frame1", "frame2", "frame3" e "tela2"

![interface](https://github.com/Rafaelszc/Contatos-Python/blob/main/fotos/interface.gif?raw=true)

## Sqlite3

A biblioteca sqlite3 trabalha como a aplicação do banco de dados do programa. 
Na sua estrutura há três tabelas "nomes" (id, nome), "descs" (id, desc), "numeros" (id, numero, id_nome, id_desc)
A interação de três tabelas diferentes permite a criação de diversos números ligados ao mesmo nome.
Os nomes ficam armazenados na tabela "nomes" e seu id -do tipo integer primary key- é usado como ponto de referência na tabela "numeros" no campo "id_nome". O mesmo acontece para a interação entre a tabela "descs" e a tabela "numeros".
Então, se na tabela "nomes" o nome "Rafael" tiver id = 1, para criar outro número associado ao nome "Rafael", basta definir no campo numeros.id_nome = 1

### Tabela "nomes"
![tabelaNomes](https://cdn.discordapp.com/attachments/715218092560613476/1214335101824016384/image.png?ex=65f8bcb1&is=65e647b1&hm=dd00c1a67c3c1179ab962027bf6321c99689a45aa36df7e7fbd5583b04ace619&)
### Tabela "numeros"
![tabelaNumeros](https://cdn.discordapp.com/attachments/715218092560613476/1214335109545852999/image.png?ex=65f8bcb3&is=65e647b3&hm=db2150b4db1caf5b9ef9ae88a17ef7f35469bcd4e26c9eb11a74eacb0e055e83&)
### Tabela "descs"
![tabelaDescs](https://cdn.discordapp.com/attachments/715218092560613476/1214335117464576020/image.png?ex=65f8bcb5&is=65e647b5&hm=a6b9052f0f2f181d7d69f3b1b133a49dbacee76dded3c74e519c7ca6db876623&)

