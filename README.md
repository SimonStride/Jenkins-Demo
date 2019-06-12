# Jenkins-Demo

## First run

    virtualenv env

    .\env\Scripts\activate

    pip install -r requirements.txt

## Subsequent runs

    .\env\Scripts\activate

Run the following after installing any additional libraries/depedencies

    pip freeze > requirements.txt
