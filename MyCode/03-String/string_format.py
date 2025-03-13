#
# %-Formatting
#
format = "Hello, %s. You are %d years old."
values = ("Alice", 30)
print(format % values)

#
# string Template
from string import Template

# Create a template with placeholders
template = Template("Hello, $name! Today is $day.")

# Substitute values (method 1: keyword args)
result = template.substitute(name="Alice", day="Monday")
print(result)  # Output: Hello, Alice! Today is Monday.

# Substitute values (method 2: dictionary)
data = {"name": "Bob", "day": "Tuesday"}
result = template.substitute(data)
print(result)  # Output: Hello, Bob! Today is Tuesday.

#
# Format method
#
format = "Hello, {}. You are {} years old."
print(format.format("Alice", 30))

#
# f-strings
#
name = "Alice"
age = 30
print(f"Hello, {name}. You are {age} years old.")
