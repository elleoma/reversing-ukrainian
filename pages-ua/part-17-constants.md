## Частина 17 - Константи

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть обговорені. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Дотепер ми створили, відлагодили та змінили простий рядок ехо в стандартній консолі. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Нам потрібно розширити цей приклад шляхом додавання константи.

Константа в C++ — це значення, яке не змінюватиметься протягом виконання програми (якщо не змінено). https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Використовується така, що ви маєте оголошення раніше в коді, щоб якщо майбутня архітектура програми коли-небудь зміниться, ви могли змінити константу в одному місці, а не змінювати код у всьому кодовому базі.

Стандартна практика кодування констант у великих літерах, щоб коли ви побачите її посилання в коді, ви знали, що значення є константою.

Нам потрібно розпочати наш другий програму в C++, яка називається програмою «Константа». https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте глибше вивчитимемо кожну лінію крок за кроком і побачимо, як ця мова працює. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Ми збережемо цей приклад в файлі __example2.cpp__ і збережемо його на нашому пристрої.

<pre spellcheck="false">#include &lt;iostream&gt;
&nbsp;
XyZ9PlH1ZuK8 main(void) {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; cons tint YEAR = 2017;
&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; YEAR &lt;&lt; std::endl;
&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;
}
</pre>

<XyZ9PlH2ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520149852856.jpg"/></XyZ9PlH3ZuK8>

Аби скомпільувати цей код, ми просто натиснемо:

<pre spellcheck="false">g++ example2.cpp -o example2
</pre>

Далі ми просто натиснемо:

<pre spellcheck="false">./example2
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520148263310.jpg"/></div>

УСПІШНО! https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Ми бачимо «__2017__» виведене в стандартний вивід або консолі!

Давайте розберемо це:

Ми використовуємо ключове слово __const __, щоб вказати, що це константа, якій ми присвоюємо ціле значення 2017.

Далі ми використовуємо функцію __cout __, щоб вивести його в стандартний вивід або консолі, і додаємо нову лінію з допомогою функції __endl__.

Так! https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Наступна неділя ми глибше вивчитимемо Відлагодження Констант.