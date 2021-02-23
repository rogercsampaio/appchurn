# Importação dos pacotes necessários
import streamlit as st
import time
import os
from joblib import dump, load
import numpy as np
import pandas as pd
from PIL import Image

# Criando os componentes 
st.set_page_config(page_title = 'Simulador de Church')
image = Image.open('image.png')
st.header('Simulador de Church em Operadoras de Telecomunicações')
st.image(image,use_column_width=True)
st.subheader('Sobre')
st.markdown('Um dos problemas enfrentados pelas empresas de telecomunicações é quanto a perda de seus respectivos clientes, chamado de churning (rotatividade). O cliente pode deixar a operadora caso esteja insatisfeito com alguns de seus serviços incluindo preço do contrato, qualidade no atendimento do call-center entre outros. O problema a resolver aqui é através de um modelo de regressão logística, prever a probabilidade de um cliente deixar a operadora, para antes mesmo disso acontecer, tomar as devidas medidas junto com as áreas gestoras.')
st.markdown('Base de dados explorada: https://www.kaggle.com/c/customer-churning')
st.markdown('Produzido por: Roger C. Sampaio, Cientista de Dados, www.dataminutes.com')
st.subheader('Cadastro')

# (account_length) = tempo do contrato
st.markdown('')
tempoContrato = st.slider('Informe o tempo de contrato em meses com a operadora',min_value = 1,
	max_value = 360)
