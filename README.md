    virtualenv -p python3 venv
   
    source venv/bin/activate
 
    pip install -r requirements.txt

    run blockchain:
        ./main.py

    open webui:
        http://localhost:5000

    after fill and submit form will add new block in ./blockchain
