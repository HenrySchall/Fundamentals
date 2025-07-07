# Google Cloud Plataform
> Plataforma de computação em nuvem do Google, que oferece centenas de serviços e produtos para desenvolvimento, armazenamento, análise de dados, inteligência artificial, redes, segurança, entre outros.

### Principais Produtos 
- Compute Engine -> Criar Máquina Virtual.
- Vertex AI -> Treinar e hopedar modelos de Machineee Learning.
- Cloud SQL -> Criar Banco de Dados.
- Big Query -> Analisar e Gerenciar dados.
- Dataproc -> Criar Clusters (Hadoop, Spark, Kubernetes).
- Text-to-Speech -> Converter texto em voz
- Speech-to-Text -> Converter voz em texto
- Cloud Vision -> Detectar objetos em imagens.
- Cloud Vision Intelligence -> Detectar objetos em videos.
- Cloud Translation -> Tradução de texto
- Looker -> Criar Dashboards.
- Anthos -> Modenizar e executar Apps.
- Firebase -> Desenvolver Web Apps ou Mobile Apps.
- Cloud Run -> Implementar Apps.
- Cloud Storage -> Bucket de armazenamento. 

![Img_1](https://github.com/user-attachments/assets/97261076-45b9-4aba-af90-29d9a24ea674)

## Big Query
> BigQuery é um serviço da Google Cloud que funciona como um data warehouse na nuvem, ou seja, armazena grandes volumes de dados organizados.

### Realizando Consultas

```
Select *
From 'projeto.conjunto_de_dados.tabela' -- LIMIT 10
```

```
SELECT DISTINCT
  First-nome
  from
```
#### Funções de Restrições

#### Função Join

```
SELECT
SKU

FROM 'JOIN.Vendas'
GROUP BY SKU
```

```
SELECT
Vendedor
COUNT(Quantidade_vendida) as Vendas

FROM 'JOIN.Vendas'
GROUP BY Vendedor 
```

```
SELECT
Filial
COUNT(Quantidade_vendida) as Vendas_filial

FROM 'JOIN.Vendas'
GROUP BY Filial
```

#### Funções de Agregação 

```
SELECT
SKU
Quantidade_Vendida
total_de_vendas

  FROM 'projeto.JOIN.Vendas'
order by Quantidade_Vendida 
```

```
SELECT
SKU
Quantidade_Vendida
total_de_vendas

  FROM 'projeto.JOIN.Vendas'
order by total_de_vendas
-- DESC 
```

```
SELECT
format_timestamp("%Y", Data_devolucao) as Ano_devolucao,
COUNT (Quantidade_Devolvida) as Devoluções

FROM "projeto.JOIN.Devolucao"
GROUP BY Ano_devolucao
ORDER BY Ano_devolucao
```

#### Funções Operacionais
