from raspador import Raspador

# Objecto para raspagem
amazon_raspador = Raspador(numero_paginas=1)
#Soup das páginas
soup_paginas = amazon_raspador.raspa_pagina()
#Raspagem de dados
dados = amazon_raspador.raspa_dados(soup_paginas)
#Criação de dicionário
dados_df = amazon_raspador.cria_dicionario(dados)
# Tratamento strings
dados_df = amazon_raspador.tratamento_string(dados_df)
# Para df
df = amazon_raspador.para_pandas(dados_df,'amazon.csv')





