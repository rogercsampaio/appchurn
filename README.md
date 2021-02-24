# appchurn
Projeto incluindo app sobre previsão de churn em uma operadora de telefonia.

Um dos maiores problemas enfrentados por empresas, em especial, operadoras de telefonia, é o churning, ou seja, rotatividade de clientes. Os clientes podem deixar a operadora depois de anos de contrato, caso estejam insatisfeitos com algum item como, por exemplo, preço do valor do contrato, qualidade no atendimento do call-center, quantidade de serviços incluso no pacote entre outros. Esse dashboard contempla uma base de dados pública do kaggle*, tendo 4250 amostras representando contratos de clientes. Informações sobre estado, tempo de acordo com a operadora em meses, se o contrato possui suporte ao plano internacional ou não, total de ligações diárias, preço das ligações noturnas entre outras estão presentes. O dashboard responde por meio de indicadores e gráficos:

1. Qual a quantidade de contratos ativos (não cancelados) e cancelados?

2. Qual o quantitativo de contratos ativos e cancelados segmentado por Estado, de modo a descobrir o estado que mais possui rotatividade?

3. Qual é o número de contratos ativos e cancelados agrupados por código de área?

4. Quantos estados são contemplados? 

5. Em questão de total das chamadas diurnas, qual a média por situação de contrato? E por Estado?

6. Qual a média dos minutos por dia dos clientes que cancelaram o contrato e daqueles que estão ativos?

Ainda é possível responder outras perguntas, utilizando os filtros disponíveis em cada página.
O projeto contempla também previsão de churn para novos clientes cadastrados, além de encontrar quais os principais fatores que influenciam o cliente deixar a operadora. Tecnologias usadas: Python, Qlik Sense, PowerBI.

Link dashboard: https://app.powerbi.com/view?r=eyJrIjoiZmMwOWIzNTctNjRhMS00Mjg5LTliZWItNTNhZTZjZDcwZWM3IiwidCI6ImYwNTFkMjhjLWM4NTctNGRiMy04NzdlLWIwNGY0M2Y1ZDQxZiJ9&pageName=ReportSection
Link previsões: https://share.streamlit.io/rogercsampaio/appchurn/main
