// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © af7bf3b8836b43f4ba9581e70d26cc

//@version=4
study( "My", overlay=true )

src = input(close)
var float extensionFactor = 1.7

var bool corridor = false
var bool band = true
var bool signals = false
var bool monthly = true
var bool weekly = false
var bool band_5_30 = false




// start :

// inputs
sma4 = input (1, title ='SMA 4')
ema21 = input(21,title='EMA21')
sma20 = input(20,title='SMA20')
sma200 = input(200,title='SMA 200')
sma8 = input (5, title = 'SMA 5')
ema50 = input(50,title='SMA 50W')
sma88 = input (8, title = 'SMA 8')
sma12 = input (12, title = 'SMA 12')
sma30 = input(30, title='SMA30')
psma30 = sma (src, sma30)
sma30plot = plot (psma30, color = color.blue,  linewidth=4, title='myLow')

// mas
pema21 = ema(src, ema21)
psma20 = sma(src, sma20)
psma200 = sma(src, sma200)
psma50 = sma(src, ema50)
psma8 = sma (src, sma8)
psma88 = sma (src, sma88)
psma12 = sma (src, sma12)
psma4 = sma(src, sma4)

//sma200plot = plot (psma200, color=color.purple, linewidth=5)

sma8plot = plot(psma8, color = #884dff, linewidth = 4)
sma4plot = plot(psma4, color = #ff61fa, linewidth = 4)
fill (sma8plot, sma4plot, color = (open > psma4 ? color.red : psma8 > psma4 ? color.red : color.green), transp = 60, editable=true)
plotshape (open > psma4 and psma4 > psma8, style = shape.triangledown, location = location.abovebar, color = #b06b6b, size = size.small, transp = 5)
plotshape (open > psma4 and psma4 > psma8 and psma8 > extensionFactor*pema21, style = shape.triangledown, location = location.abovebar, color = color.red, size = size.large, transp = 0)
plotshape (open > psma4 and psma4 > psma8 and psma8 > pema21, style = shape.triangleup, location = location.belowbar, color = color.green, size = size.small, transp = 0)
plotshape (open > psma4 and psma4 < psma8 and psma8 < pema21, style = shape.triangleup, location = location.belowbar, color = color.green, size = size.large, transp = 0)
plotshape (low < psma50, style = shape.triangleup, location = location.belowbar, color = color.green, size = size.large, transp = 0)


ema21plot = plot(pema21, color=#b1eb34,  linewidth=4, title='EMA21', transp = band ? 0 : 100)
sma20plot = plot(psma20, color=#ebc034, linewidth=4, title='SMA20', transp = band ? 0 : 100)
//sma12plot = plot(psma12, color=color.blue, linewidth=4, title='SMA12')

// corridor:
sma50plot = plot (psma50, color = corridor ? #1cff1c :  #afb6b2, linewidth=6, title = 'LOWER', transp = corridor ? 0 : 100)
upperPlot = plot (psma8 * 2.5, color = corridor ? #ff0000 :  #afb6b2, linewidth = 6, title = 'UPPER', transp = corridor ? 0 : 100)


c = color.green

if monthly
    //c := close < pema21 ? color.green : pema21 < psma20 ? color.green : close < psma8 ? pema21 < psma20 ? color.green :color.red : (close > psma8*1.7) ? color.red : pema21 > psma20 ? color.green :color.red
    c := (close < pema21) ? close < psma8 and pema21 > psma20 ? color.white : (color.green) : (pema21 < psma20) and (close > psma8) and ((close-psma8)/psma8 < .35) ? color.green : close < psma8 ? pema21 < psma20 ? color.green :color.red : (psma8 > pema21*2) ? color.red : pema21 > psma20 ? color.green :color.red

if weekly
    c := close < pema21 ? color.green : pema21 < psma20 ? color.green : close < psma88 ? pema21 < psma20 ? color.green :color.red : (close > psma88*1.7) ? color.red : pema21 > psma20 ? color.green :color.red
//fill (ema21plot, sma20plot, color = c, transp = band ? 44 : 100, editable=true)
fill (ema21plot, sma20plot, color = pema21 > psma20 ? color.green : color.red, transp = band ? 66 : 100, editable=true)
//plotshape (crossover (pema21, psma20), style = shape.triangleup, location = location.belowbar, color = color.green, size = size.small)
//plotshape (crossunder (close, psma8), style = shape.triangledown, location = location.abovebar, color = color.red, size = size.small)

plotshape (crossunder (psma8, pema21) and (close < pema21 or open < pema21), style = shape.triangleup, location = location.belowbar, color = color.green, size = size.small, transp = signals ? 0 : 100)
plotshape (close < psma50, style = shape.triangleup, location = location.belowbar, color = color.green, size = size.large, transp = signals ? 0 : 100)
plotshape (close < pema21 and close > psma8, style = shape.triangleup, location = location.belowbar, color = color.green, size = size.large, transp = signals ? 0 : 100)
plotshape ((close < open and close > psma8 and (open > psma8*extensionFactor or close > psma8*extensionFactor or high > psma8*extensionFactor) and pema21 > psma20), style = shape.triangledown, location = location.abovebar, color = color.red, size = size.large, transp = signals ? 0 : 100)
plotshape (((open > psma8 or close > psma8) and psma8 > pema21 and (psma8-psma20)/psma20 > 1.35), style = shape.triangledown, location = location.abovebar, color = color.red, size = size.small, transp = signals ? 0 : 100)

//color=pema21>psma20? color.green :color.red


// old (non filled):
//sma20 = sma(close, 20)
//ema21 = ema(close, 21)
//sma200 = sma( close, 200)
//plot( sma20, linewidth=4, color=color.green )
//plot( ema21, linewidth=4, color=color.blue )
//plot( sma200, linewidth=4, color=color.purple )
