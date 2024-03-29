import sys

def file_content_reverse_copy(inputFilePath, outputFilePath):
    #読み込みファイルが見つからなければエラー
    try:
        with open(inputFilePath, "r") as file:
            content = file.read()
            with open(outputFilePath, "w") as file:
                file.write(''.join(reversed(content)))
    except FileNotFoundError:
        print("読み込みファイルが見つかりません。")
        exit()

def file_content_copy(inputFilePath, outputFilePath):
    #読み込みファイルが見つからなければエラー
    try:
        with open(inputFilePath, "r") as file:
            content = file.read()
            with open(outputFilePath, "w") as file:
                file.write(content)
    except FileNotFoundError:
        print("読み込みファイルが見つかりません。")
        exit()
        
def file_content_self_copy_specified_times(inputFilePath, count):
    #count変数が数値に変換できるかチェック
    try:
        count = int(count)
    except ValueError:
        print("引数が不正です。")
        exit()
    
    #読み込みファイルが見つからなければエラー
    try:
        with open(inputFilePath, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("読み込みファイルが見つかりません。")
        exit()
    
    with open(inputFilePath, "a") as file:
        for i in range(count - 1):
            file.write(content)

def file_content_replace_self_copy(inputFilePath, needle, newstring):
    #読み込みファイルが見つからなければエラー
    try:
        with open(inputFilePath, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("読み込みファイルが見つかりません。")
    
    with open(inputFilePath, "w") as file:
        replaceContent = content.replace(needle, newstring)
        file.write(replaceContent)


args = sys.argv[1:]

#コマンドの確認と引数の数のチェック
if args[0] == "reverse" and len(args) == 3:
    file_content_reverse_copy(args[1], args[2])
elif args[0] == "copy" and len(args) == 3:
    file_content_copy(args[1], args[2])
elif args[0] == "duplicate-contents" and len(args) == 3:
    file_content_self_copy_specified_times(args[1], args[2])
elif args[0] == "replace-string" and len(args) == 4:
    file_content_replace_self_copy(args[1], args[2], args[3])
else:
    print("コマンドが存在しないか、引数が足りません。")
