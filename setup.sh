mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
[theme]\n\
primaryColor = '#F63366'\n\
backgroundColor = '#000000'\n\
secondaryBackgroundColor = '#31333F'\n\
textColor = '#FAFAFA'\n\
font = 'sans serif'\n\
" > ~/.streamlit/config.toml