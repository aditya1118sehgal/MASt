import plotly.graph_objects as go

def plotChart (crypto_data):
    #fig = make_subplots(specs=[[{"secondary_y": True}]])
    # Candlestick
    fig = go.Figure(
        data = [
            go.Candlestick(
                x = crypto_data.index,
                open = crypto_data.open,
                high = crypto_data.high,
                low = crypto_data.low,
                close = crypto_data.close
            ),
            go.Scatter(
                x = crypto_data.index,
                y = crypto_data.close.rolling(window=8).mean(),
                mode = 'lines',
                name = '8SMA',
                line = {'color': 'purple', 'width': 4}
            ),
            go.Scatter(
                x = crypto_data.index,
                y = crypto_data.close.rolling(window=20).mean(),
                mode = 'lines',
                name = '20SMA',
                line = {'color': 'yellow', 'width': 4}
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
        ]
    )

    fig.update_layout(
        title = f'The Candlestick graph',
        xaxis_title = 'Date',
        yaxis_title = f'Price (USD)',
        xaxis_rangeslider_visible = False,
        plot_bgcolor='rgb(10,10,10)'
    )
    fig.update_yaxes(tickprefix='$')
    fig.show()
