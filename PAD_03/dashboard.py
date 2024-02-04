import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Tytuł dashboardu
st.title('Interaktywny Dashboard')

# Upload piku
data = st.file_uploader("Upload your dataset", type=['csv'])
if data is not None:
    data = pd.read_csv(data)
    data.columns = data.columns.str.strip()
    data.columns = data.columns.str.replace(' ', '')
    data = data.drop_duplicates()
    numeric_columns = ['xdimension', 'ydimension', 'zdimension', 'depth', 'table', 'price']
    data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')
    text_columns = ['clarity', 'color', 'cut']
    data[text_columns] = data[text_columns].apply(lambda x: x.str.lower())
    numeric_columns = ['xdimension', 'ydimension', 'zdimension', 'depth', 'table']
    data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')
    data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())
    data.dropna(subset=['price', 'carat', 'depth', 'table'], inplace=True)
    def remove_outliers(df, columns):
        for col in columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
        return df

    numerical_cols = ['carat', 'depth', 'table', 'price']
    data = remove_outliers(data, numerical_cols)

    # Wybór zmiennej do wizualizacji
    available_columns = [col for col in data.columns if col != 'table']
    option = st.selectbox(
        'Którą zmienną chcesz zobaczyć?',
         available_columns)
    # Pokaż wybraną zmienną
    st.write('Wybrana zmienna:', option)

    # Wizualizacja rozkładu wybranej zmiennej
    if data[option].dtype == 'object':
        fig, ax = plt.subplots()
        sns.countplot(x=option, data=data, ax=ax)
        st.pyplot(fig)
    else:
        st.dataframe(data[option].describe(), use_container_width=True)
    
    st.write('Próbka danych wybranej kolumny')
    st.dataframe(data[[option]].head(), use_container_width=True)

    # Wykres zależności ceny do <?>
    available_columns_price = [col for col in data.columns if col not in ['price', 'table']]
    selected_column = st.selectbox('Wybierz kolumnę do porównania z ceną', available_columns_price)

    # Generowanie i wyświetlanie wykresu
    if selected_column:
        fig, ax = plt.subplots()
        sns.scatterplot(x=selected_column, y='price', data=data)
        plt.xlabel(selected_column)
        plt.ylabel('Cena')
        st.pyplot(fig)


    st.write('Statyczne wykresy')

    # Rozkład carat
    fig1, ax1 = plt.subplots()
    data['carat'].hist(bins=30, ax=ax1)
    ax1.set_title('Rozkład zmiennej carat')
    ax1.set_xlabel('Carat')
    ax1.set_ylabel('Liczba wystąpień')
    st.pyplot(fig1)

    # Wykres gęstości
    fig2, ax2 = plt.subplots()
    sns.kdeplot(data['depth'], shade=True, ax=ax2)
    ax2.set_title('Rozkład zmiennej depth')
    ax2.set_xlabel('Depth')
    ax2.set_ylabel('Gęstość')
    st.pyplot(fig2)

    # Wykres punktowy dla ceny i carat
    fig3, ax3 = plt.subplots()
    sns.scatterplot(x='carat', y='price', data=data, ax=ax3)
    ax3.set_title('Zależność ceny od carat')
    ax3.set_xlabel('Carat')
    ax3.set_ylabel('Cena')
    st.pyplot(fig3)

    # Wykres pudełkowy dla ceny i cut
    fig4, ax4 = plt.subplots()
    sns.boxplot(x='cut', y='price', data=data, ax=ax4)
    ax4.set_title('Zależność ceny od jakości szlifu')
    ax4.set_xlabel('Cut')
    ax4.set_ylabel('Cena')
    st.pyplot(fig4)

    # Liczebność dla zmiennej 'cut'
    fig5, ax5 = plt.subplots()
    sns.countplot(x='cut', data=data, ax=ax5)
    ax5.set_title('Liczebność kategorii zmiennej cut')
    ax5.set_xlabel('Cut')
    ax5.set_ylabel('Liczba wystąpień')
    st.pyplot(fig5)

    # Rozkładu zmiennej 'color'
    fig6, ax6 = plt.subplots()
    sns.countplot(x='color', data=data, palette='hls', ax=ax6)
    ax6.set_title('Rozkład zmiennej color')
    ax6.set_xlabel('Kolor')
    ax6.set_ylabel('Liczba wystąpień')
    st.pyplot(fig6)