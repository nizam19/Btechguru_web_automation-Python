# Btechguru_web_automation-Python
A python3 script which automatically takes your btechguru assessment for you.

[![Video](https://img.youtube.com/vi/Uy_viddrNrc/0.jpg)](https://www.youtube.com/watch?v=Uy_viddrNrc)

Click :point_up: for video of how this works

### Requirements -

1. [Python 3](https://www.python.org/downloads/) (I used Python 3.8.1)
2. [Google Chrome](https://www.google.com/chrome/) (I used Version 80.0.3987.149 (Official Build) (64-bit))

### How to use -

If you already have [git](https://git-scm.com/downloads) installed head to any command line and
```bash
git clone https://github.com/nizam19/Btechguru_web_automation-Python.git

cd Btechguru_web_automation-Python/

py main.py <test-url> <activation-code> <email/username>
```
py works for me you can even try
```python3 main.py ...```
```python main.py ...```

#### Command line arguments

1. test link - Url of the test you are about to take
2. test activation code - Activation code for the test
3. email/username - Your btechguru.com email/username
4. password - Your btech guru password can be passed as a command line argument also
5. delay -  How many minutes after you want your test to end

### Follow up -
If you liked the project or would like to build upon this or this types of projects here are some ideas
1. Each question or html element of that question usually has a unique ID which can be stored in a database in the database after we got to know the result for that question and whenever another user encounters the same question that id can be looked up in the database and correct answer(if any) would be fetched.
2. ML and AI are the talk of the town right now, feel free to integrate those with these types of projects use them for identifying and solving famous questions or formulae or solving equations or even identifying the language for guess the output type of questions and predicting the answer your last card to play, would be searching the question on a search engine and choosing the most appropriate answer which matched the options.

Thanks for reading
