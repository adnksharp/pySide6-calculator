import sys, re
from random import *
from math import * 
from sympy import parse_expr, solve, symbols

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, QEvent, QTimer
from PySide6.QtGui import Qt

from ui_form import Ui_Widget

class maths():
    def fix(form):
        form = form.replace('^', '**')
        form = form.replace('sen', 'sin')
        
        
        form = re.sub(r"sqrt\((.+?),(\d)\)", r"(\1)**(1/\2)", form)
        form = re.sub(r'(\d)(x)', r'\1*\2', form)
        form = re.sub(r'(\d)(pi)', r'\1*\2', form)
        form = re.sub(r'(\d)(e)', r'\1*\2', form)
        form = re.sub(r'(\d)(rand)', r'\1*\2', form)
        
        form = re.sub(r'(x)(\d)', r'\1*\2', form)
        form = re.sub(r'(pi)(\d)', r'\1*\2', form)
        form = re.sub(r'(e)(\d)', r'\1*\2', form)
        form = re.sub(r'(rand)(\d)', r'\1*\2', form)
        
        if widget.mode[0] == 0:
            form = re.sub(r'cos(.+?)', r'cos(\1', form)
            form = re.sub(r'sin(.+?)', r'sin(\1', form)
            form = re.sub(r'tan(.+?)', r'tan(\1', form)
        
            form = re.sub(r'acos(.+?)', r'acos(\1', form)
            form = re.sub(r'asin(.+?)', r'asin(\1', form)
            form = re.sub(r'atan(.+?)', r'atan(\1', form)
            
        else:
            form = re.sub(r'cos(.+?)', r'cos(radians(\1', form)
            form = re.sub(r'sin(.+?)', r'sin(radians(\1', form)
            form = re.sub(r'tan(.+?)', r'tan(radians(\1', form)
        
            form = re.sub(r'acos(.+?)', r'acos(radians(\1', form)
            form = re.sub(r'asin(.+?)', r'asin(radians(\1', form)
            form = re.sub(r'atan(.+?)', r'atan(radians(\1', form)
        
        form = re.sub(r'(\d)(cos)', r'\1*\2', form)
        form = re.sub(r'(\d)(sin)', r'\1*\2', form)
        form = re.sub(r'(\d)(tan)', r'\1*\2', form)
        
        form = re.sub(r'(\d)(acos)', r'\1*\2', form)
        form = re.sub(r'(\d)(asin)', r'\1*\2', form)
        form = re.sub(r'(\d)(atan)', r'\1*\2', form)
        
        if form.count('(') > form.count(')'):
            for _ in range(form.count('(') - form.count(')')):
                form += ')'
        elif form.count('(') < form.count(')'):
            for _ in range(form.count(')') - form.count('(')):
                form = '(' + form
        
        if 'rand(' in form:
            form = re.sub(r'rand\((.+?),(.+?)\)', r'randrange(\1, \2)', form)
        else:
            form = form.replace('rand', 'random()')
            
        return form
    
    def translate(val):
        if val == 0:
            return ''
        elif val == 3:
            return 'k'
        elif val == 6:
            return 'G'
        elif val == 9:
            return 'M'
        elif val == 12:
            return 'T'
        elif val == 15:
            return 'P'
        elif val == 18:
            return 'E'
        elif val == -3:
            return 'm'
        elif val == -6:
            return 'µ'
        elif val == -9:
            return 'n'
        elif val == -12:
            return 'p'
        elif val == -15:
            return 'f'
        return 'E{:+}'.format(val)
    
    def standard(form):
        return eval(form)
    
    def symbolic(form):
        return solve(parse_expr(form), symbols('x'))

