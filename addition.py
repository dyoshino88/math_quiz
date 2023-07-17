import random
print("足し算クイズ！")
print("ゆなちゃんは何点とれるかな〜〜？？")
score = 0

for _ in range(10):
    # 2桁または1桁の正の整数をランダムに選択
    a = random.randint(10, 99)
    b = random.randint(1, 9)

    # ランダムに順序を決定して問題を作成
    if random.choice([True, False]):
        question = f"{a} + {b}"
        correct_answer = a + b
    else:
        question = f"{b} + {a}"
        correct_answer = b + a

    # 問題を表示し、答えを入力させる
    user_answer = input(f"{question} = ")

    # 空の入力がある場合、答えを再入力させる
    while not user_answer.isdigit():
        print("ちゃんとこたえをかいてね〜〜！")
        user_answer = input(f"{question} = ")

    user_answer = int(user_answer)

    # 正解の判定
    if user_answer == correct_answer:
        print("すごい！せいかいだよ！！")
        score += 10
    else:
        print("おしい！")
        print("せいかいは", correct_answer, "だよ〜〜！")

print("点数:", score, "点")
if score == 100:
    print("すごい！100点まんてん！")
elif  score > 80:
    print("よくできました！！")
elif score > 60:
    print("できました！")
else:
    print("がんばろう！")

