import sys
import markdown

def convert_markdown_to_html(inputFilePath, outputFilePath):
    #読み込みファイルが見つからなければエラー
    try:
        with open(inputFilePath, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("ファイルが見つかりません。")
        exit()
    
    #マークダウン記法をhtmlタグへ変換
    html = markdown.markdown(content)
    
    with open(outputFilePath, "w") as file:
        file.write(html)

args = sys.argv[1:]

if args[0] == "markdown" and len(args) == 3:
    convert_markdown_to_html(args[1], args[2])
else:
    print("コマンドが存在しないか、引数が足りません。")