#!/usr/bin/python3
from todoist_api_python.api import TodoistAPI
from tkinter import *
import json
import subprocess
import webbrowser

debug = False
stage = Tk()
stage.title("Get to Work Shortcut")
stage.geometry("300x300+300+300")


def main():
    if debug:
        print("Starting main")

    # grab token to access task manager app
    with open('/home/ryan-foust/Desktop/prog/PycharmProjects/short_stuff/get_to_work/_todoist_token.txt', "r") as TDI_Token:
        token = TDI_Token.read()
        api = TodoistAPI(token)

    # open and convert json to python types
    a_n_w_temp = open("/home/ryan-foust/Desktop/prog/PycharmProjects/short_stuff/get_to_work/_apps_and_websites.json")
    to_load = a_n_w_temp.read()
    apps_and_websites = json.loads(to_load)

    # check that json data made it
    if debug:
        print(apps_and_websites)
        print(type(apps_and_websites))

    # for each element in json data
    for app in apps_and_websites:
        if debug:
            print(app['name'])

        # make each checkbox
        app_check_button = Checkbutton(stage, text=app['name'])
        app_check_button.pack()

    continue_button = Button(stage, text="Continue")
    exit_button = Button(stage, text="Exit", command=stage.destroy)
    continue_button.pack()
    exit_button.pack()

    stage.mainloop()

    if debug:
        print("Made example task")
        api.add_task(content="Example", project_id=2291523269)
    # subprocess.Popen('/snap/bin/todoist')
    # webbrowser.open("https://calendar.google.com/calendar/u/0/r")


if __name__ == '__main__':
    main()
