import sys


def get_input(input_message):
    """
    Asks the user for input from the command line

    Arguments:
        - string input_message: tell the user what kind of information to provide

    Returns:
        - false if command line input is newline character (blank line)
        - string line if command line input is nonempty
                 line contains all the command line arguments in a single string
    """
    sys.stdout.write(input_message + '\n' \
        + 'please write in the input field below \n' + 'input:  ')
    line = sys.stdin.readline()
    sys.stdout.write('\n')
    if line == '\n':
        return False
    else:
        return line
    

def evaluate_input(line):
    """
    Funny function that does not tolerate swear words and complains when
    questions are asked
    """

    swear_words = ['faen', 'helvete', 'satan', 'perkele', 'shitface']
    request_words = ['please', 'vær så snill', '?']

    for word in swear_words:
        if line:
            if word in line:
                sys.stdout.write('no swearing, please! \n')
                sys.exit(0)
        else:
            sys.exit(1)
    
    for word in request_words:
        if word in line:
            sys.stdout.write('I don\'t answer questions! \n \n')

line = True
while line:
    line = get_input('write something funny')
    evaluate_input(line)
    if line:
        sys.stdout.write('you wrote: ' + line + '\n' + '\n')
        sys.stdout.write('--'*10 + '\n')
    