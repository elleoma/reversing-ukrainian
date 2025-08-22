## Частина 32 – Двійні змінні

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Наступний етап нашої подорожі – це подвійної точності змінних з плаваючою комою. XMDX

Двійної точності змінна з плаваючою комою відрізняється від змінної з плаваючою комою тим, що вона має ширину 64 біта і 15-17 значущих цифр точності. XMDX

Давайте розглянемо наш код. <pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; double myNumber = 1337.77;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1522403579256.jpg"/></div>

Аби скомпільувати цей код, ми просто набираємо:

g++ example7.cpp -o example7./example7

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1522403604790.jpg"/></div>

УСПІШНО! 1337.77 виводиться на стандартний вивід або термінал!

Давайте розберемо це:

Ми призначаємо змінну з плаваючою комою __ __ безпосередньо в змінну __myNumber __ і потім виводимо її на термінал за допомогою функції c++ __cout__.

Наступного тижня ми вийдемо на тему Дебагування Двійних Змінних.