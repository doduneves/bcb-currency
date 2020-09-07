
# BCB Currency

Aplicação construida para acessar a API do BCB e buscar as cotações de moedas em relação ao dolar.

#### Instalação
Para executar o programa é necessário ter o python instalado em sua máquina.
Com isso, executar:

```sh
$ pip install -r requirements.txt
```

#### Execução

Para executar o programa basta rodar o comando:

```sh
$ python app.py
```
Em seguida, o programa esperara que seja inserida a data para busca da cotação no formato 'YYYYMMMDD'

APIs acessadas:
- https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$top=1000&$format=json&$select=simbolo (para buscar as moedas que existem na API)
- https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda='simbol'&@dataCotacao='quotation_date'&$top=100&$format=json&$select=cotacaoCompra (para pegar o valor de cada moeda)