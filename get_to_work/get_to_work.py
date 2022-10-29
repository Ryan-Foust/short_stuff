#!/usr/bin/python3
from todoist_api_python.api import TodoistAPI
import subprocess

debug = True

with open("_todoist_token.txt", "r") as TDI_Token:
    token = TDI_Token.read()
    api = TodoistAPI(token)


def main():
    if debug:
        print("Starting main")

    if debug:
        print("Made example task")
        api.add_task(content="Example", project_id=2291523269)
    subprocess.Popen('/snap/bin/todoist')


if __name__ == '__main__':
    main()
