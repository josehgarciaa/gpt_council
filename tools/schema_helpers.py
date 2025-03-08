import inspect
import json
import typing
from typing import Any, Callable, Dict, Optional, get_type_hints

def function_to_schema(func: Callable) -> Dict[str, Any]:
    """
    Convert a Python function (with type hints and docstring) into
    a JSON-serializable schema object, similar to the examples shown.

    :param func: The function to inspect.
    :return: A dictionary containing the schema.
    """
    # 1) Basic function metadata
    func_name = func.__name__
    docstring = inspect.getdoc(func) or ""  # Full docstring text
    # You can parse docstring to match your style; we keep it simple here

    # 2) Get signature & type hints
    sig = inspect.signature(func)
    type_hints = get_type_hints(func)

    # 3) Prepare the top-level schema structure
    schema = {
        "type": "function",
        "function": {
            "name": func_name,
            "description": docstring,
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
                "additionalProperties": False
            },
            # We’ll store the return type as well, though your examples often omit it
            "strict": True,  # or set dynamically if needed
        }
    }

    # 4) Build the parameters portion from signature
    for param_name, param in sig.parameters.items():
        # For each parameter, figure out:
        #   - type
        #   - optional or required
        #   - doc (extracted from docstring or fallback)
        #   - default value (if any)
        #   - etc.

        # Type hint
        annotated_type = type_hints.get(param_name, Any)
        # Convert Python type to JSON schema style string
        json_type = python_type_to_json_type(annotated_type)

        # Check if this param is required
        has_default = (param.default != inspect.Parameter.empty)
        if not has_default:
            schema["function"]["parameters"]["required"].append(param_name)

        # Attempt to find a short description for this param from docstring
        # (In practice, you'd parse the docstring carefully; we'll skip that.)
        param_description = f"Parameter: {param_name}"

        # Construct property definition
        schema["function"]["parameters"]["properties"][param_name] = {
            "type": json_type,
            "description": param_description
        }

        # If you want to reflect param.default in the schema, you can do so here
        # but your examples didn't do that explicitly.

    return schema

def python_type_to_json_type(py_type: Any) -> Any:
    """
    Helper to map Python type hints to JSON Schema types.
    This is simplistic. For more robust handling, check for
    generics like Union, Optional, etc.
    """
    if py_type == str:
        return "string"
    elif py_type == int or py_type == float:
        return "number"
    elif py_type == bool:
        return "boolean"
    # For Optional[...] or Union[..., None], you might return ["string", "null"], etc.
    # For demonstration, keep it simple:
    return "string"
