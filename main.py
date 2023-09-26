import pandas as pd

# DEFININO COLUNAS -> EXISTE OUTRA FORMA MAS QUIS FAZER ASSIM!
columns = dict(code="codigo", brand="marca", type="tipo", category="categoria", price="preco_unitario", cost="custo", obs="obs")

# LENDO COM PANDAS CSV DE PRODUTOS
df = pd.read_csv('produtos.csv')

## Inserir dados no banco de dados relacional(SQL)
exec_query_sql='INSERT INTO product ("product_id", "brand", "type", "category", "price", "cost", "description") VALUES \n'
range_df = range(len(df))
counter=0

for indexRow in range_df:
    code =     df[columns["code"]]
    brand =    df[columns["brand"]]
    category = df[columns["category"]]
    price =    df[columns["price"]]
    cost =     df[columns["cost"]]
    obs =      str(df[columns["obs"]]) 
    if counter != len(df)-1:
        exec_query_sql+="({},{},{},{},{},{}), \n".format(
            code[indexRow],
            brand[indexRow],
            category[indexRow],
            float(price[indexRow]),
            float(cost[indexRow]),
            obs[indexRow] if obs[indexRow] == "nan" else "NULL"
        )
    else:
        exec_query_sql+="({},{},{},{},{},{});".format(
            code[indexRow],
            brand[indexRow],
            category[indexRow],
            float(price[indexRow]),
            float(cost[indexRow]),
            obs[indexRow] if obs[indexRow] == "nan" else "NULL"
        )
      
    counter=counter+1


## Salvar dados no arquivo sql para enviar ao banco de dados
bulk_insert_sql_file = open('bulk_insert_product.sql','w')
bulk_insert_sql_file.write(exec_query_sql)
bulk_insert_sql_file.close()