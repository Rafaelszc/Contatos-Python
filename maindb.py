import sqlite3

def criar(nome, numero, desc):
    conexao = sqlite3.connect('contatos.db')
    cursor = conexao.cursor()
    conexao.row_factory = sqlite3.Row
    cursor.execute('insert into nomes(nome) values(?)', ([nome]))
    resname = cursor.lastrowid
    cursor.execute('insert into descs(desc) values(?)', ([desc]))
    resdesc = cursor.lastrowid
    cursor.execute('insert into numeros(numero, id_nome, id_desc) values(?, ?, ?)', ([numero, resname, resdesc]))
    conexao.commit()
    cursor.close()
    conexao.close()

def criar_existente(nome, numero, desc):
    conexao = sqlite3.connect('contatos.db')
    cursor = conexao.cursor()
    conexao.row_factory = sqlite3.Row
    resname = cursor.execute("""select id from nomes where nome = ?""", (nome,))
    resnamedef = [*resname][0][0]
    cursor.execute('insert into descs(desc) values(?)', ([desc]))
    resdesc = cursor.lastrowid
    cursor.execute('insert into numeros(numero, id_nome, id_desc) values(?, ?, ?)', ([numero, resnamedef, resdesc]))
    conexao.commit()
    cursor.close()
    conexao.close()

def verificar(nomes, numeros, descs):
    conexao = sqlite3.connect('contatos.db')
    cursor = conexao.cursor()
    conexao.row_factory = sqlite3.Row
    if nomes == '' or numeros == '' or descs == '':
        return None
    else:
        res = cursor.execute("""select id from nomes where nome = ?""", (nomes,))
        resultado = ([*res] == [])
        if resultado == True:
            return criar(nomes, numeros, descs)
        elif resultado == False:
            return criar_existente(nomes, numeros, descs)
        cursor.close()
        conexao.close()

def mostrar(num):
    conexao = sqlite3.connect('contatos.db')
    cursor = conexao.cursor()
    conexao.row_factory = sqlite3.Row
    p = cursor.execute('select id from nomes')
    quantidade = len([*p])
    try:
        if type(num) == int:
            #selecionar os nomes e os id
            nomes = cursor.execute('select id from nomes')
            nome_id= [*nomes][num][0]
            #listagem dos nomes, numeros e tipos
            numeros = []
            tipos = []
            estruturas = []
            tudo = cursor.execute(f'select nome, numero, desc from nomes, numeros, descs where numeros.id_nome = {nome_id} and nomes.id = {nome_id} and numeros.id_desc = descs.id')
            for c in tudo:
                nome = c[0]
                numeros.append(c[1])
                tipos.append(c[2])
                estrutura = f'Número: {c[1]}\nDescrição: {c[2]}\n'
                estruturas.append(estrutura)
                numedesc = '\n \n'.join(estruturas)
            return [nome, numedesc]
        elif type(num) == str:
            return quantidade
    except:
        pass
    cursor.close()
    conexao.close()

def pesquisar(arg):
    conexao = sqlite3.connect('contatos.db')
    cursor = conexao.cursor()
    conexao.row_factory = sqlite3.Row
    try:
        try:
            id = []
            numeros = []
            estruturas = []
            tipos = []
            for q in cursor.execute('select id from nomes where nome = ?', (arg,)):
                id.append(*q)
            pesquisa_total = cursor.execute(f'select nome, numero, desc from nomes, numeros, descs where numeros.id_nome = {id[0]} and nomes.id = {id[0]} and numeros.id_desc = descs.id')
            for c in pesquisa_total:
                nome = c[0]
                numeros.append(c[1])
                tipos.append(c[2])
                estrutura = f'Número: {c[1]}\nDescrição: {c[2]}\n'
                estruturas.append(estrutura)
                numedesc = '\n \n'.join(estruturas)
            return [nome, numedesc]
        except:
            id = []
            numeros = []
            estruturas = []
            tipos = []
            for q in cursor.execute('select id_nome from numeros where numero = ?', (arg,)):
                id.append(*q)
            pesquisa_total = cursor.execute(f'select nome, numero, desc from nomes, numeros, descs where numeros.id_nome = {id[0]} and nomes.id = {id[0]} and numeros.id_desc = descs.id')
            for c in pesquisa_total:
                nome = c[0]
                numeros.append(c[1])
                tipos.append(c[2])
                estrutura = f'Número: {c[1]}\nDescrição: {c[2]}\n'
                estruturas.append(estrutura)
                numedesc = '\n \n'.join(estruturas)
            return [nome, numedesc]
    except:
        cursor.close()
        conexao.close()
        return['', 'Nada encontrado']