st.write('Quantidade de Meses',tempoContrato)
if (tempoContrato >= 12):
	st.write('Anos contratados',tempoContrato//12)
else:
	st.write('Menos de 1 ano.')

# (area_code) = código da área
# Carregar uma lista aqui dos DDI dos Estados Unidos posteriormente
st.markdown('')
if (os.path.exists('datasets/city_area_code.xlsx')):
	#cidadesAreaCode = pd.read_excel("datasets/city_area_code.xlsx")
	#cidadesAreaCode.CODIGO_DDI = cidadesAreaCode.CODIGO_DDI.apply(lambda item: item[2:])
	#cidadesAreaCode = cidadesAreaCode.drop(columns = 'CIDADE')
	#cidadesAreaCode = cidadesAreaCode.drop_duplicates()
	#listAreaCodes = list(cidadesAreaCode.CODIGO_DDI)
	listAreaCodes = ['810','500']
	codigoArea = st.selectbox('Informe o código da área',options = listAreaCodes)
	st.write('Código da área',codigoArea)

	# (international_plan) = suporte a plano internacional ou não
	st.markdown('')
	listOpcoes = ['sim','não']
	suportePlanoInternacional = st.radio('Tem suporte ao plano internacional?',options = listOpcoes)
	st.write('Opção de suporte escolhida: ',suportePlanoInternacional)
	# Converter

	# (voice_mail_plan) = suporte a secretária eletrônica
	st.markdown('')
	suporteSecretaria = st.radio('Tem suporte a secretaria eletrônica?',options = listOpcoes)
	st.write('Opção de secretaria escolhida: ',suporteSecretaria)
	# Converter

	# (number_vmail_messages) = número de mensagens da secretária eletrônica
	st.markdown('')
	numMensagensEletrônica = st.slider('Informe o número contratado de mensagens da secretária eletrônica',min_value = 0,
		max_value = 100)
	st.write('Número de mensagens contratado: ',numMensagensEletrônica)

	# (total_day_minutes) = total de minutos por dia
	st.markdown('')
	numTotalDayMinutes = st.slider('Informe o número total de minutos por dia contratado ',min_value = 0.0,max_value = 400.0)
	st.write('Total de número de minutos por dia contratado: ',numTotalDayMinutes)

	# (total_day_calls) = total de ligações por dia
	st.markdown('')
	numTotalDayCalls = st.slider('Informe o número total de ligações por dia ',min_value = 0, max_value = 200)
	st.write('Número total de ligações por dia contratado: ',numTotalDayCalls)


	# (total_day_charge) = COBRANÇA TOTAL DAS CHAMADAS DIURNAS
	st.markdown('')
	numTotalDayCharge = st.slider('Informe o valor total das cobrança das chamadas diurnas ',min_value = 0.0, max_value = 100.0)
	st.write('Valor da cobrança total das chamadas diurnas contratado',numTotalDayCharge)

	# (total_eve_minutes) = TOTAL DE MINUTOS DE LIGAÇÕES NOTURNAS
	st.markdown('')
	numTotalEveMinutes = st.slider('Informe o valor total de minutos de ligações noturnas',min_value = 0.0, max_value = 400.0)
	st.write('Total de minutos de ligações noturnas contratado ',numTotalEveMinutes)

	# (total_eve_calls) = NÚMERO TOTAL DE LIGAÇÕES NOTURNAS
	st.markdown('')
	numTotalEveCalls = st.slider('Informe o número total de ligações noturnas',min_value = 0, max_value = 200)
	st.write('Número total de ligações noturnas contratado',numTotalEveCalls)

	# (total_eve_charge) = CUSTO TOTAL DAS CHAMADAS NOTURNAS
	st.markdown('')
	numTotalEveCharge = st.slider('Informe o custo total das chamadas noturnas',min_value = 0.0, max_value = 50.0)
	st.write('Custo total das chamadas noturnas',numTotalEveCharge)


	# total_night_minutes = TOTAL DE MINUTOS EM LIGAÇÕES MADRUGADA
	st.markdown('')
	numTotalNightMinutes = st.slider('Informe o total de minutos em ligações de madrugada',min_value = 0.0, max_value = 400.0)
	st.write('Total de minutos em ligações de madrugada contratado',numTotalNightMinutes)

	# total_night_calls = TOTAL DE LIGAÇÕES MADRUGADA
	st.markdown('')
	numTotalNightCalls = st.slider('Informe o total de ligações de madrugada',min_value = 0, max_value = 200)
	st.write('Total de ligações de madrugada contratado',numTotalNightCalls)


	# total_night_charge = COBRANÇA TOTAL DAS CHAMADAS MADRUGADA
	st.markdown('')
	numtotalNightCharge = st.slider('Informe o total da cobrança das chamadas de madrugada',min_value = 1.0, max_value = 20.0)
	st.write('Total da cobrança das chamadas de magrudada',numtotalNightCharge)

	# total_intl_minutes = TOTAL DE MINUTOS DE CHAMADAS INTERNACIONAIS
	st.markdown('')
	numTotalIntlMinutes = st.slider('Informe o total de minutos de chamadas internacionais',min_value = 0.0, max_value = 30.0)
	st.write('Total de minutos em chamadas internacionais contratato',numTotalIntlMinutes)

	# total_intl_calls = NÚMERO TOTAL DE CHAMADAS INTERNACIONAIS
	st.markdown('')
	numTotalIntlCalls= st.slider('Informe o número total de chamadas internacionais',min_value = 0, max_value = 30)
	st.write('Número total de chamadas internacionais contratato',numTotalIntlCalls)

	# total_intl_charge = CUSTO TOTAL DE CHAMADAS INTERNACIONAIS
	st.markdown('')
	numTotalIntlCharge = st.slider('Informe o custo total de chamadas internacionais',min_value = 0.0, max_value = 10.0)
	st.write('Custo total de chamadas internacionais',numTotalIntlCharge)

	# number_customer_service_calls = NÚMERO DE LIGAÇÕES AO CALL CENTER
	st.markdown('')
	numberCustomerServiceCalls = st.slider('Informe o número de ligações ao call center',min_value = 0, max_value = 20)
	st.write('Número de ligações ao call center contratado ',numberCustomerServiceCalls)


	# Transformação de variáveis booleanas para preparação do modelo preditivo
	suportePlanoInternacional = suportePlanoInternacional.replace("sim","1")
	suportePlanoInternacional = suportePlanoInternacional.replace("não","0")

	suporteSecretaria = suporteSecretaria.replace("sim","1")
	suporteSecretaria = suporteSecretaria.replace("não","0")

	st.markdown('')
	st.subheader('OS 5 Principais Motivos de Desistência dos Clientes')
	motivos = pd.DataFrame([[1,'COBRANÇA TOTAL DAS CHAMADAS DIURNAS'],
		[2,'TOTAL DE MINUTOS POR DIA'],
		[3,'NÚMERO DE LIGAÇÕES AO CALL CENTER'],
		[4,'CUSTO TOTAL DE CHAMADAS INTERNACIONAIS'],
		[5,'TOTAL DE MINUTOS DE LIGAÇÕES NOTURNAS']],columns = ['Ranking','Motivo'] )
	st.dataframe(motivos)

	st.markdown('')
	# Carregando o modelo para efetuar as previsões
	if (os.path.exists('modelo4.pk1')):
		modelo4Carregado = load('modelo4.pk1')
		cliqueBotao = st.button('Efetuar previsão')
		if(cliqueBotao):
			with st.spinner('Aguarde enquanto é efetuado a previsão...'):
				time.sleep(3)
			dadosCliente = np.array([[tempoContrato,
				codigoArea,
				int(suportePlanoInternacional),
				int(suporteSecretaria), 
				numMensagensEletrônica,
				numTotalDayMinutes,
				numTotalDayCalls,
				numTotalDayCharge,
				numTotalEveMinutes,
				numTotalEveCalls,
				numTotalEveCharge,
				numTotalNightMinutes,
				numTotalNightCalls,
				numtotalNightCharge,
				numTotalIntlMinutes,
				numTotalIntlCalls,
				numTotalIntlCharge,
				numberCustomerServiceCalls
				]])
			# exemplo dadosNovo = np.array([[100,500,0.0,1.0,35,150,80,30,115,60,10,150,100,12,10,8,4,0.0]])
			previsao = modelo4Carregado.predict(dadosCliente)
			st.subheader('Resultado da previsão')
			# Veja o que pode fazer, fatores que mais influenciam.
			if(previsao[0] == 0):
				st.balloons()
				st.success('Seu cliente não irá deixar você')
			else:
				st.warning('Seu cliente pode deixar você!')
				st.warning('Probabilidade de acontecer 95%!')

	else:
		st.error('Erro ao carregar o modelo preditivo. Contrate a administrador do sistema')


else:
	st.error('Erro ao carregar a lista de cidades. Contrate a administrador do sistema!')


