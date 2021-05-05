import streamlit as st
from datetime import date
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from util import load_data
from util import plot_raw_data
from footer import footer
import base64

st.set_page_config(page_title="Stock Price Prediction", page_icon="📈")

st.title('Stock Price Prediction')
st.markdown('Use machine learning to guide your trading.'
            + ' This application uses Facebook Research\'s Prophet model to predict equities pricing based on historical prices.'
            + ' Read the Prophet paper [here](https://peerj.com/preprints/3190v2.pdf).')


hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""

#hide hamburger menu
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

data = []
bad_input = st.text('')

selected_stock = st.text_input(label = "Ticker Symbol", max_chars = 5, help = "Example: GOOGL, AAPL, FB")

TODAY = date.today().strftime("%Y-%m-%d", )
START = st.date_input("Start Date", value = date(2019, 1, 1), min_value = date(2000, 1, 1), max_value = date.today(), help = "The date you wish the model to start training on")

#load data before button is even pushed
try:
    data = load_data(selected_stock, START, TODAY)
except:
    pass

n_years = st.slider('Years of Prediction (recommended 3 or less):', 1, 5, help = "How many years in the future you want to predict for")
period = n_years * 365

if st.button("Predict"):

    if len(data) == 0:
        bad_input = st.text('Please enter a valid ticker symbol to get started.')
    else:
        bad_input.empty()
        
        # Predict forecast with Prophet.
        df_train = data[['Date','Close']]
        df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

        m = Prophet()

        file_ = open("./assets/loading_animation.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        #set loading animation
        loading_text = st.text('The model is training. This will take a minute...')
        loading = st.markdown(f'<img src="data:image/gif;base64,{data_url}" style="width:350px; margin:auto; display:block;">',unsafe_allow_html=True,)  


        #train model
        m.fit(df_train)
        future = m.make_future_dataframe(periods=period)
        forecast = m.predict(future)

        #end loading animation
        loading_text.text('')
        loading.empty()

        if n_years == 1:
            st.subheader(f'Predictions for the Next Year')
        elif n_years >= 1:
            st.subheader(f'Predictions for the Next {n_years} years')
        fig1 = plot_plotly(m, forecast)
        st.plotly_chart(fig1, use_container_width = True)

        #Plot open/closes
        plot_raw_data(data)
        
        # Show and plot forecast
        st.subheader('Regression Data on Recent Trading Days')
        st.write(forecast.tail())

        st.subheader("Forecast components")
        fig2 = m.plot_components(forecast)
        st.write(fig2)

        st.subheader('Raw Data on Recent Trading Days')
        st.write(data.tail())

#footer
footer()
