#%%
import sidrapy as sdr
import pandas as pd
from statsmodels.tsa.filters.hp_filter import hpfilter
import matplotlib.pyplot as plt
#%% PIB QoQ
#Construindo o Dataframe
pib_qoq = sdr.get_table(
    table_code="5932",          # tabela 5932 - PIB Trimestral
    territorial_level="1",      # N1 = Brasil
    ibge_territorial_code="1",  # código 1 = Brasil
    variable="6564",            # taxa trimestre contra trimestre imediatamente anterior (%)
    period="201001 - 202503",     # toda a faixa de trimestres listada em /P/
    classifications={"11255": "90707"},    # código da classificação "Setores e subsetores"         # categoria 90707 = PIB a preços de mercado
)
#%% Limpando o Dataframe e Padronizando o Index
pib_qoq = pib_qoq[["D2N", "V"]] #elimina colunas desnecessárias
pib_qoq.columns = ("Data", "Variação") #atribui os nomes Data e Variação p/ colunas 
pib_qoq = pib_qoq.iloc[1:] # inicia a partir da segunda linha eliminando o cabeçalho
pib_qoq = pib_qoq.set_index("Data") #transforma a coluna data em index
pib_qoq = pd.DataFrame(pib_qoq).astype(float) #transforma os dados em float 
idx = pib_qoq.index.to_series() # cria uma série a partir do index
ano = idx.str.extract(r"(\d{4})", expand=False) # extrai o ano do texto do index
tri = idx.str.extract(r"(\d+)\D+trimestre", expand=False) # extrai o trimestre  do texto do index
period_str = ano + "Q"+ tri # monta o padrão YYYYT
pib_qoq.index = pd.PeriodIndex(period_str, freq="Q") # transforma o padrão em data trimestral
pib_qoq.index = pib_qoq.index.to_timestamp(how="start") # atribui a data inicial do trimestre
print(pib_qoq)
# %% PIB YoY
pib_yoy = sdr.get_table(
    table_code="5932",
    territorial_level="1",
    ibge_territorial_code="1",
    variable="6561",
    period="201001-202503",
    classifications={"11255": "90707"},   
)
pib_yoy = pib_yoy[["D2N", "V"]]
pib_yoy.columns = ("Data", "Variação")
pib_yoy = pib_yoy.iloc[1:]
pib_yoy = pib_yoy.set_index("Data")
pib_yoy = pd.DataFrame(pib_yoy).astype(float)
idx = pib_yoy.index.to_series()
ano = idx.str.extract(r"(\d{4})", expand=False)
tri = idx.str.extract(r"(\d+)\D+trimestre", expand=False)
period_str = ano + "Q"+ tri
pib_yoy.index = pd.PeriodIndex(period_str, freq="Q")
pib_yoy.index = pib_yoy.index.to_timestamp(how="start")
print(pib_yoy)

# %%
pib_df = sdr.get_table(
    table_code="1621",
    territorial_level="1",
    ibge_territorial_code="1",
    variable="584",
    period="199602-202503",
    classifications={"11255": "90707"},
)
pib_df = pib_df[["D2N", "V"]]
pib_df.columns = ("Data", "PIB")
pib_df = pib_df.iloc[1:]
pib_df = pib_df.set_index("Data")
idx = pib_df.index.to_series()
ano = idx.str.extract(r"(\d{4})", expand = False)
tri = idx.str.extract(r"(\d+)\D+trimestre", expand = False)
period_str = ano + "Q" + tri
pib_df.index = pd.PeriodIndex(period_str, freq="Q")
pib_df.index = pib_df.index.to_timestamp(how="start")
print(pib_df)

# %%

print(pib_setor)
# %%
