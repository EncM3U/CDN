import PySimpleGUI as sg

sg.ChangeLookAndFeel('SystemDefault')

form = sg.FlexForm('状态栏标题', default_element_size=(40, 1))

column1 = [[sg.Text('Column 1', background_color='#fff', justification='center', size=(10,1))],

               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],

               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],

               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

layout = [

        [sg.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25))],

        [sg.Text('Here is some text.... and a place to enter text')],

        [sg.InputText('This is my text')],

        [sg.Checkbox('My first checkbox!'), sg.Checkbox('My second checkbox!', default=True)],

        [sg.Radio('My first Radio!      ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],

        [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),

         sg.Multiline(default_text='A second multi-line', size=(35, 3))],

        [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 3)),

         sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],

        [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),

         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),

         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),

         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),

         sg.Column(column1, background_color='#fff')],

        [sg.Text('_'  * 80)],

        [sg.Text('Choose A Folder', size=(35, 1))],

        [sg.Text('你的文件夹', size=(15, 1), auto_size_text=False, justification='right'),

         sg.InputText('默认文件夹'), sg.FolderBrowse("选择文件夹")],

        [sg.Submit("确定"), sg.Cancel("取消")]

         ]

button, values = form.Layout(layout).Read()
print(values[8])
sg.Popup(button, values)
