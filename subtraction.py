import random

print("引き算クイズ！")
print("ゆなちゃんは何点とれるかな〜〜？？")
score = 0

for _ in range(10):
    valid_question = False

    while not valid_question:
        # 2桁の正の整数をランダムに選択
        a = random.randint(10, 99)
        b = random.randint(0, 9)

        # 2桁-1桁の引き算に限定し、答えがマイナスにならないようにする
        if a - b < 10:
            continue

        # 問題を作成
        question = f"{a} - {b}"
        correct_answer = a - b

        valid_question = True

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
