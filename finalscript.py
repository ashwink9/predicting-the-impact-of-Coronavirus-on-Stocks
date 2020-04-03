def getCompanyData(comp_name,start,end, FullName):
    import yfinance as yf
    st = yf.download(comp_name, start, end)
    st['CompanyName'] = FullName
    return st

def getDescriptiveStat(data):
    print(data.describe())
    
def test_stationarity(timeseries):
    import pandas as pnd
    import matplotlib.pyplot as pl
    from statsmodels.tsa.stattools import adfuller
    rolmean = timeseries.rolling(12).mean()
    rolstd = timeseries.rolling(12).std()
    pl.plot(timeseries, color='blue',label='Original')
    pl.plot(rolmean, color='red', label='Rolling Mean')
    pl.plot(rolstd, color='black', label = 'Rolling Std')
    pl.legend(loc='best')
    pl.title('Rolling Mean and Standard Deviation')
    pl.show(block=False)
    print("Results of the  test")
    adft = adfuller(timeseries,autolag='AIC')
    output = pnd.Series(adft[0:4],index=['Test Statistics','p-value','No. of lags used','Number of observations used'])
    for key,values in adft[4].items():
        output['critical value (%s)'%key] =  values
    print(output)
    
    