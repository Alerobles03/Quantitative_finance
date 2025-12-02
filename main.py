import pandas as pd
import numpy as np
from modules.financial_functions import portfolio_volatility, portfolio_returns, VaR
from modules.backend import tickers_by_issuer

if __name__ =='__main__': 
    #Obtener tickers de ishares
    tickers = tickers_by_issuer(issuer= 'iShares')
    list_tickers = list(tickers['TICKER'])
    
    for ticker in list_tickers:
        print(f'Instrumento: {ticker}')
    
    #Portafolio de renta fija
    tickers_rf = tickers[tickers['CATEGORIA']=='ETF RF']
    list_tickers_rf = list(tickers_rf['TICKER'])

    #Portafolio de renta variable
    tickers_rv = tickers[tickers['CATEGORIA']=='ETF RV']
    list_tickers_rv = list(tickers_rv['TICKER'])

    #Rango de fechas
    start = '2024-01-01'
    end = '2024-12-31'

    #Nivel de confianza
    confidence = 0.05
    lst = []
    
    for portafolio  in [list_tickers_rf, list_tickers_rv]:
        print(portafolio)
        
        df = portfolio_returns(tickers=portafolio ,start=start, end=end)
        print(df.head(5))

        vector_w = np.array([1/len(portafolio)]*len(portafolio))
        print(vector_w)

        #Calcular volatilidad
        sigma = portfolio_volatility(df=df, vector_w=vector_w)
        print(sigma)

        #Calcular el VaR
        var= VaR(sigma=sigma, confidence=confidence)
        var= np.abs(var)
        var_mensual = var * np.sqrt(20) 
        print(var_mensual)
        lst.append(var_mensual)
    
    df_final = pd.DataFrame(
        {
            'PORTAFOLIO': ['iShares Renta Fija', 'iShares Renta Variaable'], 
            f'Value At Risk: {1-confidence}%': lst
        }
    )
    df_final = df_final.sort_values(
        by=f'Value At Risk: {1-confidence}%',
         ascending=False)
    print(df_final)








