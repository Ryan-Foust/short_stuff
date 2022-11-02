#!/usr/bin/python3
from todoist_api_python.api import TodoistAPI
from tkinter import *
import json
import subprocess
import webbrowser

def open_website():
    # webbrowser.open([url])
    print("open_website called")

def open_app():
    # subprocess.Popen([path])
    print("open_app called")

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

    elements = []
    # for each element in json data
    for app in apps_and_websites:
        if debug:
            print(app['name'])

        # make each checkbox, depending on whether the
        if app['is_website']:
            app_check_button = Checkbutton(stage, text=app['name'], command=open_website)
            elements.append(app_check_button)
        else:
            app_check_button = Checkbutton(stage, text=app['name'], command=open_app)
            elements.append(app_check_button)

    for elem in elements:
        elem.pack()

    # make continue button
    continue_button = Button(stage, text="Continue")
    continue_button.pack()

    # make exit button
    exit_button = Button(stage, text="Exit", command=stage.destroy)
    exit_button.pack()

    # start GUI portion
    stage.mainloop()


if __name__ == '__main__':
    main()
