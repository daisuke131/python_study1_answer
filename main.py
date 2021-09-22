# task1. 変数の使い方

"""
変数を使って、
「シンジとカヲルくんは仲良し！」
とprint文を使って表示させましょう。
"""

name1: str = "シンジ"
name2: str = "カヲルくん"

print(f"{name1}と{name2}は仲良し！")

# task2. if文の使い方

"""
task1のソースを改造して、name2が「使徒」だった場合に
「使徒です！」
とprint文で表示させましょう。
"""

if name2 == "使徒":
    print("使徒です！")

# task3. 配列の使い方

"""
以下の配列に、「アスカ」を追加しましょう。
"""

names: list = ["シンジ", "レイ", "カヲルくん"]
names.append("アスカ")

# task4. for文の使い方

"""
task3のソースコードを使用し、`names`のキャラクターをfor文を使って1行に1キャラずつ表示してみましょう。
"""

for name in names:
    print(name)

# task5. 関数の使い方

"""
task3とtask4を合体させて1つの関数にしましょう。
関数化したら、その関数を呼び出して結果が表示されることを確認しましょう。
"""


def show_name1() -> None:
    names: list = ["シンジ", "レイ", "カヲルくん"]
    names.append("アスカ")
    for name in names:
        print(name)


show_name1()


# task6. 引数を使う関数の使い方

"""
task5で作成した関数の引数に「マリ」を渡して、namesに追加しましょう。
リストに追加されているか表示されることを確認しましょう。
"""


def show_name2(mari: str):
    names: list = ["シンジ", "レイ", "カヲルくん"]
    names.append("アスカ")
    names.append(mari)
    for name in names:
        print(name)


show_name2("マリ")

# task7. 引数を使う関数の使い方

"""
if文で`in`を使い、入力した名前nameがnamesの中に含まれているか判定しましょう。
含まれている場合は「{入力した名前}はいます。」、
含まれてない場合は「{入力した名前}はいません。」と表示させましょう。
"""

names: list = ["シンジ", "レイ", "カヲルくん"]
input_name: str = input("名前を入力してください：")
if input_name in names:
    print(f"{input_name}はいます。")
else:
    print(f"{input_name}はいません。")
