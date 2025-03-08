
from authentication import AuthenticationService
from models import Config, ConfigDirector, Model,Director, ConfigAdapter
from chat_manager import ChatManager
from helpers import *
import os

if __name__ == "__main__":


    

    #I got everything to communicate to the API
    manager = AuthenticationService()
    manager.login()

    # User friendly structured model building clearly:
    model = Director.default_model()
    model_config_template = ConfigDirector.reliable_config() #default_config
    model_config = ConfigAdapter.adapt(model_config_template, model)
    print(model_config.get_params())
    
    
#    original_project_directory = "."
#    ai_project_directory = "../external/projects/ai_generated/base"
#    documents_directory="./patterns.md"
    
 #   project_content = read_project(original_project_directory)
 #   write_project(project_content, ai_project_directory)
 #   print(ai_project_directory)
    model.set_tools([read_project,safe_write_file, safe_read_file])
    manager = ChatManager(authenticator = manager)

 #   message = "Could you read my project in the current directory and give me an honest opinion on the patterns and design  using mark down and defining a clear set of improvement in order to pass to my facotring team. You can write this on "+documents_directory
    message = "Dog is a human as Cat is to ?"

    if manager.send_message(message):
        chatbot = [model_config, model]
        response = manager.get_response(chatbot) 
        print(response)
    else:
        print("Problems processing data")   
        
