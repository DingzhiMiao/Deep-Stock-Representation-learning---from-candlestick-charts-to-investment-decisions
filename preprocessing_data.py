import pandas as pd
import plotly.offline as offline
import matplotlib.pyplot as plt
from plotly.tools import FigureFactory as FF
offline.init_notebook_mode()
# import plotly.graph_objs as go
#py.sign_in('rosdyana', 'eVtlDykeB8gMHmp6y4Ff')
# read stock data
df = pd.read_csv('^FTSE.csv', header=None, index_col=0)
# drop date and volume columns
df.drop(df.columns[[4, 5]], axis=1, inplace=True)
df = df.astype(str)
separators = pd.DataFrame(', ', df.index, df.columns[:-1])
separators[df.columns[-1]] = '\n'
# print (df + separators).sum(axis=1).sum()
data = df[1:]
# print(data.head())

for i in range(0, len(data), 20):

    c = data[i:i + 20]
    fig = FF.create_candlestick(
        open=c[1], high=c[2], low=c[3], close=c[4])

    fig['layout'].update({
        'xaxis': dict(visible=False),
        'yaxis': dict(visible=False),
        'paper_bgcolor': 'rgba(1,1,1,1)',
        'plot_bgcolor': 'rgba(1,1,1,1)'
    })
    #plot_mpl(fig, image='png')
    #py.image.save_as(fig, filename='dataset/images/{}.png'.format(i))
    offline.plot(fig, filename='dataset/images/{}.html'.format(i),
                     image='png', auto_open=False, show_link=False, image_filename='dataset/images/{}.png'.format(i))

# resize 224x224 imagemagick
# find . -maxdepth 1 -iname "*.png" | xargs -L1 -I{} convert -adaptive-resize 224x224! "{}" "{}"
