
"""

# 
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Importar dados
df = pd.read_csv('https://raw.githubusercontent.com/freeCodeCamp/boilerplate-medical-data-visualizer/main/medical_examination.csv')

# 2. Coluna overweight
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# 3. Normalizar cholesterol e gluc
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# 4. Gráfico categórico
def draw_cat_plot():
    # 5. DataFrame para catplot
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Agrupar e contar
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7. Criar catplot
    g = sns.catplot(data=df_cat, x='variable', y='total', hue='value',
                    col='cardio', kind='bar')

    # 8. Salvar figura
    fig = g.fig

    # 9. Não modificar
    fig.savefig('catplot.png')
    return fig


# 10. Mapa de calor
def draw_heat_map():
    # 11. Limpar dados
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Matriz de correlação
    corr = df_heat.corr()

    # 13. Máscara triângulo superior
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True

    # 14. Configurar figura
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15. Heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', ax=ax,
                center=0, vmin=-0.1, vmax=0.3, square=True, linewidths=0.5)

    # 16. Não modificar
    fig.savefig('heatmap.png')
    return fig


# Rodar e exibir
draw_cat_plot()
plt.show()

draw_heat_map()
plt.show()
