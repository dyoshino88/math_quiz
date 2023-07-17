import random
import tkinter as tk
import tkinter.messagebox

def check_answer():
    user_answer = entry.get()
    entry.delete(0, tk.END)  # 入力フィールドをクリア

    # 空の入力がある場合、再入力を促す
    while not user_answer.isdigit():
        tkinter.messagebox.showinfo("エラー", "ちゃんとこたえをかいてね")
        return
    
    user_answer = int(user_answer)

    # 正解の判定
    if user_answer == correct_answer:
        tkinter.messagebox.showinfo("◯", "すごい！せいかいだよ！！")
        add_score(10)
    else:
        tkinter.messagebox.showinfo("✗", f"おしい！\nせいかいは {correct_answer} だよ")

    # 次の問題へ進む
    ask_question()

def add_score(points):
    global score
    score += points
    score_label.configure(text=f"点数: {score} 点")

def ask_question():
    global current_question, correct_answer

    if current_question < 10:
        a = random.randint(10, 99)
        b = random.randint(1, 9)

        if random.choice([True, False]):
            question = f"{a} + {b}"
            correct_answer = a + b
        else:
            question = f"{b} + {a}"
            correct_answer = b + a

        question_label.configure(text=question)
        entry.delete(0, tk.END)  # 入力フィールドをクリア
        current_question += 1
    else:
        finish_quiz()

def finish_quiz():
    # クイズ終了時の処理
    result_text = f"点数: {score} 点\n"
    if score == 100:
        result_text += "すごい！100点まんてん！"
    elif score > 80:
        result_text += "よくできました！"
    elif score > 60:
        result_text += "できました！"
    else:
        result_text += "がんばろう！"

    result_label.configure(text=result_text)
    question_label.pack_forget()
    entry.pack_forget()
    submit_button.pack_forget()

root = tk.Tk()
root.geometry("500x300")
root.title("足し算クイズ")

# クイズ情報の初期化
print("足し算クイズ！")
print("ゆなちゃんは何点とれるかな？")
score = 0
current_question = 0
correct_answer = 0

# GUI部品の作成
question_label = tk.Label(root, text="", font=("Arial", 16))
question_label.pack()

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

submit_button = tk.Button(root, text="そうしん", command=check_answer)
submit_button.pack()

score_label = tk.Label(root, text="点数: 0 点", font=("Arial", 14))
score_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

# 最初の問題を表示
ask_question()

# ウィンドウを表示
root.mainloop()
