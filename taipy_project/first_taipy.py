# A taipy scenario consists of nodes and tasks
# The nodes can be input nodes which can be from a database or user and output nodes
# The input node is passed through the task which will process the information and then output the information to the output node

############################## STARTING SCRIPTS ########################
# "Config" module lets us configure a taipy scenario 
# "Core" module processes the configuration 
# "Gui" module will add interactivity 

import taipy as tp 
from taipy import Config, Core, Gui

#create a function (build_message) which is the key element of the task block 
#it will take the name of user, we define that the data type is a string
def build_message(name: str, formal: int):
    if formal == "Yes":
        return f"Greetings, {name}."
    else:
        return f"Hey there, {name}!"

#configure the data nodes 
#the id is a key word argument 
#each of the nodes will have its own id
#input node
input_name_data_node_cfg= Config.configure_data_node(id="input_name")

#formality node for the toggle switch
formality_data_node_cfg= Config.configure_data_node(id="formality")

#output node
message_data_node_cfg= Config.configure_data_node(id="message")

#configure the task: task= node + function
build_msg_task_cfg= Config.configure_task(
    #it takes in several arguments
    "build_msg",                        #the id of the task to keep track of it
    build_message,                      #the function that will be used in the task
    [input_name_data_node_cfg, formality_data_node_cfg],          #the input node and formality node that the task will take in
    message_data_node_cfg               #the output node that the task will output to
)

#configure the scenario: scenario= tasks + nodes
scenario_cfg= Config.configure_scenario(
    "scenario",                        #the id of the scenario
    task_configs=[build_msg_task_cfg]  #the tasks that will be used in the scenario
)

############################## GRAPHICAL USER INTERFACE ########################
input_name= "Kami Mukami"
message= ""  
formality= ""  

#define the "page" variable which is the UI layout
#It could be Markdown, HTML, Python
#the "input_name" is a variable
#the "input" is the type
#adding a formality toggle switch for the user to select "Yes" or "No"

page= """
Name: <|{input_name}|input|>
<|submit|button|on_action=submit_scenario|> 

Message: <|{message}|text|>
 
Formality: <|{formality}|toggle|lov=Yes;No|>           
"""

######## Abstracting the "submit" functionality through a callback
#it allows the application to be interactive
#we will abstract the .submit() method to a function
#this allows us to arbitrarily handle user inputs
def submit_scenario(state):
    #the state parameter is specific to each user's session
    scenario.input_name.write(state.input_name)
    #write the formality of the state
    scenario.formality.write(state.formality)
    #submit()
    scenario.submit()
    #read the message as usual but pass it to the state
    state.message= scenario.message.read()

#build the scenario 
#it checks if the file is the main file in the project for it to run
if __name__ == "__main__":
    #instantiate the Core function that is necessary for taipy to run 
    Core().run()
    #build the scenario
    scenario= tp.create_scenario(scenario_cfg)

    # #write a value to the input_name node 
    # hello_scenario.input_name.write("Kami")
    # #submit the scenario to be run 
    # hello_scenario.submit()                #this build the scenario
    # #print the value of the final data node 
    # print(hello_scenario.message.read())   #use the id method to locate it 

    #run a GUI to interact with the scenario, instead of prescribing the functionality 
    Gui(page).run()

