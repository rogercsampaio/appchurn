mkdir -p ~/.streamlit/


echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

echo "\
[general]\n\
email = \"rogersampaioo@gmail.com.br\"\n\
" > ~/.streamlit/credentials.toml
