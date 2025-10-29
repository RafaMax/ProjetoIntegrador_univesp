from peewee import MySQLDatabase


#db = MySQLDatabase('univesp_pi.db')
#Banco de Dados Mysql online
#mysql://root:GCruUsgoPnknKFPZLewtKKWftSVPNYtD@interchange.proxy.rlwy.net:45565/railway
db = MySQLDatabase(
    'Univesp_PI1',
    user='admin',
    password='ProjetoIntegrador2',
    host='database-1.c1ioo442c1m1.us-east-2.rds.amazonaws.com',
    port=3306
)
"""CREATE TABLE itens_compra (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    compra_id INT NOT NULL,
    product_id INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    qualidade_avaliada ENUM('Ruim', 'Regular', 'Bom', 'Ótimo'),
    FOREIGN KEY (compra_id) REFERENCES compras(compra_id) ON DELETE CASCADE,
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id) ON DELETE CASCADE
);

-- Atualizar a tabela fornecedores para armazenar a média de avaliações
ALTER TABLE fornecedores ADD COLUMN avaliacao_media DECIMAL(3,2) DEFAULT 0;
"""