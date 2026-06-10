
"""
# 
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Importar dados
    df = pd.read_csv('https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/main/epa-sea-level.csv')

    fig, ax = plt.subplots(figsize=(12, 6))

    # Scatter plot
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6, label='Data')

    # 1. Linha de melhor ajuste — todos os dados (1880 até 2050)
    slope1, intercept1, *_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years1 = range(df['Year'].min(), 2051)
    ax.plot(years1, [slope1 * y + intercept1 for y in years1],
            color='red', label='Best Fit Line (1880-2050)')

    # 2. Linha de melhor ajuste — apenas a partir de 2000
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, *_ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years2 = range(2000, 2051)
    ax.plot(years2, [slope2 * y + intercept2 for y in years2],
            color='green', label='Best Fit Line (2000-2050)')

    # Rótulos e título
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    fig.savefig('sea_level_plot.png')
    return fig

draw_plot()
plt.show()
