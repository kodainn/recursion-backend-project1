import sys
import random

#ゲーム開始の表示
sys.stdout.buffer.write(b"start guess the number game!!\n")
sys.stdout.buffer.flush()

#最小値を入力させる
sys.stdout.buffer.write(b"input min number: ")
sys.stdout.buffer.flush()
minNumber = int(sys.stdin.buffer.readline().strip())

#最大値を入力させる
sys.stdout.buffer.write(b"input max number: ")
sys.stdout.buffer.flush()
maxNumber = int(sys.stdin.buffer.readline().strip())

#最小値の方が最大値より大きいとき不正とみなしてゲーム終了
if minNumber > maxNumber:
    sys.stdout.buffer.write(b"unauthorized Error: The minimum value is greater than the maximum value!!\n")
    exit()

#答えれる回数は3回まで
randomAnswer = random.randint(minNumber, maxNumber)
answerNumberStr = [b"first", b"second", b"last"]
for i in range(3):
    sys.stdout.buffer.write(answerNumberStr[i] + b' answer: ')
    sys.stdout.buffer.flush()
    userAnswer = int(sys.stdin.buffer.readline().strip())
    
    #答えがあっていたらゲーム終了
    if userAnswer == randomAnswer:
        sys.stdout.buffer.write(b"The correct answer is: That's correct!!\n")
        exit()
    
    #三回目間違っていてもこれは表示しない
    if i < 2:
        sys.stdout.buffer.write(b"The correct phrase is: Incorrect. Once again.\n")
        #sys.stdout.buffer.flush()

sys.stdout.buffer.write(b"Unfortunately, that's incorrect.\n")