import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import plotly.express as px

def plotDf (df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df ['formatted_date'], y = df['close'], mode='lines', name='lines'))
    fig.add_trace(go.Scatter(x=df ['formatted_date'], y = df['slopeEma21'], mode='lines', name='lines'))
    fig.add_trace(go.Scatter(x=df ['formatted_date'], y = df['slopeSma20'], mode='lines', name='lines'))
    #fig = px.line(df)
    #fig = px.line(df)
    fig.show()

def plotChartSubplots (data):
    fig = make_subplots (specs = [[{"secondary_y": True}]])
    fig.add_trace (
        go.Candlestick (
            x = data['formatted_date'],
            open = data.open,
            high = data.high,
            low = data.low,
            close = data.close
        )
    )
    fig.add_trace (
        go.Scatter (
            x = data['formatted_date'],
            y = data['sma20'],
            mode = 'lines',
            name = 'SMA_20',
            line = {'color': 'orange', 'width': 4}
        )
    )
    fig.add_trace (
        go.Scatter (
            x = data['formatted_date'],
            y = data['ema21'],
            mode = 'lines',
            name = 'EMA_21',
            line = {'color': 'yellow', 'width': 4}
        )
    )
    fig.add_trace (
        go.Scatter (
            x = data['formatted_date'],
            y = data['sma36'],
            mode = 'lines',
            name = 'SMA_36',
            line = {'color': 'blue', 'width': 4}
        )
    )
    fig.add_trace (
        go.Scatter (
            x = data['formatted_date'],
            y = data['sma60'],
            mode = 'lines',
            name = 'SMA_60',
            line = {'color': 'green', 'width': 4}
        )
    )
    fig.add_trace (
        go.Scatter (
            x = data['formatted_date'],
            y = data['slopeEma21'],
            mode = 'lines',
            name = 'Slope EMA 21',
            line = {'color': 'yellow', 'width': 1}
        ),
        secondary_y = True
    )
    fig.add_trace (
        go.Scatter (
            x = data['formatted_date'],
            y = data['slopeSma20'],
            mode = 'lines',
            name = 'Slope SMA 20',
            line = {'color': 'orange', 'width': 1}
        ),
        secondary_y = True
    )
    '''
    fig.add_trace (
        go.Scatter (
            x = data['formatted_date'],
            y = data['slopeSma36'],
            mode = 'lines',
            name = 'Slope SMA 36',
            line = {'color': 'blue', 'width': 1}
        ),
        secondary_y = True
    )
    fig.add_trace (
        go.Scatter (
            x = data['formatted_date'],
            y = data['slopeSma60'],
            mode = 'lines',
            name = 'Slope SMA 60',
            line = {'color': 'green', 'width': 1}
        ),
        secondary_y = True
    )'''
    #fig.add_trace (go.Bar(x=data['formatted_date'], y=data['sma20ext'], marker_color = 'rgba(167, 240, 242, .05)', name = 'sma20ext'),secondary_y=True)
    fig.layout.yaxis2.showgrid=False
    fig.update_layout(
        title = f'The Candlestick graph',
        xaxis_title = 'Date',
        yaxis_title = f'Price (USD)',
        xaxis_rangeslider_visible = True,
        plot_bgcolor='rgb(10,10,10)'
    )
    #fig.update_yaxes(tickprefix='$')

    #
    '''
    dist=5
    buySignal = np.logical_and(data.low < data.sma20, data.sma4 > data.sma8)
    buySignal = np.logical_or (buySignal, data.low < data.sma50)
    sellSignal = data.sma20ext > 2.5
    data['buys'] = np.where(buySignal, data.low - dist, data.high + dist)
    data['buyArrows'] = np.where(buySignal, 'triangle-up', 'triangle-down')
    data['buyColor'] = np.where(buySignal, 'green', 'rgba(167, 240, 242, 0)')
    data['sells'] = np.where (sellSignal, data.high + dist, data.low - dist)
    data['sellArrows'] = np.where(sellSignal, 'triangle-down', 'triangle-down')
    data['sellColor'] = np.where(sellSignal, 'red', 'rgba(167, 240, 242, 0)')
    fig.add_trace (go.Scatter(x=data['formatted_date'],
                   y=data['buys'],
                   mode='markers',
                   name ='markers',
                   marker=go.Marker(size=20,symbol=data['buyArrows'],color=data['buyColor']))
                   )

    fig.add_trace (go.Scatter(x=data['formatted_date'],
                   y=data['sells'],
                   mode='markers',
                   name ='markers',
                   marker=go.Marker(size=20,symbol=data['sellArrows'],color=data['sellColor']))
                   )
    #
    '''
    fig.show()


def plotChart (crypto_data):
    # Candlestick
    fig = go.Figure (
        data = [
            go.Candlestick (
                x = crypto_data.index,
                open = crypto_data.open,
                high = crypto_data.high,
                low = crypto_data.low,
                close = crypto_data.close
            ),
            go.Scatter (
                x = crypto_data.index,
                y = crypto_data.close.rolling (window = 4).mean (),
                mode = 'lines',
                name = '4SMA',
                line = {'color': 'pink', 'width': 4}
            ),
            go.Scatter (
                x = crypto_data.index,
                y = crypto_data.close.rolling (window = 8).mean (),
                mode = 'lines',
                name = '8SMA',
                line = {'color': 'purple', 'width': 4}
            ),
            go.Scatter (
                x = crypto_data.index,
                y = crypto_data.close.rolling(window=20).mean(),
                mode = 'lines',
                name = '20SMA',
                line = {'color': 'yellow', 'width': 4}
            ),
            go.Scatter (
                x = crypto_data.index,
                y = crypto_data.close.rolling (window = 50).mean (),
                mode = 'lines',
                name = '50SMA',
                line = {'color': 'blue', 'width': 4}
            ),
            go.Scatter (
                x = crypto_data.index,
                y = 10000 * (crypto_data.close.rolling(window=1).mean() - crypto_data.close.rolling(window=20).mean())/crypto_data.close.rolling(window=20).mean(),
                mode = 'lines',
                name = '20SMAext',
                line = {'color': 'green', 'width': 4}
            )
        ]
    )
    '''
    ,
    go.Scatter(
        x = crypto_data.index,
        y = crypto_data.close.rolling(window=8).mean(),
        mode = 'lines',
        name = '8SMA',
        line = {'color': 'purple', 'width': 4}
    ),
    go.Scatter(
        x = crypto_data.index,
        y = crypto_data.close.rolling(window=50).mean(),
        mode = 'lines',
        name = '50SMA',
        line = {'color': 'blue', 'width': 4}
    ),
    go.Scatter(
        x = crypto_data.index,
        y = crypto_data.close.rolling(window=200).mean(),
        mode = 'lines',
        name = '200SMA',
        line = {'color': 'purple'}
    )
    '''

    fig.update_layout(
        title = f'The Candlestick graph',
        xaxis_title = 'Date',
        yaxis_title = f'Price (USD)',
        xaxis_rangeslider_visible = True,
        plot_bgcolor='rgb(10,10,10)'
    )
    #fig.update_yaxes(tickprefix='$')
    fig.show()
