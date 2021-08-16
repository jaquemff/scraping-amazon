from bs4 import BeautifulSoup
import requests
import pandas as pd

class Raspador():
    def __init__(self, numero_paginas):
        self.numero_paginas = numero_paginas

    def raspa_pagina(self):
        soup_paginas = list()

        request = requests.get('https://www.amazon.com.br/s?k=iphone&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2')
        conteudo = request.content
        soup = BeautifulSoup(conteudo, features="html.parser")
        soup_paginas.append(soup)

        return soup_paginas

    def raspa_dados(self, soup_paginas):

        nomes =list()
        precos = list()

        for i in range(len(soup_paginas)):
            for d in soup_paginas[i].findAll('div', attrs={'class': 's-expand-height s-include-content-margin s-border-bottom s-latency-cf-section'}):
                #Nome do livro
                nome = d.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
                #Preço do livro
                preco = d.find('span', attrs={'class':'a-price-whole'})

                if nome is not None:
                    nomes.append(nome.text)
                else:
                    nomes.append('nan')
                if preco is not None:
                    precos.append(preco.text)
                else:
                    precos.append('nan')

        dados = [nomes, precos]

        return dados

    def cria_dicionario(self, dados):

        dados_df = dict()

        dados_df['nomes'] = dados[0]
        dados_df['precos'] = dados[1]

        return dados_df

    def tratamento_string(self, dados_df):

        for i in range(len(dados_df['precos'])):
            try:
                dados_df['precos'][i] = dados_df['precos'][i].split('R$')[1]
                dados_df['precos'][i] = float(dados_df['precos'][i].replace(',', '.'))
            except:
                pass

            return dados_df

    def para_pandas(self, dados_df, arquivo):
        df = pd.DataFrame(dados_df)
        df.to_csv(arquivo)

        return df








