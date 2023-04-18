import pytest
import PySimpleGUI as sg

# Define the PySimpleGUI program to be tested
def create_gui():
    layout = [
        [sg.Text("Enter your name:"), sg.Input(key="-NAME-")],
        [sg.Button("Submit"), sg.Button("Cancel")],
    ]
    return sg.Window("My GUI", layout)

# Define a test case for the PySimpleGUI program
def test_gui():
    window = create_gui()
    window.read(timeout=1)
    assert window.FindElement("-NAME-").Get() == ""
    window.FindElement("-NAME-").Update("John Doe")
    window.FindElement("Submit").Click()
    event, values = window.read()
    assert event == "Submit"
    assert values["-NAME-"] == "John Doe"
    window.close()

# Run the test case
if __name__ == "__main__":
    pytest.main()
