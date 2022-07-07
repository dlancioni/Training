import sys

# Simplest example
# First argument is the script name, then other parameters
# cmd: python basic.py 111 222 333

print('Number of arguments:', len(sys.argv), 'arguments.') 
print('Argument List:', str(sys.argv))

if __name__ == "__main__":
    main(111)