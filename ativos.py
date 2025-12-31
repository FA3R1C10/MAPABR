#%% Bibliotecas
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %% Lista de ativos
start = "2024-12-30"
end = "2025-12-30"
ativos = ["^BVSP", "^GSPC", "BTC-USD", "GC=F", "BRL=X", "EURBRL=X"]
data = yf.download(ativos, start, end)["Close"].dropna()
data = data.rename(columns = {"BRL=X": "Dólar",
                              "BTC-USD": "Bitcoin",
                              "EURBRL=X": "Euro",
                              "GC=F": "Ouro",
                              "^BVSP": "Ibovespa",
                              "^GSPC": "S&P500"
                              })
#%% Performance normalizada
data_perf = ((data / data.iloc[0] - 1) * 100).astype(float).round(2)
# %%
fig, axes = plt.subplots(ncols=3, nrows=2, figsize=(24,12))
axes[0,0].plot(data_perf["Ibovespa"], color="blue", label="Ibovespa")
axes[0,0].annotate(f"{data_perf["Ibovespa"].iloc[-1]}%",
                   xy=(0.97, 0.5), xycoords = "axes fraction",
                   va = "bottom", ha = "right", fontsize = 10, color = "blue",
                   bbox=dict(boxstyle= "round, pad=0.25", fc="lightgray", ec="blue", lw=0.8, alpha=0.75))
axes[0,0].annotate(f"Ibov: {data["Ibovespa"].iloc[-1]:.0f}",
                   xy=(0.97, 0.45), xycoords = "axes fraction",
                   va = "bottom", ha = "right", fontsize = 10, color = "blue",
                   bbox=dict(boxstyle="round,pad=0.25", fc="lightgray", ec="blue", lw=0.8, alpha=0.75))
axes[0,0].legend()
axes[0,1].plot(data_perf["S&P500"], color="blue", label="S&P500")
axes[0,1].annotate(f"{data_perf["S&P500"].iloc[-1]}%",
                   xy=(0.97, 0.5), xycoords = "axes fraction",
                   va = "bottom", ha = "right", fontsize = 10, color = "blue",
                   bbox=dict(boxstyle="round,pad=0.25", fc="lightgray", ec="blue", lw=0.8, alpha=0.75))
axes[0,1].annotate(f"SP500: {data["S&P500"].iloc[-1]:.0f}",
                   xy=(0.97, 0.45), xycoords = "axes fraction",
                   va = "bottom", ha = "right", fontsize = 10, color = "blue",
                   bbox=dict(boxstyle="round,pad=0.25", fc="lightgray", ec="blue", lw=0.8, alpha=0.75))
axes[0,1].legend()
axes[0,2].plot(data_perf["Bitcoin"], color="red", label="Bitcoin")
axes[0,2].annotate(f"{data_perf["Bitcoin"].iloc[-1]}%",
                   xy=(0.97, 0.5), xycoords = "axes fraction",
                   va = "bottom", ha = "right", fontsize = 10, color = "red",
                   bbox=dict(boxstyle="round,pad=0.25", fc="lightgray", ec="red", lw=0.8, alpha=0.75))
axes[0,2].annotate(f"BTC: {data["Bitcoin"].iloc[-1]:.2f}",
                   xy=(0.97, 0.45), xycoords = "axes fraction",
                   va = "bottom", ha = "right", fontsize = 10, color = "red",
                   bbox=dict(boxstyle="round,pad=0.25", fc="lightgray", ec="red", lw=0.8, alpha=0.75))
axes[0,2].legend()
axes[1,0].plot(data_perf["Dólar"], color="red", label="Dólar")
axes[1,0].annotate(f"{data_perf["Dólar"].iloc[-1]}%",
                   xy=(0.97, 0.5), xycoords = "axes fraction",
                   va = "bottom", ha = "right", fontsize = 10, color = "red",
                   bbox=dict(boxstyle="round,pad=0.25", fc="lightgray", ec="red", lw=0.8, alpha=0.75))
axes[1,0].annotate(f"USD: {data["Dólar"].iloc[-1]:.2f}",
                   xy=(0.97, 0.45), xycoords = "axes fraction",
                   va = "bottom", ha = "right", fontsize = 10, color = "red",
                   bbox=dict(boxstyle="round,pad=0.25", fc="lightgray", ec="red", lw=0.8, alpha=0.75))
axes[1,0].legend()
axes[1,1].plot(data_perf["Euro"], color="blue", label="Euro")
axes[1,1].annotate(f"{data_perf["Euro"].iloc[-1]}%",
                   xy=(0.97, 0.5), xycoords = "axes fraction",
                   va = "bottom", ha = "right", fontsize = 10, color = "blue",
                   bbox=dict(boxstyle="round,pad=0.25", fc="lightgray", ec="blue", lw=0.8, alpha=0.75))
axes[1,1].annotate(f"Euro: {data["Euro"].iloc[-1]:.2f}",
                   xy=(0.97, 0.45), xycoords = "axes fraction",
                   va = "bottom", ha = "right", fontsize = 10, color = "blue",
                   bbox=dict(boxstyle="round,pad=0.25", fc="lightgray", ec="blue", lw=0.8, alpha=0.75))
axes[1,1].legend()
axes[1,2].plot(data_perf["Ouro"], color="blue", label="Ouro")
axes[1,2].annotate(f"{data_perf["Ouro"].iloc[-1]}%",
                   xy=(0.97, 0.5), xycoords = "axes fraction",
                   va = "bottom", ha = "right", fontsize = 10, color = "blue",
                   bbox=dict(boxstyle="round,pad=0.25", fc="lightgray", ec="blue", lw=0.8, alpha=0.75))
axes[1,2].annotate(f"Ouro: {data["Ouro"].iloc[-1]:.2f}",
                   xy=(0.97, 0.45), xycoords = "axes fraction",
                   va = "bottom", ha = "right", fontsize = 10, color = "blue",
                   bbox=dict(boxstyle="round,pad=0.25", fc="lightgray", ec="blue", lw=0.8, alpha=0.75))
axes[1,2].legend()
fig.suptitle("2025")
plt.annotate("Fonte: Yahoo Finance", xy=(0.06,0.0),
             va="bottom", ha="left", xycoords="figure fraction",
             color="black", fontsize=10)
plt.annotate("Elaborado por: Fabricio Orlandin, CFP®", xy=(0.84,0.0),
             va="bottom", ha="right", xycoords="figure fraction",
             color="black", fontsize=10)
# %%
