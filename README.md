Este projeto utiliza Selenium WebDriver para coletar automaticamente informações de upgrades do jogo Cookie Clicker.


A classe Collector lê valores de itens como Cursor, Grandma, Factory, Mine e Shipment, além do total de dinheiro disponível no jogo.
O objetivo é capturar os preços atuais dos upgrades e manter referências aos elementos clicáveis, permitindo futuras automações de compra.
Funcionalidades
A classe Collector coleta automaticamente, ao ser instanciada:
Dinheiro atual (money)
Custo dos upgrades:
Cursor
Grandma
Factory
Mine
Shipment
Referência aos elementos clicáveis de cada item (para automação futura)
Cada método de coleta realiza:
Busca do elemento pelo ID
Extração e limpeza do texto
Conversão para inteiro
Armazenamento do valor na instância
