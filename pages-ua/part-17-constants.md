## Частина 17 - Константи

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Дотепер ми створили, відлагодили та змінили простий рядок ехо в стандартній консолі. call ми розширимо цей приклад шляхом додавання константи.

Константа в C++ — це значення, яке не змінюватиметься протягом виконання програми (якщо не змінено). <pre spellcheck="false">#include &lt;iostream&gt;
&nbsp;
int main(void) {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; cons tint YEAR = 2017;
&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; YEAR &lt;&lt; std::endl;
&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;
}
</pre> використовується так, щоб ви мали оголошення раніше в коді, щоб якщо майбутня архітектура програми коли-небудь зміниться, ви могли переозначити константу в одному місці, а не змінювати код у всьому кодовому базі.

Це стандартна практика кодування наших констант у великих літерах, щоб коли ви побачите її посилання в коді, ви знали, що значення є константою.

Ми починаємо з нашого другого програми в C++, яка називається програмою «Константа». <div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520149852856.jpg"/></div> давайте підійдемо до кожного рядка крок за кроком і побачимо, як ця мова працює. <pre spellcheck="false">g++ example2.cpp -o example2
</pre> ми збережемо цей __example2.cpp__ і збережемо його на нашому пристрої.

Для компіляції цього ми просто натискаємо:

<pre spellcheck="false">./example2
</pre>

Ми просто потім натискаємо:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520148263310.jpg"/></div>

УСПІШНО! https://github.com/mytechnotalent/Reverse-Engineering-Tutorial ми бачимо «__2017__» виведене на стандартний вивід або консоль!

Давайте розберемо це:

Ми використовуємо ключове слово __const __, щоб вказати константу, якій ми присвоюємо ціле значення 2017.

Ми потім використовуємо функцію __cout __, щоб вивести його на стандартний вивід або консоль, і додаємо нову лінію з допомогою функції __endl__.

Так! <div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520149852856.jpg"/></div> дуже просто.

Наступна неділя ми підійдемо до Відлагодження Констант.