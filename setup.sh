mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
[theme]\n\
primaryColor = '#E694FF'\n\
backgroundColor = '#00172B'\n\
secondaryBackgroundColor = '#0083B8'\n\
textColor = '#C6CDD4'\n\
font = 'sans serif'\n\
" > ~/.streamlit/config.toml