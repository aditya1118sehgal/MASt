// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/

//@version=4
study( "M", overlay=true )

src = input(close)

pema21 = ema(src, input(21,title='EMA21'))
psma20 = sma(src, input(20,title='SMA20'))

ema21plot = plot(pema21, color=#f17a0afc,  linewidth=4, title='EMA21', transp = 0)
sma20plot = plot(psma20, color=#b3ff01, linewidth=4, title='SMA20', transp = 0)
sma50plot = plot (sma(src, input(50,title='SMA 50')), color = #52fa03, linewidth=4)
sma100plot = plot (sma(src, input(100,title='SMA 100')), color=#03fa2c, linewidth=5)
sma200plot = plot (sma(src, input(200,title='SMA 200')), color=color.rgb(9, 246, 21), linewidth=6)
plot (sma(src, input(300,title='SMA300')), color=#03fa8b, linewidth=6)
plot (pema21 * 1.5, color = #f2525d, linewidth = 2, title = 'UPPER')
plot (pema21 * 2, color = #f2525d, linewidth = 3, title = 'UPPER')
plot (pema21 * 2.5, color = #f2525d, linewidth = 4, title = 'UPPER')
plot (pema21 * 3, color = #f2525d, linewidth = 5, title = 'UPPER')

fill (ema21plot, sma20plot, color = pema21 > psma20 ? color.red : color.green, transp = 66, editable=true)


