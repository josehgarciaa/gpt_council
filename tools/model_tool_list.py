
from tools import ModelTool

class ModelToolList:
    """
    A container for ModelTool objects that prevents duplicate names,
    allows iteration, and supports name-based lookups.
    """
    def __init__(self):
        # Use a dict keyed by tool_name to prevent duplicates and allow quick lookup
        self._tools = {}

    def add_tool(self, tool: ModelTool) -> None:
        """
        Add a ModelTool to the list, ensuring no two tools have the same name.
        Raises a ValueError if the name already exists.
        """
        if tool.tool_name in self._tools:
            raise ValueError(f"Tool with name '{tool.tool_name}' already exists.")
        self._tools[tool.tool_name] = tool

    def get_tool_by_name(self, name: str) -> ModelTool:
        """
        Retrieve a ModelTool by its tool_name.
        Returns None if no such tool is found.
        """
        return self._tools.get(name)

    def get_all_functions(self) -> list:
        """
        Return a list of the `tool_function` objects from all ModelTools.
        """
        return [tool.tool_function for tool in self._tools.values()]

    def get_all_schemas(self) -> list:
        """
        Return a list of the `tool_schema` dictionaries from all ModelTools.
        """
        return [tool.tool_schema for tool in self._tools.values()]

    def __iter__(self):
        """
        Make the container iterable, returning each ModelTool object in the collection.
        """
        return iter(self._tools.values())

    def __len__(self):
        """
        Return the number of ModelTools in the container.
        """
        return len(self._tools)


    
 
 