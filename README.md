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
* Pay the amount you want for usage
* Obtain your API key and keep it safe
* In your the CONTROL.PY file, located in the folder, navigate to line 23 or find the section in code with > client = OpenAI(
    api_key=os.environ.get("YOUR_OPENAI_API_KEY"),
)

## Connecting With Your Collaborative Robot
In our case we used an aerial robot (**DJI Tello Edu**) drone. 
*Ensure the battery is fully charged and robot placed in a open space with good clearance. 
