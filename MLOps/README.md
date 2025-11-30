# Fundamentals

<div align="center">

![Img](https://github.com/user-attachments/assets/af62f067-04ac-4a16-861e-7a00bb690283)
<!-- BADGES -->
<img src="https://img.shields.io/github/license/HenrySchall/Fundamentals?style=flat&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
<img src="https://img.shields.io/github/last-commit/HenrySchall/Fundamentals?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/HenrySchall/Fundamentals?style=flat&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/HenrySchall/Fundamentals?style=flat&color=0080ff" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Markdown-000000.svg?style=flat&logo=Markdown&logoColor=white" alt="Markdown">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/R-276DC3?style?style=flat&logo=r&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Stata-30B5C8?style=flat&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Jupyter%20Notebook-F37626?style?style=flat&logo=jupyter&logoColor=white" alt="Python">

</div>
<br>

> A área de dados engloba um conjunto de disciplinas que trabalham desde a coleta, organização e armazenamento dos dados até a sua análise, modelagem e aplicação prática. Os profissionais que atuam nesse campo buscam transformar dados brutos em informações úteis, capazes de gerar vantagens competitivas, otimizar processos e criar novos produtos e serviços.

### Áreas de Atuação 

* Data Science = extrai valor e conhecimento a partir de grandes volumes de dados usando estatística, programação, machine learning e conhecimento do negócio. Seu papel principal é transformar dados brutos em insights estratégicos ou soluções automatizadas, como modelos preditivos, sistemas de recomendação, segmentações
    
* Data Analyst =  coletar, organizar, interpretar e apresentar dados, com o objetivo de ajudar empresas a tomar decisões baseadas em evidências. Ele atua como um "tradutor entre os dados e o negócio", transformando números em insights claros e acionáveis.

* Data Engineer = Construir, manter e otimizar a infraestrutura de dados de uma empresa. Ele garante que os dados estejam disponíveis, organizados, limpos e acessíveis para analistas, cientistas de dados, engenheiros de machine learning

* Machine Learning Engineer = desenvolver, treinar, testar, otimizar e colocar em produção modelos de machine learning (aprendizado de máquina) em escala. Ele atua na ponte entre ciência de dados e engenharia de software, garantindo que os modelos não apenas funcionem bem em notebooks de pesquisa, mas que também sejam robustos, escaláveis e usáveis em ambientes reais

* AI Engineer = projeta, desenvolve, implementa e mantém sistemas de IA, combinando conhecimentos de machine learning, deep learning, engenharia de software, e às vezes até IA simbólica
  
---
## Índice

- [Math](https://github.com/HenrySchall/Fundamentals/tree/main/Math)
    - [Statistical Inference](https://github.com/HenrySchall/Fundamentals/tree/main/Math/Statistical%20Inference)
    - [Linear Algebra](https://github.com/HenrySchall/Fundamentals/tree/main/Math/Linear%20Algebra)
- [Data Science](https://github.com/HenrySchall/Fundamentals/tree/main/Data%20Science)
    - [Python](https://github.com/HenrySchall/Fundamentals/tree/main/Data%20Science/Python)
    - [R](https://github.com/HenrySchall/Fundamentals/tree/main/Data%20Science/R)
    - [Stata](https://github.com/HenrySchall/Fundamentals/tree/main/Data%20Science/Stata)
- [Data Process](https://github.com/HenrySchall/Fundamentals/tree/main/Data%20Process)
    - [Cloud](https://github.com/HenrySchall/Fundamentals/tree/main/Data%20Process/Cloud)
    - [Databricks](https://github.com/HenrySchall/Fundamentals/tree/main/Data%20Process/Databricks)
    - [MLFlow](https://github.com/HenrySchall/Fundamentals/tree/main/Data%20Process/MLflow)

---

### Referências Bibliográficas:
- https://visualgo.net/en
- https://neetcode.io/courses

![1756281794385](https://github.com/user-attachments/assets/89138c5b-3825-4211-8548-ac9d22591c2b)

# Data Process

> Processamento de dados é o conjunto de atividades que transforma dados brutos (informações soltas, sem estrutura ou significado imediato) em informações organizadas (relatórios, gráficos, análises)

### Introdução

- Database -> Armazenar dados operacionais/transacionais do dia a dia. Exemplo: Cadastro de clientes, registros de vendas, dados de estoque, pedidos.
  
- Data Warehouse -> Armazena dados análiticos/gerenciais, ou seja, dados estruturados (relatórios e análises). Exemplo: Indicadores de desempenho (KPIs), relatórios financeiros, dados de vendas e marketing.
    - Google Big Query
    - Snowflake
    - AWS Redshift
    - Microsoft Azure Synapse

- Big Data -> Conjuntos de dados massivamente grandes, complexos e que crescem em velocidade tão alta que os métodos tradicionais de processamento de dados não conseguem lidar com eles de forma eficiente.
    - Formatos de Big Data:
      - Parquet -> Colunar, padrão Spark
      - Apache ORC -> Colunar, padrão Hive
      - Apache Avro -> Linha
     
> Em geral ORC é mais eficiente na criação (escrita) e na compressão e Parquet tem melhor performance na consulta (leitura). Lembrando que: Muito atributos e mais escrita = Bancos de dados orientados a linha (Row-oriented databases), ideal para sistemas transacionais (Databases) e menos atributos e mais leitura = Bancos de dados orientados a coluna (Column-oriented databases), ideal para sistemas análiticos (Data Warehouse).
  
- Data Lake -> Armazena dados estruturados, semi-estruturados e não estruturados, ou seja. um repositório de qualquer tipo de dado. Exemplos:
    - AWS S3
    - Azure Data Lake 
    - Google Cloud Storage
    - Databricks Lakehouse
    - Hadoop Distributed File System

- Data Swamp: É um data lake sem controle de qualidade e repleto de dados desorganizados e não-estruturados.

- Delta Lake -> É uma tecnologia open source desenvolvida em cima de data lakes (normalmente desenvolvido em Spark) como uma camada complementar, responsável por executar o chamado armazenamento transacional. O armazenamento transacional é um sistema projetado para suportar transações ACID, dentro de um Data Lake, permitindo ler, transformar, limpar, analisar e armazenar dados de forma mais confiável e performática. Acontece que os data lakes eram rápidos para armazenar dados, mas difíceis de manter a qualidade, sendo assim essa solução combina a escalabilidade dos data lakes com a confiabilidade dos Data Warehouse, dando origem ao Data Lakehouse. Além dele existem outras soluções como: Apache Hudi e Apache Iceberg.

- Data Lakehouse -> Data Warehouse + Data Lake
    - Databricks Lakehouse Platform
    - Amazon Redshift Spectrum + S3
    - Google BigLake

![Img.1](https://github.com/user-attachments/assets/7b4d3a0b-e7ce-483e-b283-279f09be574e)
Fonte: Databricks

Data Mesh, Data Fabric

Observações: 

IaaS
PaaS
SaaS

- Sistemas de Arquivos -> é uma maneira de organizar, armazenar e nomear dados em um dispositivo de armazenamento, como um disco rígido, SSD, cartão de memória ou pen drive.

- Sistemas de Arquivos Distribuido -> armazenar e analisar os dados de maneira distribuída e paralela em um cluster de computadores (arquivos espalhados por vários computadores ou servidores), ou seja, divide-se os arquivos em blocos, distribuindo eles em todo o cluster, mas apresentando ao usuário como se fossem parte de um único sistema de arquivos unificado. Exemplos: S3, Google File System, GlusterFS, HDFS, Databricks File System.

### Spark 

> Spark é uma solução de processamento de dados distribuída open source, ou seja, um conjunto de ferramentas que permite coletar, armazenar, organizar, transformar e analisar dados. Ele foi projetado para facilitar o trabalho com grandes volumes de dados, permitindo eficiência e escalabilidade. Além dele existem outras soluções como: Flink, Hadoop e o Dataflow.

- Data Lakes modernos tendem a armazenar dados em formatos: Desacoplados, Compactados, Particionados, esse último possibilita a redundância (replicar em vários discos) e paralelismo (múltiplas operações de leitura e escrita ao mesmo tempo).


# Cloud Plataforms
> São serviços que fornecem recursos computacionais (on demand), como servidores, armazenamento, redes, softwares e análises. Esse tipo de serviço é utilizado por empresas que querem aumentar sua escalabilidade e flexibilidade otimizando seus custos. Em vez delas comprarem e gerenciarem seu próprio hardware e infraestrutura, a nuvem permite elas acessarem esses recursos sob demanda, pagando pelo que usar, adpatando-se a necessidade do momento de cada empresa, ou seja, podem ser aumentados ou diminuídos conforme a necessidade do negócio.

### Principais Clouds

- Amazon Web Services (AWS) 
- Microsoft Azure
- Google Cloud Platform (GCP)
- IBM Cloud
- Oracle Cloud
- SAS Cloud

### Conceitos Importantes
- Data Warehouse -> Sistemas de armazenamento centralizado que reúne todos os dados de uma empresa, organizando-os para facilitar consultas e análises complexas. Exemplo: Google BigQuery, Amazon Redshift, Snowflake

- DataOps (Data + Operations) -> conjunto de práticas para gerenciar e automatizar o ciclo de vida dos dados. Exemplos: Apache Airflow,

- MLOps (Machine Learning + Operations) -> Conjunto de práticas para desenvolver, implementar e manter de modelos de machine learning (ML). Exemplo: MLflow, Kubeflow, SageMaker, VertexAI

- DevOps (Development + Operations) -> Conjunto de práticas para integrar desenvolvimento de software (Dev) com operações/infraestrutura (Ops). Exemplos: Docker, Kubernetes, GitLab CI/CD

- RevOps -> Maximizar e acelerar a geração de receita da empresa, criando processos mais previsíveis, eficientes e baseados em dados. Exemplos: Salesforce, HubSpot

- https://www.coursera.org/specializations/aws-fundamentals (Amazon AWS) 
- https://www.coursera.org/specializations/cloud-computing
- https://www.coursera.org/professional-certificates/aws-cloud-solutions-architect

- https://cloud.google.com/learn/certification/generative-ai-leader
- https://cloud.google.com/learn/certification/machine-learning-engineer?hl=pt-br
- https://www.databricks.com/learn/certification/machine-learning-professional
- https://www.databricks.com/learn/certification/genai-engineer-associate 
- https://www.coursera.org/professional-certificates/preparing-for-google-cloud-machine-learning-engineer-professional-certificate



> Plataforma de computação em nuvem do Google, que oferece centenas de serviços e produtos para desenvolvimento, armazenamento, análise de dados, inteligência artificial, redes, segurança, entre outros.

### Principais Produtos 
- Redshift
- Glue
- S3
- SageMaker
- Quicksight
- Bedrock
- Forecast
- DynamoDB

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