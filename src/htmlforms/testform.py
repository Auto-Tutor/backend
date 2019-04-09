import json


class TestForm():
    def get_text_v1(self) -> json:
        return """
 <!DOCTYPE HTML>
 <html>
 <head>
 	<meta charset="utf-8">
 	<title>Тег FORM</title>
 </head>
 <body>

 	<form >
 		<p><b>Однажды в поликлинику пришел больной.
 			– Что у вас болит? – спросил врач.
 			– У меня болит живот, – ответил молодой человек.
 			– Что вы ели вчера?
 			– Зеленые яблоки.
 			– Хорошо. Я дам вам лекарство для глаз, – сказал врач больному.
 			– Почему для глаз? Ведь у меня болит живот? – удивился молодой человек.
 		– Я дам вам лекарство для глаз, чтобы вы лучше видели, что вы едите, – сказал врач.</b></p>

 		<p><b>Почему пациент пришел к врачу?</b></p>
 		<p><input type="radio" name="answer1" value="a1">у него болели глаза;<Br>
 			<input type="radio" name="answer1" value="a2">у него проблемы с животом;<Br>
 			<input type="radio" name="answer1" value="a3">у него проблемы с аппетитом - он ест только зеленые яблоки
 		</p>


 		<p><b>Почему пациент плохо себя чувствует?</b></p>
 		<p><input type="radio" name="answer2" value="a1">ему нужно лекарство;<Br>
 			<input type="radio" name="answer2" value="a2">это - плановый визит;<Br>
 			<input type="radio" name="answer2" value="a3">вчера он ел зеленые яблоки.
 		</p>


 		<p><b>Почему доктор выписал пациенту лекарство для глаз?</b></p>
 		<p><input type="radio" name="answer3" value="a1">у пациента болели глаза;<Br>
 			<input type="radio" name="answer3" value="a2">чтобы он не ел зеленые яблоки;<Br>
 			<input type="radio" name="answer3" value="a3"> лекарство для глаз может лечить и больной живот.</p>
 			<p>
 				<input type="submit"></p>
 			</form>

 		</body>
 		</html>s
        """
