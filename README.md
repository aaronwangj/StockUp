# Stock 🆙

Use machine learning to guide your trading. Stock 🆙 uses Facebook Research's Prophet model to predict equities pricing based on historical prices. Read the Prophet paper [here](https://peerj.com/preprints/3190v2.pdf).

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the application's dependencies.

```bash
pip install -r requirements.txt
```

## Usage
Navigate to the project directory and start the Streamlit server.

```python
streamlit run app.py
```

### Landing Page
<p align="center">
<img src="/assets/landing-page.png?raw=true" align="middle" />  </p>

### Model Predictions
<p align="center">
<img src="/assets/predictions.png?raw=true" align="middle" />  </p>

### Regression Data
<p align="center">
<img src="/assets/regression-data.png?raw=true" align="middle" />  </p>

### Intraday Trading Data
<p align="center">
<img src="/assets/intraday.png?raw=true" align="middle" />  </p>

### Forecast Components
<p align="center">
<img src="/assets/forecast-components.png?raw=true" align="middle" />  </p>

### Raw Data on Recent Trading Days
<p align="center">
<img src="/assets/raw-data.png?raw=true" align="middle" />  </p>


## Deployment
The application is deployed through Streamlit Sharing and can be found [here](https://share.streamlit.io/aaronwangj/stockup/app.py). The project also supports Heroku deployment.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
