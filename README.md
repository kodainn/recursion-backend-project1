# Recursion バックエンドプロジェクト 1

- このコースでは、コンピュータシステムにおけるアプリケーションプログラムについて詳しく学習します。
- コンピュータシステムの概要
- コンパイルとインタプリタ
- オペレーションシステムの基礎知識(カーネル、システムコール、シェル、インターフェース、環境構築)
- データストリーム(パイプ、ソケット)

# GuessTheNumberGame(標準的なストリームを使ったプログラム)

- guess_the_number_game.py ファイル参照

# FileManipulatorProgram(コマンドラインからのファイル操作プログラム)

- file_manipulator.py ファイル参照

# MarkdownToHTMLConverter(md ファイルから html ファイルに変換するプログラム)

- file-converter.py ファイル参照

# プログラムの実行方法
- cd プロジェクトディレクトリ直下
- イメージの作成 docker image build --tag ubuntu-my-custom .
- コンテナの立ち上げ docker container run --rm -it --mount type=bind,source="$(pwd)",target=/python_practice ubuntu-my-custom bash
