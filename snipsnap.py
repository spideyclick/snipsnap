import pyperclip, time, multiprocessing, ctypes, os

def scanClipboard(historyList):
    oldClipboardContent = ""
    while True:
        currentClipBoardContent = pyperclip.paste()
        if oldClipboardContent != currentClipBoardContent and len(currentClipBoardContent) < 5000:
            historyList.append(currentClipBoardContent)
            oldClipboardContent = currentClipBoardContent
            if len(historyList) > 10:
                historyList.pop(0)
        time.sleep(0.2)

def pcopy(text):
    pyperclip.copy(text)
    print()
    print(text)

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    historyList = manager.list()
    scanProcess = multiprocessing.Process(target=scanClipboard, args=(historyList,))
    scanProcess.start()
    while True:
        operation=input('Enter command:').lower()
        text=pyperclip.paste().lower()
        if operation[0:2] == 'hi':
            for i, item in enumerate(historyList[::-1]):
                if i == 0:
                    print('Current:')
                else:
                    print("\n" + str(i) + ".")
                print(item)
            copyItem = input('\n\nPress number to copy or Enter to close...')
            if copyItem.isdigit():
                copyItem=int(copyItem)
                if copyItem != '' and copyItem > 0 and copyItem <= len(historyList):
                    pyperclip.copy(historyList[len(historyList)-copyItem-1])
            os.system('cls')
            continue
        elif operation[0:2] == 'up':
            pcopy(text.upper())
        elif operation[0:2] == 'lo':
            pcopy(text.lower())
        elif operation[0:2] == 'ti':
            pcopy(text.title().replace(' And ', ' & '))
        elif operation[0:2] == 'ip':
            while text[0:1] == '0':
                text=text[1:]
            while '.0' in text:
                text=text.replace('.0', '.')
            if '..' in text:
                text=text.replace('..', '.0.')
            pcopy(text)
        elif operation[0:2] == 'sh':
            removeChars=' :-().'
            for character in removeChars:
                text=text.replace(character, '')
            pcopy(text.upper())
        elif operation[0:2] == 'ma': # 0010e784dc7e to 00:10:E7:84:DC:7E
            text=text.replace('-', '').replace(':', '').upper()
            if '-' in operation:
                text=str("{0}-{1}-{2}-{3}-{4}-{5}".format(text[0:2], text[2:4], text[4:6], text[6:8], text[8:10], text[10:12]))
            else:
                text=str("{0}:{1}:{2}:{3}:{4}:{5}".format(text[0:2], text[2:4], text[4:6], text[6:8], text[8:10], text[10:12]))
            pcopy(text)
        elif operation[0:2] == 'ph':
            removeChars=' :-().'
            for character in removeChars:
                text=text.replace(character, '')
            if not text.isdigit():
                print("Not a number? " + str(text))
                time.sleep(1)
            if '.' in operation:
                text="{0}.{1}.{2}".format(text[0:3], text[3:6], text[6:])
            else:
                text="({0}) {1}-{2}".format(text[0:3], text[3:6], text[6:])
            pcopy(text)
        elif operation[0:2] == 'ex':
            scanProcess.terminate()
            scanProcess.join()
            exit()
        else:
            print('available commands are history, mac, short, upper, lower, title.')
            continue
        time.sleep(1)
        os.system('cls')
