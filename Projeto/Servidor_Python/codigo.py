from gerar_doc import criar_doc


arquivo = open('Codigo_sql.txt', 'r')
texto = arquivo.read()
arquivo.close()

criar_doc(texto)