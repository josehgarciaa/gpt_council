
from tools import function_to_schema


class ModelTool:

    def __init__(self) -> None:
        self.tool_name: str = False
        self.tool_schema: dict = None
        self.tool_function: object = None
        self.raw_last_answer = None
        self.last_answer = None
        
    def set_function(self, external_function: object)-> None:
        self.tool_schema = function_to_schema(external_function)
        self.tool_function = external_function
        self.tool_name = external_function.__name__
        return self
    
    def call_function(self, arguments: dict):
        self.raw_last_answer = self.tool_function(**arguments)
        self.last_answer="You got the answer:"+str(self.raw_last_answer)+"now report it to the user"
        return self.raw_last_answer
    
        
        
    

    
 
 