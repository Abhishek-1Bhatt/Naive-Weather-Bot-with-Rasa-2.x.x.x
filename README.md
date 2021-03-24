# Naive-Weather-Bot-with-Rasa-2.x.x.x
![Screenshot from 2021-03-24 23-46-16](https://user-images.githubusercontent.com/46929125/112364709-cf26b600-8cfc-11eb-9692-78ba087f5e58.png)
The above image shows the outputs of the weather bot in the terminal. The responses are fetched with the help of OpenWeatherMap API and processed in the actions.py file.
The training data is contained in the data folder. It contains stories, nlu, and rules files which are in yml format. Starting from RASA 2.x.x all the files need to be in yml format.
## In order to Reproduce the results:
- Install RASA with command: pip install rasa(same for terminal or cmd)
- Clone this repository
- Obtain the OpenWeatherMap API key and provide it as the value of api_key variable in actions.py file,
#### Now inside the folder where this repository is cloned
- Open a terminal and run the command: rasa run actions{Gets the endpoint for API calls up and running}
- Now in a separate terminal run : rasa shell {This runs the weather chat bot in your terminal}
