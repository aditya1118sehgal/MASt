import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

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
            y = data['sma4'],
            mode = 'lines',
            name = '4SMA',
            line = {'color': 'pink', 'width': 4}
        )
    )
    fig.add_trace (
        go.Scatter (
            x = data['formatted_date'],
            y = data['sma8'],
            mode = 'lines',
            name = '8SMA',
            line = {'color': 'purple', 'width': 4}
        )
    )
    fig.add_trace (
        go.Scatter (
            x = data['formatted_date'],
            y = data['sma20'],
            mode = 'lines',
            name = '20SMA',
            line = {'color': 'yellow', 'width': 4}
        )
    )
    fig.add_trace (
        go.Scatter (
            x = data['formatted_date'],
            y = data['sma50'],
            mode = 'lines',
            name = '50SMA',
            line = {'color': 'blue', 'width': 4}
        )
    )
    fig.add_trace (go.Bar(x=data['formatted_date'], y=data['sma20ext'], marker_color = 'rgba(167, 240, 242, .25)', name = 'sma20ext'),secondary_y=True)
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
    dist=5
    data['occurences'] = np.where(data.low < data.sma20, data.low - dist, data.high + dist)
    data['arrows'] = np.where(data['low'] < data['sma20'], 'triangle-up', 'triangle-down')
    data['color'] = np.where(data['low'] < data['sma20'], 'green', 'rgba(167, 240, 242, 0)')
    fig.add_trace (go.Scatter(x=data['formatted_date'],
                   y=data['occurences'],
                   mode='markers',
                   name ='markers',
                   marker=go.Marker(size=20,symbol=data["arrows"],color=data['color']))
                   )
    #

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
