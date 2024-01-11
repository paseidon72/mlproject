import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fandango = pd.read_csv('fandango_scrape.csv')
#fandango = fandango.corr()
fandango['YEAR'] = fandango['FILM'].apply(lambda title: title.split('(')[-1].replace(')', ''))
#fandango = fandango['YEAR'].value_counts()
#fandango = fandango.nlargest(10, 'VOTES')
#fandango = fandango[fandango['VOTES'] == 0]
#fandango = fandango[fandango['VOTES'] > 0]
fandango['STARS_DIFF'] = fandango['STARS'] - fandango['RATING']
fandango['STARS_DIFF'] = fandango['STARS_DIFF'].round(1)
all_sites = pd.read_csv('all_sites_scores.csv')
all_sites['Rotten_Diff'] = all_sites['RottenTomatoes'] - all_sites['RottenTomatoes_User']
all_sites['Rotten_Diff'].apply(abs).mean()
#all_sites = all_sites.nsmallest(5, 'Rotten_Diff')
#all_sites = all_sites.nlargest(5, 'Rotten_Diff')
#all_sites = all_sites.nlargest(1, 'IMDB_user_vote_count')
#all_sites = all_sites.nlargest(1, 'Metacritic_user_vote_count')
df = pd.merge(fandango, all_sites, on='FILM', how='inner')
df['RT_Norm'] = np.round(df['RottenTomatoes']/20, 1)
df['RTU_Norm'] = np.round(df['RottenTomatoes_User']/20, 1)
df['Meta_Norm'] = np.round(df['Metacritic']/20, 1)
df['Meta_U_Norm'] = np.round(df['Metacritic_User']/2, 1)
df['IMDB_Norm'] = np.round(df['IMDB']/2, 1)
#norm_scores = df[['STARS', 'RATING', 'RT_Norm', 'RTU_Norm', 'Meta_Norm', 'Meta_U_Norm', 'IMDB_Norm']]
norm_scores = df[['FILM', 'STARS', 'RATING', 'RT_Norm', 'RTU_Norm', 'Meta_Norm', 'Meta_U_Norm', 'IMDB_Norm']]
worst_film = norm_scores.nsmallest(10, 'RT_Norm')
# sns.kdeplot(data=fandango, x='RATING', clip=[0, 5], fill=True, label='True Rating')
# sns.kdeplot(data=fandango, x='STARS', clip=[0, 5], fill=True, label='Stars Displayed')
# plt.legend(loc=(0.8, 1.0))
#sns.countplot(data=fandango, x='YEAR')
#sns.scatterplot(data=fandango, y='VOTES', x='RATING')
#sns.countplot(data=fandango, x='STARS_DIFF', palette='magma')
# sns.scatterplot(data=all_sites, x='RottenTomatoes', y='RottenTomatoes_User')
# plt.xlim(0, 100)
# plt.ylim(0, 100)
#sns.histplot(data=all_sites, x='Rotten_Diff', kde=True, bins=25)
#sns.histplot(x=all_sites['Rotten_Diff'].apply(abs), kde=True, bins=25)
# sns.scatterplot(data=all_sites, x='Metacritic', y='Metacritic_User')
# plt.xlim(0, 100)
# plt.ylim(0, 10)
#sns.scatterplot(data=all_sites, x='Metacritic_user_vote_count', y='IMDB_user_vote_count')
# def move_legend(ax, new_loc, **kws):
#     old_legend = ax.legend_
#     handles = old_legend.legendHandles
#     labels = [t.get_text() for t in old_legend.get_texts()]
#     title = old_legend.get_title().get_text()
#     ax.legend(handles, labels, loc=new_loc, tile=title, **kws)
# fig, ax = plt.subplots(figsize=(15, 6), dpi=100)
#plt.figure(figsize=(15, 6), dpi=100)
#sns.kdeplot(data=norm_scores, clip=[0, 5], fill=True, palette='Set1')
#sns.kdeplot(data=norm_scores[['RT_Norm', 'STARS']], clip=[0, 5], fill=True, palette='Set1')
#sns.clustermap(norm_scores, cmap='magma', col_cluster=False)
#move_legend(ax, "upper left")
plt.figure(figsize=(15, 6), dpi=100)
sns.kdeplot(data=worst_film, clip=[0, 5], fill=True, palette='Set1')
print(worst_film)
plt.show()
