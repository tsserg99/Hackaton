# Hackaton

This project uses **python3**.

Steps to run via ***Docker***:
1. git clone https://github.com/tsserg99/Hackaton.git
2. cd Hackaton
3. docker build -t kvaratop/grechapp . 
4. docker run -d -t -p 8081:5000 kvaratop/grechapp:latest
5. now you can access the webapp by address: 
   http://localhost:8081

Or you can find the webapp deployed via ***Heroku*** by following link:
https://grechapp.herokuapp.com
