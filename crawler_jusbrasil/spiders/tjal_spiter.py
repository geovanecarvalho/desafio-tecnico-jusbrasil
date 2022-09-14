import scrapy


class TjalSpiterPrimeiroGrau(scrapy.Spider):
    name = 'primeiro_grau'
    numero_processo = "0710802-55.2018.8.02.0001"
    start_urls = [f'https://www2.tjal.jus.br/cpopg/show.do?processo.codigo=01000O7550000&processo.foro=1&processo.numero={numero_processo}']


    def parse(self, response):
        classe = response.xpath('//*[@id="classeProcesso"]/text()').get()
        area = response.xpath('//*[@id="areaProcesso"]/span/text()').get()
        assunto = response.xpath('//*[@id="assuntoProcesso"]/text()').get()
        data_de_distribuicao = response.xpath('//*[@id="dataHoraDistribuicaoProcesso"]/text()').get()
        juiz = response.xpath('//*[@id="juizProcesso"]/text()').get()
        valor_da_acao = response.xpath('//*[@id="valorAcaoProcesso"]/text()').get().replace(" ", "")

        partes_autor = response.xpath('/html/body/div[2]/table[1]/tr[1]/td[2]/text()').getall()
        partes_advogado_autor = response.xpath('/html/body/div[2]/table[1]/tr[1]/td[2]/span/text()').get().strip()
        partes_re = response.xpath('/html/body/div[2]/table[1]/tr[2]/td/text()').getall()
        partes_advogados_re = response.xpath('/html/body/div[2]/table[1]/tr[2]/td/span/text()').getall()

        data = response.xpath('//*[@id="tabelaTodasMovimentacoes"]/tr/td[1]/text()').getall()
        title_movimentacao =  response.xpath('//*[@id="tabelaTodasMovimentacoes"]/tr/td[3]/text()').getall()
        title_link_movimentacao = response.xpath('//*[@id="tabelaTodasMovimentacoes"]/tr/td[3]/a/text()').getall()
        sub_title_movimetacao = response.xpath('//*[@id="tabelaTodasMovimentacoes"]/tr/td[3]/span/text()').getall()

       
        
        data_das_movimentacao = []
        lista_title_movimentacao = []
        lista_title_link_movimetacao = []
        lista_sub_title_movimentacao = []
        
        for l in title_link_movimentacao:
            lista_title_link_movimetacao.append(l.strip())

        for l in title_movimentacao:
            lista_title_movimentacao.append(l.strip().replace('\r\n', ''))

        for l in sub_title_movimetacao:
            lista_sub_title_movimentacao.append(l.strip().replace('\r\n',''))

        
        for d in data:
            data_das_movimentacao.append({"data": d.strip()})


        autor = []
        re = []
        advogados_re = []
        lista_re = []
        

        for nome in partes_advogados_re:
            advogados_re.append(nome.strip()) 
            
    
        for nome in partes_re:
            re.append(nome.strip())

        for nome in partes_autor:
            autor.append(nome.strip())
        
        autor.pop(1)

        autor[1] = partes_advogado_autor + " " + autor[1]
        re.pop(0)
        re.pop(0)
        re.pop(1)
        re.pop(2)
        re.pop(3)
        re.pop(4)

        for i in range(len(re)):
            lista_re.append(advogados_re[i] + " " + re[i])

        lista_re[0] = lista_re[0][3:]

        partes_do_processo = {'autor': autor, 'ré': lista_re}

        lista_title_movimentacao_01 = [word.strip() for word in lista_title_movimentacao if word.strip() != "" ]
        lista_sub_title_movimentacao_01 = [word.strip() for word in lista_sub_title_movimentacao if word.strip() != ""]

        data_das_movimentacao[0]['movimento'] = lista_title_movimentacao_01[0]
        data_das_movimentacao[1]['movimento'] = lista_title_movimentacao_01[1] + " " + lista_sub_title_movimentacao_01[0]
        data_das_movimentacao[2]['movimento'] = lista_title_movimentacao_01[2] + " " + lista_sub_title_movimentacao_01[1]
        data_das_movimentacao[3]['movimento'] = lista_title_movimentacao_01[3] + " " + lista_sub_title_movimentacao_01[2]
        data_das_movimentacao[4]['movimento'] = lista_title_movimentacao_01[4] + " " + lista_sub_title_movimentacao_01[3]
        data_das_movimentacao[5]['movimento'] = lista_title_movimentacao_01[5] + " " + lista_sub_title_movimentacao_01[4]
        data_das_movimentacao[6]['movimento'] = lista_title_movimentacao_01[6] + " " + lista_sub_title_movimentacao_01[5]
        data_das_movimentacao[7]['movimento'] = lista_title_movimentacao_01[7] + " " + lista_sub_title_movimentacao_01[6]
        data_das_movimentacao[8]['movimento'] = lista_title_movimentacao_01[8] + " " + lista_sub_title_movimentacao_01[7]
        
        data_das_movimentacao[9]['movimento'] = lista_title_link_movimetacao[0] + " " + lista_sub_title_movimentacao_01[8]
        
        data_das_movimentacao[10]['movimento'] = lista_title_movimentacao_01[9] + " " + lista_sub_title_movimentacao_01[9]
        data_das_movimentacao[11]['movimento'] = lista_title_movimentacao_01[10] + " " + lista_sub_title_movimentacao_01[10]
        data_das_movimentacao[12]['movimento'] = lista_title_movimentacao_01[11] + " " + lista_sub_title_movimentacao_01[11]
        data_das_movimentacao[13]['movimento'] = lista_title_movimentacao_01[12] + " " + lista_sub_title_movimentacao_01[12]
        data_das_movimentacao[14]['movimento'] = lista_title_movimentacao_01[13] + " " + lista_sub_title_movimentacao_01[13]
        data_das_movimentacao[15]['movimento'] = lista_title_movimentacao_01[14] + " " + lista_sub_title_movimentacao_01[14]
        data_das_movimentacao[16]['movimento'] = lista_title_movimentacao_01[15] + " " + lista_sub_title_movimentacao_01[15]
        data_das_movimentacao[17]['movimento'] = lista_title_movimentacao_01[16] + " " + lista_sub_title_movimentacao_01[16]

        data_das_movimentacao[18]['movimento'] = lista_title_link_movimetacao[1] + " " + lista_sub_title_movimentacao_01[17]

        data_das_movimentacao[19]['movimento'] = lista_title_movimentacao_01[17] 

        data_das_movimentacao[20]['movimento'] = lista_title_link_movimetacao[2] + " " + lista_sub_title_movimentacao_01[19]
        data_das_movimentacao[21]['movimento'] = lista_title_movimentacao_01[18] + " " + lista_sub_title_movimentacao_01[20]
        
        data_das_movimentacao[22]['movimento'] = lista_title_movimentacao_01[19]

        data_das_movimentacao[23]['movimento'] = lista_title_link_movimetacao[3] + " " + lista_sub_title_movimentacao_01[21]

        data_das_movimentacao[24]['movimento'] = lista_title_movimentacao_01[20] + " " + lista_sub_title_movimentacao_01[22]
        data_das_movimentacao[25]['movimento'] = lista_title_movimentacao_01[21] + " " + lista_sub_title_movimentacao_01[23]
        data_das_movimentacao[26]['movimento'] = lista_title_movimentacao_01[22] + " " + lista_sub_title_movimentacao_01[24]
        data_das_movimentacao[27]['movimento'] = lista_title_movimentacao_01[23]
        data_das_movimentacao[28]['movimento'] = lista_title_movimentacao_01[24] + " " + lista_sub_title_movimentacao_01[25]
        data_das_movimentacao[29]['movimento'] = lista_title_movimentacao_01[25] + " " + lista_sub_title_movimentacao_01[26]
        data_das_movimentacao[30]['movimento'] = lista_title_movimentacao_01[26] + " " + lista_sub_title_movimentacao_01[27]
        data_das_movimentacao[31]['movimento'] = lista_title_movimentacao_01[27] + " " + lista_sub_title_movimentacao_01[28]

        data_das_movimentacao[32]['movimento'] = lista_title_link_movimetacao[4] + " " + lista_sub_title_movimentacao_01[29]

        data_das_movimentacao[33]['movimento'] = lista_title_movimentacao_01[28] + " " + lista_sub_title_movimentacao_01[30]
        data_das_movimentacao[34]['movimento'] = lista_title_movimentacao_01[29] + " " + lista_sub_title_movimentacao_01[31]
        data_das_movimentacao[35]['movimento'] = lista_title_movimentacao_01[30] + " " + lista_sub_title_movimentacao_01[32]
        data_das_movimentacao[36]['movimento'] = lista_title_movimentacao_01[31] + " " + lista_sub_title_movimentacao_01[33]

        data_das_movimentacao[37]['movimento'] = lista_title_link_movimetacao[5] + " " + lista_sub_title_movimentacao_01[34]
        data_das_movimentacao[38]['movimento'] = lista_title_movimentacao_01[32] + " " + lista_sub_title_movimentacao_01[36]
        data_das_movimentacao[39]['movimento'] = lista_title_movimentacao_01[33] + " " + lista_sub_title_movimentacao_01[37]
        data_das_movimentacao[40]['movimento'] = lista_title_movimentacao_01[34]
        data_das_movimentacao[41]['movimento'] = lista_title_movimentacao_01[35]

        data_das_movimentacao[42]['movimento'] = lista_title_link_movimetacao[5] + " " + lista_sub_title_movimentacao_01[38]

        data_das_movimentacao[43]['movimento'] = lista_title_movimentacao_01[36] + " " + lista_sub_title_movimentacao_01[39]
        data_das_movimentacao[44]['movimento'] = lista_title_movimentacao_01[37] + " " + lista_sub_title_movimentacao_01[40]
        data_das_movimentacao[45]['movimento'] = lista_title_movimentacao_01[38] + " " + lista_sub_title_movimentacao_01[41]
        data_das_movimentacao[46]['movimento'] = lista_title_movimentacao_01[39] + " " + lista_sub_title_movimentacao_01[42]

        data_das_movimentacao[47]['movimento'] = lista_title_link_movimetacao[6] + " " + lista_sub_title_movimentacao_01[43]
        
        data_das_movimentacao[48]['movimento'] = lista_title_movimentacao_01[40] + " " + lista_sub_title_movimentacao_01[44]
        data_das_movimentacao[49]['movimento'] = lista_title_movimentacao_01[41] + " " + lista_sub_title_movimentacao_01[45]
        data_das_movimentacao[50]['movimento'] = lista_title_movimentacao_01[42] + " " + lista_sub_title_movimentacao_01[46]
        data_das_movimentacao[51]['movimento'] = lista_title_movimentacao_01[43] + " " + lista_sub_title_movimentacao_01[47]
        data_das_movimentacao[52]['movimento'] = lista_title_movimentacao_01[44] + " " + lista_sub_title_movimentacao_01[48]
        data_das_movimentacao[53]['movimento'] = lista_title_movimentacao_01[45] + " " + lista_sub_title_movimentacao_01[49]

        data_das_movimentacao[54]['movimento'] = lista_title_link_movimetacao[8] + " " + lista_sub_title_movimentacao_01[50]
        data_das_movimentacao[55]['movimento'] = lista_title_link_movimetacao[9] + " " + lista_sub_title_movimentacao_01[51]
        
        data_das_movimentacao[56]['movimento'] = lista_title_movimentacao_01[46] + " " + lista_sub_title_movimentacao_01[52]

        data_das_movimentacao[57]['movimento'] = lista_title_link_movimetacao[10] + " " + lista_sub_title_movimentacao_01[53]

        data_das_movimentacao[58]['movimento'] = lista_title_movimentacao_01[47]
        data_das_movimentacao[59]['movimento'] = lista_title_movimentacao_01[48]
        data_das_movimentacao[60]['movimento'] = lista_title_movimentacao_01[49]

        
        yield {
            'classe': classe,
            'area': area,
            'assunto': assunto,
            'data_de_distribuicao': data_de_distribuicao,
            'juiz': juiz,
            'valor_da_acao':valor_da_acao,
            'partes_do_processo': partes_do_processo,
            'lista_das_movimentacao': data_das_movimentacao
        }
       
   
    

