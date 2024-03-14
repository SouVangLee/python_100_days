# try and execute something and add exceptions
try:
    file = open("file.txt")
    dictionary = {"key": "value"}
    # print(dictionary["sadasd"])
    print(dictionary["key"])
# can except many errors
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("something")
# can get the error message by using "as error_message"
except KeyError as error_message:
    # print("That key does not exist")
    print(f"The key {error_message} does not exist.")
# else executes when no exceptions have occured
else:
    content = file.read()
    print(content)
# finally will execute no matter what happens
finally:
    file.close()
    print("File was closed.")

# can raise your own exceptions by:
# raise TypeError("your message")
# raise ValueError("your message")


# Learning to use JSON
import json

new_data = {
    "key": {"nested_key": "value"},
    # ...
}
# Use the following format to read json files
#
with open("file_name.json", "r") as data_file:
    data = json.load(data_file)
    # Update old data with new data
    data.update(new_data)
    print(data)

# Use the following format to write json files:
#
with open("file_name.json", "w") as data_file:
    json.dump(data, data_file, indent=4)
