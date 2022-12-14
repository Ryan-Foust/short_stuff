#!/usr/bin/python3
from todoist_api_python.api import TodoistAPI
from tkinter import *
import json
import sys
import subprocess
import webbrowser


def modify_ctrl_vars():
    # modify control variables
    print("modify_ctrl_vars called")


def open_website(url):
    # webbrowser.open([url])
    print("open_website called")
    print("url passed:", url)


def open_app(path):
    # subprocess.Popen([path])
    print("open_app called")
    print("path passed:", path)


debug = False
stage = Tk()
stage.title("Get to Work Shortcut")
# stage.geometry("300x300+300+300")


def main(argv):
    if debug:
        print("Starting main")
        print("args received:", argv)

    # grab token to access task manager app
    with open(argv[1]) as TDI_Token:
        token = TDI_Token.read()
        api = TodoistAPI(token)

    # open and convert json to python types
    a_n_w_temp = open(argv[2])
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

        # make each checkbox, depending on whether the option points to website, or app
        app_check_button = Checkbutton(stage, text=app['name'], command=modify_ctrl_vars, padx=10, pady=5)
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
    main(sys.argv)
