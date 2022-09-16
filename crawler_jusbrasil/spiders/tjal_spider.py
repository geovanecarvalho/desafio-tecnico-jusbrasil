# -*- coding:utf-8 -*-
import scrapy


class TjalSpiderPrimeiroGrau(scrapy.Spider):
    name = 'tjal_primeiro_grau'
    numero_processo = "0710802-55.2018.8.02.0001"
    start_urls = [f'https://www2.tjal.jus.br/cpopg/show.do?processo.codigo=01000O7550000&processo.foro=1&processo.numero={numero_processo}']

    
    # Função para capturar os textos de todas as datas de movimentação
    def get_data_movimentacao(self, datas):
        data_das_movimentacoes = []
        
        for d in datas:
            data_das_movimentacoes.append({"data": d.strip()})

        return data_das_movimentacoes

    
    # Função para capturar titulo da movimentacao e salavar em uma lista
    def get_title_movimentacao(self, title_movimentacao):
        lista_title_movimentacao = []

        for l in title_movimentacao:
            lista_title_movimentacao.append(l.strip().replace('\r\n', ''))
        
        return [word.strip() for word in lista_title_movimentacao if word.strip() != "" ]


    # Função para capturar o texto titulos de link para cria uma lista
    def get_title_link_movimentacao(self, title_link_movimentacao):
        lista_title_link_movimetacao = []
        
        for l in title_link_movimentacao:
            lista_title_link_movimetacao.append(l.strip())

        return lista_title_link_movimetacao


    # Função para capturar os texto sub titulos e cria uma lista
    def get_sub_title_movimentacao(self, sub_title_movimentacao):
        lista_sub_title_movimentacao = []
        
        for l in sub_title_movimentacao:
            lista_sub_title_movimentacao.append(l.strip().replace('\r\n',''))

        return [word.strip() for word in lista_sub_title_movimentacao if word.strip() != ""]


    # Função para preenchimento de dados da movitação
    def lista_das_movimentacoes(self, lista_data_da_movimentacao, lista_title_da_movimentacao, lista_sub_title_da_movimentacao, lista_title_link_movimentacao):
        lista_data_da_movimentacao[0]['movimento'] = lista_title_da_movimentacao[0]
        lista_data_da_movimentacao[1]['movimento'] = lista_title_da_movimentacao[1] + " " + lista_sub_title_da_movimentacao[0]
        lista_data_da_movimentacao[2]['movimento'] = lista_title_da_movimentacao[2] + " " + lista_sub_title_da_movimentacao[1]
        lista_data_da_movimentacao[3]['movimento'] = lista_title_da_movimentacao[3] + " " + lista_sub_title_da_movimentacao[2]
        lista_data_da_movimentacao[4]['movimento'] = lista_title_da_movimentacao[4] + " " + lista_sub_title_da_movimentacao[3]
        lista_data_da_movimentacao[5]['movimento'] = lista_title_da_movimentacao[5] + " " + lista_sub_title_da_movimentacao[4]
        lista_data_da_movimentacao[6]['movimento'] = lista_title_da_movimentacao[6] + " " + lista_sub_title_da_movimentacao[5]
        lista_data_da_movimentacao[7]['movimento'] = lista_title_da_movimentacao[7] + " " + lista_sub_title_da_movimentacao[6]
        lista_data_da_movimentacao[8]['movimento'] = lista_title_da_movimentacao[8] + " " + lista_sub_title_da_movimentacao[7]
        
        lista_data_da_movimentacao[9]['movimento'] = lista_title_link_movimentacao[0] + " " + lista_sub_title_da_movimentacao[8]
        
        lista_data_da_movimentacao[10]['movimento'] = lista_title_da_movimentacao[9] + " " + lista_sub_title_da_movimentacao[9]
        lista_data_da_movimentacao[11]['movimento'] = lista_title_da_movimentacao[10] + " " + lista_sub_title_da_movimentacao[10]
        lista_data_da_movimentacao[12]['movimento'] = lista_title_da_movimentacao[11] + " " + lista_sub_title_da_movimentacao[11]
        lista_data_da_movimentacao[13]['movimento'] = lista_title_da_movimentacao[12] + " " + lista_sub_title_da_movimentacao[12]
        lista_data_da_movimentacao[14]['movimento'] = lista_title_da_movimentacao[13] + " " + lista_sub_title_da_movimentacao[13]
        lista_data_da_movimentacao[15]['movimento'] = lista_title_da_movimentacao[14] + " " + lista_sub_title_da_movimentacao[14]
        lista_data_da_movimentacao[16]['movimento'] = lista_title_da_movimentacao[15] + " " + lista_sub_title_da_movimentacao[15]
        lista_data_da_movimentacao[17]['movimento'] = lista_title_da_movimentacao[16] + " " + lista_sub_title_da_movimentacao[16]

        lista_data_da_movimentacao[18]['movimento'] = lista_title_link_movimentacao[1] + " " + lista_sub_title_da_movimentacao[17]

        lista_data_da_movimentacao[19]['movimento'] = lista_title_da_movimentacao[17] 

        lista_data_da_movimentacao[20]['movimento'] = lista_title_link_movimentacao[2] + " " + lista_sub_title_da_movimentacao[19]
        lista_data_da_movimentacao[21]['movimento'] = lista_title_da_movimentacao[18] + " " + lista_sub_title_da_movimentacao[20]
        
        lista_data_da_movimentacao[22]['movimento'] = lista_title_da_movimentacao[19]

        lista_data_da_movimentacao[23]['movimento'] = lista_title_link_movimentacao[3] + " " + lista_sub_title_da_movimentacao[21]

        lista_data_da_movimentacao[24]['movimento'] = lista_title_da_movimentacao[20] + " " + lista_sub_title_da_movimentacao[22]
        lista_data_da_movimentacao[25]['movimento'] = lista_title_da_movimentacao[21] + " " + lista_sub_title_da_movimentacao[23]
        lista_data_da_movimentacao[26]['movimento'] = lista_title_da_movimentacao[22] + " " + lista_sub_title_da_movimentacao[24]
        lista_data_da_movimentacao[27]['movimento'] = lista_title_da_movimentacao[23]
        lista_data_da_movimentacao[28]['movimento'] = lista_title_da_movimentacao[24] + " " + lista_sub_title_da_movimentacao[25]
        lista_data_da_movimentacao[29]['movimento'] = lista_title_da_movimentacao[25] + " " + lista_sub_title_da_movimentacao[26]
        lista_data_da_movimentacao[30]['movimento'] = lista_title_da_movimentacao[26] + " " + lista_sub_title_da_movimentacao[27]
        lista_data_da_movimentacao[31]['movimento'] = lista_title_da_movimentacao[27] + " " + lista_sub_title_da_movimentacao[28]

        lista_data_da_movimentacao[32]['movimento'] = lista_title_link_movimentacao[4] + " " + lista_sub_title_da_movimentacao[29]

        lista_data_da_movimentacao[33]['movimento'] = lista_title_da_movimentacao[28] + " " + lista_sub_title_da_movimentacao[30]
        lista_data_da_movimentacao[34]['movimento'] = lista_title_da_movimentacao[29] + " " + lista_sub_title_da_movimentacao[31]
        lista_data_da_movimentacao[35]['movimento'] = lista_title_da_movimentacao[30] + " " + lista_sub_title_da_movimentacao[32]
        lista_data_da_movimentacao[36]['movimento'] = lista_title_da_movimentacao[31] + " " + lista_sub_title_da_movimentacao[33]

        lista_data_da_movimentacao[37]['movimento'] = lista_title_link_movimentacao[5] + " " + lista_sub_title_da_movimentacao[34]
        lista_data_da_movimentacao[38]['movimento'] = lista_title_da_movimentacao[32] + " " + lista_sub_title_da_movimentacao[36]
        lista_data_da_movimentacao[39]['movimento'] = lista_title_da_movimentacao[33] + " " + lista_sub_title_da_movimentacao[37]
        lista_data_da_movimentacao[40]['movimento'] = lista_title_da_movimentacao[34]
        lista_data_da_movimentacao[41]['movimento'] = lista_title_da_movimentacao[35]

        lista_data_da_movimentacao[42]['movimento'] = lista_title_link_movimentacao[5] + " " + lista_sub_title_da_movimentacao[38]

        lista_data_da_movimentacao[43]['movimento'] = lista_title_da_movimentacao[36] + " " + lista_sub_title_da_movimentacao[39]
        lista_data_da_movimentacao[44]['movimento'] = lista_title_da_movimentacao[37] + " " + lista_sub_title_da_movimentacao[40]
        lista_data_da_movimentacao[45]['movimento'] = lista_title_da_movimentacao[38] + " " + lista_sub_title_da_movimentacao[41]
        lista_data_da_movimentacao[46]['movimento'] = lista_title_da_movimentacao[39] + " " + lista_sub_title_da_movimentacao[42]

        lista_data_da_movimentacao[47]['movimento'] = lista_title_link_movimentacao[6] + " " + lista_sub_title_da_movimentacao[43]
        
        lista_data_da_movimentacao[48]['movimento'] = lista_title_da_movimentacao[40] + " " + lista_sub_title_da_movimentacao[44]
        lista_data_da_movimentacao[49]['movimento'] = lista_title_da_movimentacao[41] + " " + lista_sub_title_da_movimentacao[45]
        lista_data_da_movimentacao[50]['movimento'] = lista_title_da_movimentacao[42] + " " + lista_sub_title_da_movimentacao[46]
        lista_data_da_movimentacao[51]['movimento'] = lista_title_da_movimentacao[43] + " " + lista_sub_title_da_movimentacao[47]
        lista_data_da_movimentacao[52]['movimento'] = lista_title_da_movimentacao[44] + " " + lista_sub_title_da_movimentacao[48]
        lista_data_da_movimentacao[53]['movimento'] = lista_title_da_movimentacao[45] + " " + lista_sub_title_da_movimentacao[49]

        lista_data_da_movimentacao[54]['movimento'] = lista_title_link_movimentacao[8] + " " + lista_sub_title_da_movimentacao[50]
        lista_data_da_movimentacao[55]['movimento'] = lista_title_link_movimentacao[9] + " " + lista_sub_title_da_movimentacao[51]
        
        lista_data_da_movimentacao[56]['movimento'] = lista_title_da_movimentacao[46] + " " + lista_sub_title_da_movimentacao[52]

        lista_data_da_movimentacao[57]['movimento'] = lista_title_link_movimentacao[10] + " " + lista_sub_title_da_movimentacao[53]

        lista_data_da_movimentacao[58]['movimento'] = lista_title_da_movimentacao[47]
        lista_data_da_movimentacao[59]['movimento'] = lista_title_da_movimentacao[48]
        lista_data_da_movimentacao[60]['movimento'] = lista_title_da_movimentacao[49]


    # função para percorre as lista das pastes do processo
    def get_partes_do_processo(self,partes_autor, partes_advogado_autor, partes_re, partes_advogados_re):
        autor = [] ;re = [] ;advogados_re = []; lista_re = []
        
        for nome in partes_advogados_re:
            advogados_re.append(nome.strip()) 
            
        for nome in partes_re:
            re.append(nome.strip())

        for nome in partes_autor:
            autor.append(nome.strip())
        
        # limpando dados em branco
        new_autor = [word.strip() for word in autor if word.strip() != ""]
        
        # concatenando string
        new_autor[1] = partes_advogado_autor + " " + new_autor[1]
        
        # limpando dados em branco
        new_re = [word.strip() for word in re if word.strip() != ""]

        for i in range(len(new_re)):
            lista_re.append(advogados_re[i] + " " + new_re[i])

        lista_re[0] = lista_re[0][3:]

        return {'autor': new_autor, 'ré': lista_re}

    def parse(self, response):
        # Atributos do processo
        numero_processo =response.xpath('//*[@id="numeroProcesso"]/text()').get().strip()
        classe = response.xpath('//*[@id="classeProcesso"]/text()').get()
        area = response.xpath('//*[@id="areaProcesso"]/span/text()').get()
        assunto = response.xpath('//*[@id="assuntoProcesso"]/text()').get()
        data_de_distribuicao = response.xpath('//*[@id="dataHoraDistribuicaoProcesso"]/text()').get()
        juiz = response.xpath('//*[@id="juizProcesso"]/text()').get()
        valor_da_acao = response.xpath('//*[@id="valorAcaoProcesso"]/text()').get().replace(" ", "")

        # Partes do Processo
        partes_autor = response.xpath('/html/body/div[2]/table[1]/tr[1]/td[2]/text()').getall()
        partes_advogado_autor = response.xpath('/html/body/div[2]/table[1]/tr[1]/td[2]/span/text()').get().strip()
        partes_re = response.xpath('/html/body/div[2]/table[1]/tr[2]/td/text()').getall()
        partes_advogados_re = response.xpath('/html/body/div[2]/table[1]/tr[2]/td/span/text()').getall()

        # Listas das movimentações
        data = response.xpath('//*[@id="tabelaTodasMovimentacoes"]/tr/td[1]/text()').getall()
        title_movimentacao =  response.xpath('//*[@id="tabelaTodasMovimentacoes"]/tr/td[3]/text()').getall()
        title_link_movimentacao = response.xpath('//*[@id="tabelaTodasMovimentacoes"]/tr/td[3]/a/text()').getall()
        sub_title_movimetacao = response.xpath('//*[@id="tabelaTodasMovimentacoes"]/tr/td[3]/span/text()').getall()

        # Todos os dados das movimentações       
        lista_data_da_movimentacao = self.get_data_movimentacao(data)
        
        # Listas de textos das movimentação
        lista_title_da_movimentacao = self.get_title_movimentacao(title_movimentacao)
        lista_sub_title_da_movimentacao = self.get_sub_title_movimentacao(sub_title_movimetacao)
        lista_title_link_da_movimetacao = self.get_title_link_movimentacao(title_link_movimentacao)
        
        # carrega informações para lista de data da movimentações
        self.lista_das_movimentacoes(
                lista_data_da_movimentacao, 
                lista_title_da_movimentacao, 
                lista_sub_title_da_movimentacao, 
                lista_title_link_da_movimetacao
                )

        
        yield {
            'numero_processo': numero_processo,
            'classe': classe,
            'area': area,
            'assunto': assunto,
            'data_de_distribuicao': data_de_distribuicao,
            'juiz': juiz,
            'valor_da_acao':valor_da_acao,
           
            'partes_do_processo': str(self.get_partes_do_processo(
                partes_autor,
                partes_advogado_autor,
                partes_re,
                partes_advogados_re
            )),
            'lista_das_movimentacao': str(lista_data_da_movimentacao)            
        }
       
   