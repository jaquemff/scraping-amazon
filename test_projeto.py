import pytest
from raspador import Raspador

def test_classe_principal():
	raspador = Raspador(numero_paginas=1)
	assert type(raspador) == type(Raspador(numero_paginas=-999))

def test_listas_finais():
	raspador = Raspador(numero_paginas=1)
	soup_paginas = raspador.raspa_pagina()
	dados = raspador.raspa_dados(soup_paginas)
	dados_df = raspador.cria_dicionario(dados)
	dados_df = raspador.tratamento_string(dados_df)

	assert len(dados_df['nomes']) == 48
	assert	len(dados_df['precos']) == 48

