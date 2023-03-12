from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication,QButtonGroup, QWidget, QGroupBox, QRadioButton, QPushButton, QLabel, QHBoxLayout, QVBoxLayout 
from random import shuffle 
from random import *
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


app = QApplication([]) 
window = QWidget() 
window.setWindowTitle('Jokes') 
RadioGroupBox = QGroupBox('Варианты ответа') 
question_list = []
question_list.append(
    Question("государственный язык португалии", 'Португальский', 'Английский', 'Испанский', ' Французский')
    )
question_list.append(
    Question("Кем или чем ты являешся если ты разваливаешся","Советский союз","Пизанская башня","песочный замок", "старый бабушкин телевизор")
    )
question_list.append(
    Question('ИЗ точки А в точку В едет твоя кукуха со скоростью света. Вопрос: кто такая света?', '880965.201 мax', 'Штирлиц', "Тема", "Имя")
)
question_list.append(
    Question('Вопрос: Кто?','Я','Человек','Арбуз','кто-то')
)
question_list.append(
    Question('Абдул?','Да','Нет','Возможно','кто?')
)
window.score = 0
window.total = 0
Ben = QPushButton('WHO') 
window.cur_question = - 1
rbtn_1 = QRadioButton('1') 
rbtn_2 = QRadioButton('2') 
rbtn_3 = QRadioButton('3') 
rbtn_4 = QRadioButton('4') 
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1) 
RadioGroup.addButton(rbtn_2) 
RadioGroup.addButton(rbtn_3) 
RadioGroup.addButton(rbtn_4) 
layout_ans1 = QVBoxLayout() 
layout_ans1.addWidget(rbtn_1) 
layout_ans1.addWidget(rbtn_2) 
layout_ans2 = QVBoxLayout() 
layout_ans2.addWidget(rbtn_3) 
layout_ans2.addWidget(rbtn_4) 
layout_ans_main = QHBoxLayout() 
layout_ans_main.addLayout(layout_ans1) 
layout_ans_main.addLayout(layout_ans2) 
RadioGroupBox.setLayout(layout_ans_main) 
AnswerGroupBox = QGroupBox('Vernij variant') 
lbl_result = QLabel('ggg') 
lbl_correct = QLabel('You shell not pass') 
layout_res = QVBoxLayout() 
layout_res.addWidget(lbl_result,alignment = (Qt.AlignHCenter|Qt.AlignVCenter)) 
layout_res.addWidget(lbl_correct,alignment = (Qt.AlignHCenter|Qt.AlignVCenter)) 
AnswerGroupBox.setLayout(layout_res) 
lbl_Question = QLabel('Вопрос: ЧЕ?') 
line1 = QHBoxLayout() 
line2 = QHBoxLayout() 
line3 = QHBoxLayout() 
line1.addWidget(lbl_Question,alignment = (Qt.AlignHCenter|Qt.AlignVCenter)) 
line2.addWidget(RadioGroupBox) 
line2.addWidget(AnswerGroupBox) 
RadioGroupBox.hide() 
line3.addWidget(Ben) 
main_layout = QVBoxLayout() 
window.setLayout(main_layout) 
main_layout.addLayout(line1,stretch = 2) 
main_layout.addLayout(line2,stretch = 8) 
main_layout.addLayout(line3,stretch = 1) 
main_layout.addStretch(1) 
main_layout.setSpacing(1) 

def show_result(): 
    RadioGroupBox.hide() 
    AnswerGroupBox.show() 
    Ben.setText('AUF') 
     
def show_question(): 
    AnswerGroupBox.hide() 
    RadioGroupBox.show() 
    Ben.setText('WHO') 
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False) 
    rbtn_2.setChecked(False) 
    rbtn_3.setChecked(False) 
    rbtn_4.setChecked(False) 
    RadioGroup.setExclusive(True) 
 
def next_question():
    window.total += 1
    window.cur_question = randint(0, len(question_list) - 1)
    if len(question_list) <= window.cur_question:
        window.cur_question = randint(0, len(question_list) - 1)
    q = question_list[window.cur_question]
    ask(q)
def click_OK():
    if Ben.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def start_test(): 
    if Ben.text == 'WHO': 
        show_result() 
    else: 
        show_question() 
 
answer = [rbtn_1,rbtn_2,rbtn_3,rbtn_4] 
 
def ask(q: Question): 
    shuffle(answer) 
    answer[0].setText(q.right_answer) 
    answer[1].setText(q.wrong1) 
    answer[2].setText(q.wrong2) 
    answer[3].setText(q.wrong3) 
    lbl_Question.setText(q.question) 
    lbl_correct.setText(q.right_answer) 
    show_question()
 
def show_correct(res):
    lbl_result.setText(res) 
    show_result() 
 
def check_answer(): 
    if answer[0].isChecked(): 
        show_correct('Oui') 
        window.score +=1
    else: 
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked(): 
            show_correct('Non') 
Ben.clicked.connect(click_OK) 
next_question()
window.show() 
app.exec()
procent = window.score/ window.total * 100
print('Всего вопросов: ', window.total)
print('Правильных ответов: ', window.score)

print('Рейтинг: ',procent, '%')
window2 = QWidget()