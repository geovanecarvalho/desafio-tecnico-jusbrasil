# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class CrawlerJusbrasilPipeline:
    def process_item(self, item, spider):
        self.conn.execute(
            'insert into crawler(numero_processo, classe, area, assunto, data_de_distribuicao, juiz, valor_da_acao, partes_do_processo, lista_das_movimentacao) values(:numero_processo, :classe, :area, :assunto, :data_de_distribuicao, :juiz, :valor_da_acao, :partes_do_processo, :lista_das_movimentacao)', item
        )
        self.conn.commit()
        return item

    def create_table(self):
        result = self.conn.execute(
            'select name from sqlite_master where type = "table" and name = "crawler"'
        )
        try:
            value = next(result)
        except StopIteration as ex:
            self.conn.execute(
                'create table crawler(numero_processo varchar(25) primary key, classe varchar(50), area varchar(50), assunto varchar(50), data_de_distribuicao varchar(50), juiz varchar(50), valor_da_acao varchar(50), partes_do_processo text, lista_das_movimentacao text)'
            )

    def open_spider(self, spider):
        self.conn = sqlite3.connect('db.sqlite3')
        self.create_table()

    def close_spider(self, spider):
        self.conn.close()