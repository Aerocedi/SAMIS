# Getting Started
This is the home section of the SAMIS code codex. Besides the main branch (**Dashboard**), there are four other branches, kindly check them to have the complete code. 
The Dashboard is a web application built on django with support of Javascript. It consist of Django, and standalone python library called SAMISgpt integrated into the webapp
- Requirements: Python 3.6 or >

* Download the SAMIS **Dashboard** as a zip file and extract OR  Create a folder called SAMIS_WEB and **clone** the files into it.


* After extracting or cloning


Run this command in the path of your folder:
```
python3 manage.py runserver
```

## Connect with OpenAI Backend LLM
* Visit and create an account with [OpenAI](https://platform.openai.com/)
* Create an account if you don’t have one
* Pay the amount you want for usage
* Click the button to “Create new secret key”
* Go to View API keys
* Obtain your API key and keep it safe
* In your the CONTROL.PY file, located in the folder, navigate to line 23 or find the section in code with `client = OpenAI(
    api_key=os.environ.get("YOUR_OPENAI_API_KEY"),
  )`
* Paste your key where it us required
* Now return to your terminal and add your key to the environment to prevent disconnection with backend due opening and closing of terminal

  #### On Windows:

- Use the search bar in the Start menu to find “Edit the system environment variables”.

- Click “Environment variables”

- Use the upper “New…” button to add a User variable

- Create a new variable called OPENAI_API_KEY and set the value to the secret key you got from your account settings on openai.com

#### For Mac or Linux:

- Find the .bashrc, .bash_profile, or .zshrc in your home directory

- Open the file in a text editor

- Add a new line to the file
  `export OPENAI_API_KEY=<your secret key>`

**OR** 
1. Run the following command in your terminal, replacing yourkey with your API key. 

``` 
echo "export OPENAI_API_KEY='yourkey'" >> ~/.zshrc
```
 

2. Update the shell with the new variable:

```
source ~/.zshrc
```
 

3. Confirm that you have set your environment variable using the following command. 

``` 
echo $OPENAI_API_KEY
```

## Connecting With Your Collaborative Robot
In our case we used an aerial robot (**DJI Tello Edu**) drone. 
*Ensure the battery is fully charged and robot placed in a open space with good clearance*. 
* Make sure your Wifi is on, then search for `Tello` signal
* Connect with the open network

## Viewing And Working With Dashboard 
Now navigate to the the localhost address usually `http://127.0.0.1:8000`
- The first page you will see is a SAMIS login (**Features to be updated in next realease)
- Kindly navigate to `http://127.0.0.1:8000`
