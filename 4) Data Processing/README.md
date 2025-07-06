# Data Processing

> Processamento de dados é o conjunto de atividades que transforma dados brutos (informações soltas, sem estrutura ou significado imediato) em informações organizadas (relatórios, gráficos, análises)

### Introdução

- Database -> Armazenar dados operacionais/transacionais do dia a dia. Exemplo: Cadastro de clientes, registros de vendas, dados de estoque, pedidos.
  
- Data Warehouse -> Armazena dados análiticos/gerenciais, ou seja, dados estruturados (relatórios e análises). Exemplo: Indicadores de desempenho (KPIs), relatórios financeiros, dados de vendas e marketing.
    - Google Big Query
    - Snowflake
    - AWS Redshift
    - Microsoft Azure Synapse

- Big Data -> Conjuntos de dados massivamente grandes, complexos e que crescem em velocidade tão alta que os métodos tradicionais de processamento de dados não conseguem lidar com eles de forma eficiente.
  
- Data Lake -> Armazena dados estruturados, semi-estruturados e não estruturados, ou seja. um repositório de qualquer tipo de dado.
    - AWS S3
    - Azure Data Lake 
    - Google Cloud Storage
    - Databricks Lakehouse
    - Hadoop Distributed File System

- Delta Lake -> É uma tecnologia open source desenvolvida em cima de data lakes (normalmente desenvolvido em Spark) como uma camada complementar, responsável por executar o chamado armazenamento transacional. O armazenamento transacional é um sistema projetado para suportar transações ACID, dentro de um Data Lake, permitindo ler, transformar, limpar, analisar e armazenar dados de forma mais confiável e performática. Acontece que os data lakes eram rápidos para armazenar dados, mas difíceis de manter a qualidade, sendo assim essa solução combina a escalabilidade dos data lakes com a confiabilidade dos Data Warehouse, dando origem ao Data Lakehouse.
    - Delta Lake (Databricks)
    - Hudi (Apache)
    - Iceberg (Apache)

- Data Lakehouse -> Data Warehouse + Data Lake
    - Databricks Lakehouse Platform
    - Amazon Redshift Spectrum + S3
    - Google BigLake
 
> Spark é uma plataforma de processamento de dados distribuída de open source, ou seja, um conjunto de ferramentas que permite coletar, armazenar, organizar, transformar e analisar dados. Ele foi projetado para facilitar o trabalho com grandes volumes de dados, permitindo eficiência e escalabilidade. Ele geralmente é a base de desenvolvimento de todos os Delta Lake. Além dele existem outras soluções como: Flink, Hadoop e o Dataflow.

![Img.1](https://github.com/user-attachments/assets/7b4d3a0b-e7ce-483e-b283-279f09be574e)
Fonte: Databricks


  - Hadoop
    - Flink
