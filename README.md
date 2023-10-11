### Общее описания решения
1. Выполнила команду **git clone**
- *команда git clone копирует репозиторий по ссылке* 
2. Создала новую ветку new_features<мой код ИСУ> 
- *команда git branch создаёт новую ветку*
- *команда git checkout переключает на ветку*
3. Добавила новый файл в эту ветку
4. Изменила содержимое файла в Python
5. Сделала git add для этого файла 
- *команда git add добавляет файл в репозиторий*
6. Сделала коммита с сообщением о том, что был добавлен новый файл 
- *команда git commit – m сохраняет сделанные ранее изменения и добавляет комментарий*
7. Добавила ещё один один файл в эту ветку
8. Сделала git add для нового файла 
- *команда git add добавляет файл в репозиторий*
9. Исправила ошибку в вычислении периметра в файле rectangle.py
10. Создала ещё один коммит внутри этой же ветки с сообщением о том, что была исправлена ощибка
- *команда git commit -m сохраняет сделанные ранее изменения и добавляет комментарий*
11. Построила граф истории всего репозитория с однострочным выводом коммитов
- *команда git log –graph –oneline –all выводит все комментарии*
12. Построила граф истории только текущей ветки
- *команда git log –graph –oneline выводит комментарии только текущей ветки*
13. Взяла хэши двух последних коммитов из истории и посмотрела, какие изменения были внесены
- *команда git show показывает сохранённые конкретным коммитом изменения*
14. Выполнила merge в ветку main
- *команда git checkout main переключает на ветку main*
15. Сделала Pull Reqest и обсудила с рецензентом в процессе Code Review
- *команда git remote set-url origin задает url указанного по ссылке репозитория*
- *команда git remote -v показывает наполнение удаленного репозитория*
- *команда git push -u origin связывает текущую ветку с указанной веткой удаленного 
репозитория*
16. Удалила созданную ветку
- *команда git branch -d удаляет заданную ветку*
17. Добавила описание решения для фалов circle.py, rectangle.py, square.py, triangle.py в Python
18. Сделала git add для файлов circle.py, rectangle.py, square.py, triangle.py
- *команда git add добавляет файл в репозиторий*
19. Сделала git commit 
- *команда git commit – m сохраняет сделанные ранее изменения и добавляет комментарий*
20. Сделала git add README.md
- *команда git add добавляет файл в репозиторий*

### <font color="green"> Описание функций для файла circle.py:

def area(r):  
&nbsp;&nbsp;&nbsp;&nbsp;return math.pi * r * r

- <font color="grey">
Принимает число r - радиус
- Возвращает площадь круга с радиусом r  
<font color="orange">*Примеры вызова:*  
input: 5  
output: ~78,53982

<font color="green">def perimeter(r):  
&nbsp;&nbsp;&nbsp;&nbsp;return 2 * math.pi * r

- <font color="grey">Принимает число r - радиус
- Возвращает длину окружности с радиусом r  
<font color="orange">*Примеры вызова:*  
input: 3  
output: ~18,84956

### <font color="green"> Описание функций для файла rectangle.py:

def area(a, b):  
&nbsp;&nbsp;&nbsp;&nbsp;return a * b

- <font color="grey">Принимает 2 числа a и b
- Возвращает площадь прямоугольника со сторонами длины a и b   
<font color="orange">*Примеры вызова:*  
input: 2 7  
output: 14

<font color="green">def perimeter(a, b):  
&nbsp;&nbsp;&nbsp;&nbsp;return 2 * a + 2 * b

- <font color="grey">Принимает 2 числа a и b
- Возвращает периметр прямоугольника со сторонами длины a и b  
<font color="orange">*Примеры вызова:*  
input: 4 7  
output: 22

### <font color="green"> Описание функций для файла square.py:

def area(a):  
&nbsp;&nbsp;&nbsp;&nbsp;return a * a

- <font color="grey">Принимает число a
- Возвращает площадь квадрата со стороной длины a   
<font color="orange">*Примеры вызова:*  
input: 3  
output: 9

<font color="green">def perimeter(a, b):  
&nbsp;&nbsp;&nbsp;&nbsp;return 4 * a

- <font color="grey">Принимает число a
- Возвращает периметр квадрата со стороной длины a  
<font color="orange">*Примеры вызова:*  
input: 4  
output: 16

### <font color="green"> Описание функций для файла triangle.py:

def area(a, h):  
&nbsp;&nbsp;&nbsp;&nbsp;return a * h / 2

- <font color="grey">Принимает 2 числа a и h
- Возвращает площадь треугольника со стороной длины a и высотой длины h, проведённой к стороне длины a   
<font color="orange">*Примеры вызова:*  
input: 5 8  
output: 20

<font color="green">def perimeter(a, b, c):  
&nbsp;&nbsp;&nbsp;&nbsp;return a + b + c

- <font color="grey">Принимает 3 числа a, b, c
- Возвращает периметр треугольника со сторонами длины a, b, c  
<font color="orange">*Примеры вызова:*  
input: 5 3 4  
output: 12

### <font color="green"> История изменения проектов с хэшами коммитов
<font color="white">commit f87de56eb12f053a8da335ef4f2f273c85210635 (origin/main, origin/HEAD, main)  
Author: Anastasia0 <anstasia_don@list.ru>  
Date:   Thu Sep 21 21:35:31 2023 +0300  
*'''Была исправлена ошибка'''*  

<font color="white">commit 6ad9dbfcff420da6f19dface2b1a43bbd3491a3d  
Author: Anastasia0 <anstasia_don@list.ru>  
Date:   Thu Sep 21 21:32:24 2023 +0300  
*'''Добавлен новый файл'''*

<font color="white">commit d078c8d9ee6155f3cb0e577d28d337b791de28e2  
Author: smartiqa <info@smartiqa.ru>  
Date:   Thu Mar 4 14:55:29 2021 +0300  
*'''L-03: Docs added'''*

<font color="white">commit 8ba9aeb3cea847b63a91ac378a2a6db758682460  
Author: smartiqa <info@smartiqa.ru>  
Date:   Thu Mar 4 14:54:08 2021 +0300  
*'''L-03: Circle and square added'''*
