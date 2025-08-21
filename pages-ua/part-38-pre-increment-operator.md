## PART 38-Оператор попереднього інкрементації

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Наступний етап нашої подорожі-це оператор попереднього інкрементації.&nbsp;

Давайте розглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumber = 16;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNewNumber = ++myNumber;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1526036616866.jpg"/></div>

Щоб скласти це, ми просто вводимо:

g ++ example9.cpp -o example9

./example9

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1526036640627.jpg"/></div>

Ми бачимо 17 надрукованих на екран.

Давайте розберемо його:

Ми створюємо змінну __mynumber = 16__, до якої ми створюємо іншу змінну __mynewnumber__, що попередньо запроваджує значення __mynumber __. &nbsp;we це бачимо, коли виконуємо наш код, він показує 17.

Коли ми заздалегідь запроваджуємо, значення змінної збільшується перед тим, як призначити її іншій змінній.&nbsp; для прикладу __mynumber__ є __16__, тому він збільшується перед тим, як бути призначеним до __mynewnumbum__, тому ми отримуємо __17__.

Наступного тижня ми занурюємось у налагодження оператора попереднього інтекції.