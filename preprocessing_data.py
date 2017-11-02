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

# import time
# from selenium import webdriver
#
# profile = webdriver.FirefoxProfile()
# profile.set_preference('browser.download.folderList', 2)  # custom location
# profile.set_preference('browser.download.manager.showWhenStarting', False)
# profile.set_preference('browser.download.dir', '/tmp')
# profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'image/png')
#
# driver = webdriver.Firefox(firefox_profile=profile)
# import glob, os
# os.chdir("dataset/images")
# for file in glob.glob("*.html"):
#     #file:///home/ros/ROS/research/Deep_Stock_Representation_learning%20-%20from_candlestick_charts_to_investment_decisions/dataset/images/4100.html
#     driver.get("file:///home/ros/ROS/research/Deep_Stock_Representation_learning%20-%20from_candlestick_charts_to_investment_decisions/dataset/images/{}".format(file))
#     export_button = driver.find_element_by_xpath("//a[@data-title='Download plot as a png']")
#     export_button.click()
#     time.sleep(10)
#     driver.quit()
