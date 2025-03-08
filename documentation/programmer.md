# How to Use the 'raise' Statement in Python

In Python, the `raise` statement is used to trigger an exception. It allows you to disrupt the normal flow of a program when something unexpected happens.

## Basic Usage

You can raise a built-in exception by specifying its type along with an optional error message:

```python
raise ValueError("Invalid value provided!")
```

This will immediately stop the execution of the program unless the exception is caught and handled.

## Handling Raised Exceptions

You can use a try-except block to catch and handle exceptions:

```python
try:
    # Code that might throw an exception
    raise ValueError("Invalid value provided!")
except ValueError as e:
    print(f"Caught an error: {e}")
```

## Creating Custom Exceptions

It is often useful to define your own exception types by subclassing from the built-in `Exception` class:

```python
class MyCustomError(Exception):
    pass

raise MyCustomError("Something went wrong in my application")
```

## Re-raising Exceptions

Sometimes you might want to catch an exception, perform some action (like logging), and then re-raise the same exception:

```python
try:
    # Code that might throw an exception
    raise RuntimeError("An error occurred")
except RuntimeError as e:
    # Do some logging or cleanup
    print("Logging error:", e)
    raise  # Re-raise the caught exception
```

## Summary

- Use `raise` to trigger exceptions when necessary.
- You can pass an exception instance or exception type with an optional message.
- Use try-except blocks to handle exceptions gracefully.
- Create custom exceptions by subclassing from `Exception` for more specific error handling.
