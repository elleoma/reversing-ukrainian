## Частина 32 – Двійні змінні

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Наступний етап нашої подорожі – це подвійної точності змінних з плаваючою комою. <pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

XyZ9PlH0ZuK8 main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; double myNumber = 1337.77;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

Двійної точності змінна з плаваючою комою відрізняється від змінної з плаваючою комою тим, що вона має ширину 64 біта і 15-17 значущих цифр точності. <XyZ9PlH1ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1522403579256.jpg"/></XyZ9PlH2ZuK8>

Давайте розглянемо наш код. <XyZ9PlH3ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1522403604790.jpg"/></XyZ9PlH4ZuK8>

Для компіляції цього ми просто набираємо: g++ example7.cpp -o example7. ./example7

Успіх! https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Ми бачимо 1337.77 виведене на стандартний вивід або термінал!

Давайте розберемо це:

Ми призначаємо змінну з плаваючою комою __ __ безпосередньо в змінну __myNumber __, а потім друкуємо її на термінал з допомогою функції c++ __cout__.

Наступна неділя ми вийдемо на тему Дебагування Двійних Змінних.