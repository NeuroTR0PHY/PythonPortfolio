
# Print "hello, world!" to the terminal
import sys
from termcolor import colored, cprint
text = colored('Hello, World!', 'green', attrs=['reverse','blink'])
print(text)