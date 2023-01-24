import easygui
import pyperclip
if easygui.ccbox('选择：',title='选择',choices=('生成','解开')):
    enter1 = easygui.enterbox('要生成的文本')
    enter2 = easygui.enterbox('程度')
    enter2 = int(enter2)
    text = ''
    for i in enter1:
        text += chr(ord(i) + enter2)
    easygui.msgbox(text)
    pyperclip.copy(text)
    easygui.msgbox('已复制到剪贴板！')
else:
    enter1 = easygui.enterbox('要解开的文本')
    enter2 = easygui.enterbox('程度')
    enter2 = int(enter2)
    text = ''
    for i in enter1:
        text += chr(ord(i) - enter2)
    easygui.msgbox(text)
    pyperclip.copy(text)
    easygui.msgbox('已复制到剪贴板！')
