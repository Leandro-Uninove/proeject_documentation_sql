import re
def gerar_atributos(texto):
    lista_select = []
    lista_from = []
    lista_joins = []
    lista_where = []
    lista_group = []
    lista_having =[]
    lista_order = []
    lista_tabelas = []

    texto = texto.upper()
    sql_aux = re.sub(r"\s+", " ", texto)
    creates = re.findall(r'CREATE\s+TABLE\s+([\w|\.]+)\s+AS\s+(.*?)(?:;|$)', sql_aux)
    qtd_tabelas = len(creates)

    for creacao in range(0,qtd_tabelas):
        sql = creates[creacao][1]
        lista_tabelas.append(creates[creacao][0])
        
        clauses = [
            {"name": "SELECT", "regex": r"SELECT\s+(.*)\s*FROM"},
            {"name": "FROM", "regex": r"FROM\s+(.*?)\s*(?:WHERE|GROUP\sBY|HAVING|ORDER\sBY|;|$)"},
            {"name": "WHERE", "regex": r"WHERE\s+(.*?)\s*(?:GROUP\sBY|ORDER\sBY|HAVING|;|$)"},
            {"name": "GROUP BY", "regex": r"GROUP BY\s+(.*?)\s*(?:ORDER\sBY|HAVING|;|$)"},
            {"name": "HAVING", "regex": r"HAVING\s+(.*?)\s*(?:ORDER BY|;|$)"},
            {"name": "ORDER BY", "regex": r"ORDER BY\s*(.*)"}
        ]

        sql_dict = {}

        for clause in clauses:
            try:
                match = re.search(clause["regex"], sql, re.DOTALL)
                if match:
                    clause_value = match.group(1).split(',')
                    sql_dict[clause["name"].lower()] = clause_value
            except re.error:
                print("Erro:", clause["name"])

       
        atributos_select = sql_dict["select"]

        if 'group by' in sql_dict:
            atributos_groupby = sql_dict["group by"]
            atributos_groupby = [item.strip() for item in atributos_groupby]
        else: 
            atributos_groupby = []
            
        if "order by" in sql_dict:
            atributos_orderby = sql_dict["order by"]
            atributos_orderby = [item.strip() for item in atributos_orderby]
        else:
            atributos_orderby = []
        
        #### TRATA O FROM #########

        txt_from  = sql_dict["from"][0].upper()

        joins = re.findall(r'(INNER|FULL|LEFT|RIGHT)?\s*JOIN\s+(\w+)\s+(\w*)\s+ON\s+([\w|\.]+\s+=\s+[\w|\.]+)', txt_from)
        exit_joins = []

        for join in joins:
            exit_joins.append(join[1:])

        table_princ = re.findall(r'([\w|\.]+)\s*(\w?)\s*(INNER|FULL|LEFT|RIGHT|WHERE|GROUP\sBY|ORDER\sBY|HAVING)?',txt_from)[0]
        atributos_from = list(table_princ)
        atributos_from.pop(2)
        atributos_from.append('principal')
        atributos_joins = exit_joins


        ###### TRATANDO WHERE E HAVING ########
        if 'where' in sql_dict:
            atributos_where  = sql_dict["where"][0].upper()
            atributos_where = re.split(r"OR|AND",atributos_where)
        else:
            atributos_where = []

        if 'having' in sql_dict:
            atributos_having  = sql_dict["having"][0].upper()
            atributos_having = re.split(r"OR|AND",atributos_having)
        else:
            atributos_having = []


        aux_from = list(atributos_joins)
        aux_from.append(tuple(atributos_from))

        
        lista_select.append(atributos_select)
        lista_from.append(atributos_from)
        lista_joins.append(aux_from)
        lista_where.append(atributos_where)
        lista_group.append(atributos_groupby)
        lista_having.append(atributos_having)
        lista_order.append(atributos_orderby)
    return lista_tabelas,lista_select,lista_from,lista_joins,lista_where,lista_group,lista_having,lista_order