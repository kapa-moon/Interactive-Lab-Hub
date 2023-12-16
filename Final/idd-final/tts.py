import subprocess
def createAudio(itemName, section):
    # Define the command to be executed
    command = "echo '%s' | piper --model en_US-lessac-medium --output_file %s.wav" % (itemName, section)

    # Execute the command
    subprocess.run(command, shell=True, check=True)

createAudio("Here is your box! It might help you out!","present")