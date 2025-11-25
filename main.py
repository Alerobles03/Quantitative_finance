import numpy as np
from modules.financial_functions import porfolop_volatility, portfolio_returns, VaR

if __name__ =='__main__': 
    pass
    tickers = ['IEF', 'SPTL', 'TLT', 'VGLT']
    start = '2023-01-01'
    end = '2024-21-31'

 
    #Descargar retornos de portafolio
    
    df = portfolio_returns(
        tickers=tickers, 
        start=start, 
        end=end
        )
    print(df.head(5))

    #Calculo volatilidad 
    vector_w = np.array ([1/len(tickers)]*len(tickers))
    print(vector_w)
    sigma = porfolop_volatility(df= df, vector_w= vector_w)
    print(sigma)

    print('='*100)

    #Value at Risk
    confidence = 0.05
    var = VaR(sigma= sigma, confidence= confidence)
    print(var)

