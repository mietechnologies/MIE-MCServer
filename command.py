from util.configuration import RCON
from util.syslog import log
from rcon import Client

def runCommand(command: str):
    RCON.read()
    if RCON.enabled and RCON.password != "":
        with Client("mieserver.ddns.net",
                    RCON.port,
                    passwd=RCON.password) as client:

            response = client.run(command)
            __handleResponse(response, command)
    else:
        log("ERR: RCON has not been correctly initialized.")

def runTerminal(commands: list[str] = None):
    if RCON.enabled and RCON.password != "":
        with Client("mieserver.ddns.net",
                    RCON.port,
                    passwd=RCON.password) as client:
            
            if commands:
                for command in commands:
                    response = client.run(command)
                    __handleResponse(response, command)
            else:
                exit_command = "!exit"
                user_input = ""

                while (user_input != exit_command):
                    user_input = input(">> ")
                    response = client.run(user_input)
                    __handleResponse(response, user_input)


def __handleResponse(response: str, command: str):
    invalid_responses = ["Unknown command",
                         "Expected whitespace",
                         "Invalid or unknown"]
    
    if response in invalid_responses:
        log("Could not execute command [{}]: {}".format(command,
                                                        response))
    else:
        log(response)
