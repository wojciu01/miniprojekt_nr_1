# miniprojekt_nr_1
How to open a test

1. Setup the virtualenv or use the existing.

   - Python2:

      - Prepare virtualenv
      ```
      source /usr/bin/virtualenvwrapper.sh
      mkvirtualenv projekt-selenium
      ```
      
     - Continue working with virtualenv:
      ```
      workon projekt-selenium
      ```
    - Python3:

      - create python virtualenv
      ```
      python3 -m venv .venv
      ```
      - activate the venv
      ```
      source .venv/bin/activate
      ```

2. Install the deps if needed:

```
pip install -r requirements.txt
```

3. Get the driver:

   - chrome (check https://sites.google.com/a/chromium.org/chromedriver/):
       ```
       wget https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip
       unzip chromedriver_linux64.zip
       ```

   - firefox:
       ```
       wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz
       tar -xvzf geckodriver*tar.gz
       chmod +x geckodriver*
       ```

#How to run
```
  export PATH=$PATH:$(pwd)
  python auto_search.py
```
