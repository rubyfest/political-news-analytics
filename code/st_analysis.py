import pandas as pd
import cache_saves
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
top_words_fox = cache_saves.open_df('top_words_fox')
top_words_cbs = cache_saves.open_df('top_words_cbs')
top_words_fox_proportion = cache_saves.open_df('top_words_fox_proportion')
top_words_cbs_proportion = cache_saves.open_df('top_words_cbs_proportion')
top_prop_diff_fox = cache_saves.open_df('top_prop_diff_fox')
top_prop_diff_cbs = cache_saves.open_df('top_prop_diff_cbs')
df=cache_saves.open_df('filtered_final_df')


st.title('Comparing Language in Fox and CBS Election Articles')
st.subheader(':grey[Count of top words:]',divider='grey')
col1, col2 = st.columns(2)
col1.caption(':red[FOX]')
col1.dataframe(top_words_fox)
col2.caption(':blue[CBS]')
col2.dataframe(top_words_cbs)
st.subheader(':grey[Proportion of top words:]',divider='grey')
col1, col2 = st.columns(2)
col1.write(':red[FOX]')
col1.dataframe(top_words_fox_proportion)
col2.write(':blue[CBS]')
col2.dataframe(top_words_cbs_proportion)
st.subheader(':grey[Top proportion difference of words:]',divider='grey')
col1, col2 = st.columns(2)
col1.write(':red[FOX]')
col1.dataframe(top_prop_diff_fox)
col2.write(':blue[CBS]')
col2.dataframe(top_prop_diff_cbs)

st.title('Visualizations')
colors=['blue','red']
st.caption(':violet[Hover over a plot and click the arrow icon to expand it]')
st.subheader(":grey[Plots of top word counts on average:]",divider='grey')
col1, col2 = st.columns(2)
col1.write(':red[FOX]')
figure, series1 = plt.subplots()
top_words_fox.plot(kind='bar', ax=series1, figsize=(10, 6), color=colors)
series1.set_title('Top words for Fox News by Count')
series1.set_ylabel('Word Count')
series1.set_xlabel('Word')
series1.set_xticklabels(series1.get_xticklabels(), rotation=45)
series1.legend(title='Source', fontsize=12)
col1.pyplot(figure)

col2.markdown(':blue[CBS]')
figure2, series2 = plt.subplots()
top_words_cbs.plot(kind='bar', ax=series2, figsize=(10, 6), color=colors)
series2.set_title('Top words for CBS News by Count')
series2.set_ylabel('Word Count')
series2.set_xlabel('Word')
series2.set_xticklabels(series2.get_xticklabels(), rotation=45)
series2.legend(title='Source', fontsize=12)
col2.pyplot(figure2)

st.subheader(":grey[Plots of top word proportions on average:]",divider='grey')
col1, col2 = st.columns(2)
col1.write(':red[FOX]')
figure3, series3 = plt.subplots()
top_words_fox_proportion.plot(kind='bar', ax=series3, figsize=(10, 6), color=colors)
series3.set_title('Top words for Fox News by Proportion')
series3.set_ylabel('Word Proportion')
series3.set_xlabel('Word')
series3.set_xticklabels(series3.get_xticklabels(), rotation=45)
series3.legend(title='Source', fontsize=12)
col1.pyplot(figure3)

col2.markdown(':blue[CBS]')
figure4, series4 = plt.subplots()
top_words_cbs_proportion.plot(kind='bar', ax=series4, figsize=(10, 6), color=colors)
series4.set_title('Top words for CBS News by Proportion')
series4.set_ylabel('Word Proportion')
series4.set_xlabel('Word')
series4.set_xticklabels(series4.get_xticklabels(), rotation=45)
series4.legend(title='Source', fontsize=12)
col2.pyplot(figure4)

st.subheader(":grey[Plots of top proportion difference of words:]",divider='grey')
col1, col2 = st.columns(2)
col1.write(':red[FOX]')
figure5, series5 = plt.subplots()
top_prop_diff_fox.plot(kind='bar', ax=series5, figsize=(10, 6), color=colors)
series5.set_title('Top proportion difference of words for Fox News')
series5.set_ylabel('Proportion Difference')
series5.set_xlabel('Word')
series5.set_xticklabels(series5.get_xticklabels(), rotation=45)
series5.legend(title='Source', fontsize=12)
col1.pyplot(figure5)

col2.markdown(':blue[CBS]')
figure6, series6 = plt.subplots()
top_prop_diff_cbs.plot(kind='bar', ax=series6, figsize=(10, 6), color=colors)
series6.set_title('Top proportion difference of words for CBS News')
series6.set_ylabel('Proportion Difference')
series6.set_xlabel('Word')
series6.set_xticklabels(series6.get_xticklabels(), rotation=45)
series6.legend(title='Source', fontsize=12)
col2.pyplot(figure6)