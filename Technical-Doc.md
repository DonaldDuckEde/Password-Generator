# Technical Documentation: **The EasyPass Function**

The EasyPass function is a Python function that generates a random password of a specified length, with options to include uppercase letters and digits. The function takes three arguments:

* **length:** an integer that specifies the length of the password to be generated.
* **upper:** a boolean that specifies whether to include uppercase letters in the password (default is False).
* **digits:** a boolean that specifies whether to include digits in the password (default is False).


The function uses the random module and the string module to generate a password consisting of randomly chosen characters from a set of lowercase letters, uppercase letters, and digits. The password is then returned as a string.