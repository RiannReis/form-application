# Form Application
An application that registers users who will participate in a certain event. And where it is possible to see who is registered with special access.

## About:
This is a study project, made with the python language, using the flask framework and other libs. With the aim of developing a simple application that records participants and their respective information in a given table.

## Technologies used:

- Python
- Flask
- HTML & CSS
- VSCode
- PyJWT
- WTForms
- SQLAlchemy

## Installation:

- Clone the repository to your computer.

Need to have python installed and use pip for install the dependencies _(preferable in a venv)_
- `python -m venv .venv`
- `source .venv/Scripts/activate`
-  `pip install -r requirements.txt`

# How to Run:

After running the pip command:
- `flask --app form run `

And then access the application in the browser at: http://127.0.0.1:5000 and feel free to test the application :)


## Some Infos:
`http://127.0.0.1:5000`

- Main page, where participant information will be recorded.

`http://127.0.0.1:5000/success`

- Page where participants will be redirected after submitting their data.

`http://127.0.0.1:5000/login`

- Page where it will be possible to log in with the token to access the table with participant information.

`http://127.0.0.1:5000/auth`

- Page where the access token is generated.

`http://127.0.0.1:5000/tableDB?token=token`

- Page where the data is stored.

`http://127.0.0.1:5000/delete`

- Deletes all information and cleans the Database Table.
