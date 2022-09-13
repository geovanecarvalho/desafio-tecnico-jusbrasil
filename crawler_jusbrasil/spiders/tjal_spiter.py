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
        sub_title_movimetacao = response.xpath('//*[@id="tabelaTodasMovimentacoes"]/tr/td[3]/span/text()').getall()
       
        
        data_das_movimentacao = []
        lista_title_movimentacao = []
        lista_sub_title_movimentacao = []
        

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

        yield {
            'classe': classe,
            'area': area,
            'assunto': assunto,
            'data_de_distribuicao': data_de_distribuicao,
            'juiz': juiz,
            'valor_da_acao':valor_da_acao,
            'partes_do_processo': partes_do_processo,
            'lista_das_movimentacao': lista_sub_title_movimentacao_01
        }

   
    