class KeyPress(QObject):
    def eventFilter(self, widget, event):
        if event.type() == QEvent.KeyRelease:
            if event.text():
                if event.text() == '\b':
                    widget.form = widget.form[:-1]
                elif event.text() == '\u007F':
                    widget.cur = widget.cur[1:]
                else:
                    widget.form += event.text()
            else:
                try:
                    if event.key() == Qt.Key_Right:
                        widget.form += widget.cur[0]
                        widget.cur = widget.cur[1:]
                    elif event.key() == Qt.Key_Left:
                        widget.cur = widget.form[len(widget.form) - 1] + widget.cur
                        widget.form = widget.form[:-1]
                except:
                    pass
            widget.solve()
        return False

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.form = ''
        self.cur = ''
        self.out = ''
        self.srtcur = ' '
        self.strout = '-'
        self.mode = [0, 0]
        
        self.eventFilter = KeyPress(parent=self)
        self.installEventFilter(self.eventFilter)
        
        self.timer = QTimer()
        self.timer.setInterval(300)
        self.timer.timeout.connect(self.inputBlinks)
        
        self.ui.pushButton.clicked.connect(lambda x: self.ButtonPress('0'))
        self.ui.pushButton_2.clicked.connect(lambda x: self.ButtonPress('.'))
        self.ui.pushButton_3.clicked.connect(lambda x: self.ButtonPress('E'))
        self.ui.pushButton_4.clicked.connect(lambda x: self.ButtonPress('ans'))
        self.ui.pushButton_5.clicked.connect(lambda x: self.ButtonPress('='))
        self.ui.pushButton_6.clicked.connect(lambda x: self.ButtonPress('1'))
        self.ui.pushButton_7.clicked.connect(lambda x: self.ButtonPress('2'))
        self.ui.pushButton_8.clicked.connect(lambda x: self.ButtonPress('3'))
        self.ui.pushButton_9.clicked.connect(lambda x: self.ButtonPress('+'))
        self.ui.pushButton_10.clicked.connect(lambda x: self.ButtonPress('-'))
        self.ui.pushButton_11.clicked.connect(lambda x: self.ButtonPress('4'))
        self.ui.pushButton_12.clicked.connect(lambda x: self.ButtonPress('5'))
        self.ui.pushButton_13.clicked.connect(lambda x: self.ButtonPress('6'))
        self.ui.pushButton_14.clicked.connect(lambda x: self.ButtonPress('*'))
        self.ui.pushButton_15.clicked.connect(lambda x: self.ButtonPress('/'))
        self.ui.pushButton_16.clicked.connect(lambda x: self.ButtonPress('7'))
        self.ui.pushButton_17.clicked.connect(lambda x: self.ButtonPress('8'))
        self.ui.pushButton_18.clicked.connect(lambda x: self.ButtonPress('9'))
        self.ui.pushButton_19.clicked.connect(lambda x: self.ButtonPress('del'))
        self.ui.pushButton_20.clicked.connect(lambda x: self.ButtonPress('clear'))
        self.ui.pushButton_22.clicked.connect(lambda x: self.ButtonPress('sin'))
        self.ui.pushButton_23.clicked.connect(lambda x: self.ButtonPress('cos'))
        self.ui.pushButton_24.clicked.connect(lambda x: self.ButtonPress('tan'))
        self.ui.pushButton_26.clicked.connect(lambda x: self.ButtonPress('left'))
        self.ui.pushButton_27.clicked.connect(lambda x: self.ButtonPress('right'))
        self.ui.pushButton_31.clicked.connect(lambda x: self.ButtonPress('alpha'))
        self.ui.pushButton_34.clicked.connect(lambda x: self.ButtonPress('shift'))
        self.ui.pushButton_35.clicked.connect(lambda x: self.ButtonPress('angles'))
        self.ui.pushButton_37.clicked.connect(lambda x: self.ButtonPress('mode'))
        
        self.timer.start()
        
    def ButtonPress(self, opt):
        if ((opt.isdigit() or re.search(r'[^A-Za-z0-9]', opt)) and opt != '=') or opt == 'E':
            self.form += opt
        elif opt == 'sin' or opt == 'cos' or opt == 'tan':
            self.form += opt + '('
        else:
            match opt:
                case 'ans':
                    self.form += self.out
                case 'del':
                    self.form = self.form[:-1]
                case 'clear':
                    self.form = ''
                case 'left':
                    try:
                        self.cur = self.form[len(self.form) - 1] + self.cur
                        self.form = self.form[:-1]
                    except:
                        pass
                case 'right':
                    try:
                        self.form += self.cur[0]
                        self.cur = self.cur[1:]
                    except:
                        pass
                case 'angles':
                    self.mode[0] = 1 - self.mode[0]
                    self.ui.pushButton_35.setText('DEG' if self.mode[0] == 1 else 'RAD')
                case 'mode':
                    self.mode[1] -= 1
                    if self.mode[1] < 0:
                        self.mode[1] = 2
                    if self.mode[1] == 0:
                        self.ui.pushButton_37.setText('NORM')
                    if self.mode[1] == 2:
                        self.ui.pushButton_37.setText('SCI')
                    if self.mode[1] == 1:
                        self.ui.pushButton_37.setText('ENG')
                        
        self.solve()
        
    def solve(self):
        try:
            self.out = maths.standard(maths.fix(self.form + self.cur))
        except:
            try:
                self.out = maths.symbolic(maths.fix(self.form + self.cur))
            except:
                self.out = '-'
        self.ui.inLabel.setText(str(self.form + '_' + self.cur))

        self.strout = ''
        if type(self.out) == list:
            for i in range(len(self.out)):
                if self.mode[1] == 0:
                    self.strout += 'x' + str(i+1) + ': ' + str(self.out[i])
                elif self.mode[1] == 2:
                    j = eval(str(self.out[i]))
                    self.strout += 'x' + str(i+1) + ': {:E}'.format(j)
                else:
                    try:
                        j = eval(str(self.out[i]))
                        ingexp = int(floor(log10(abs(j))))
                        ingexp -= ingexp % 3
                        ingvar = j / 10 ** ingexp
                        ingexp = maths.translate(ingexp)
                    
                        self.strout += 'x' + str(i+1) + f": {ingvar:.3f}{ingexp}"
                    except:
                        self.strout += ''
                    
                if i < len(self.out) - 1:
                    self.strout += '\n'
        else:
            if self.mode[1] == 0:
                self.strout = str(self.out)
            elif self.mode[1] == 2:
                try:
                    self.strout = '{:E}'.format(self.out)
                except:
                    self.strout = ''
            else:
                try:
                    ingexp = int(floor(log10(abs(self.out))))
                    ingvar = self.out / 10 ** ingexp
                    ingexp -= ingexp % 3
                    ingvar = self.out / 10 ** ingexp
                    ingexp = maths.translate(ingexp)
                    
                    self.strout += f"{ingvar:.3f}{ingexp}"
                    
                except:
                    self.strout = ''
        
    def inputBlinks(self):
        self.srtcur = '_' if self.srtcur == ' ' else ' '
        self.ui.inLabel.setText(str(self.form + self.srtcur + self.cur))
        self.ui.outLabel.setText(self.strout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
