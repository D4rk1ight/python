from pywinauto import Application

WINDOW_TITLE = "Sound Devices"

try:
    app = Application(backend="win32").connect(title=WINDOW_TITLE)
    window = app.window(title=WINDOW_TITLE)

    DEVICES = [window.print_control_identifiers()]

except Exception as e:
    print("Не удалось прочитать данные".format(e))

# with open("output_device_list.cmd", mode="r+w", encoding="utf-8") as file:
#     content = file.read()
#     print(content)
