## part 40-Hacking попередній оператор

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте знову переглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumber
= 16;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int
myNewNumber = ++myNumber;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout
&lt;&lt; myNewNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527247718232.jpg"/></div>

Щоб скласти це, ми просто вводимо:

g ++ example9.cpp -o example9

./example9

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527247743089.jpg"/></div>

  

Ми бачимо 17 надрукованих на екран.

Давайте розберемо його:

Ми створюємо змінну __mynumber = 16__, до якої ми створюємо іншу змінну __mynewnumber__, що попередньо запроваджує значення __mynumber __. &nbsp;we це бачимо, коли ми виконуємо наш код, він показує 17.

Коли ми заздалегідь запроваджуємо, значення змінної збільшується перед тим, як призначити її іншій змінній.&nbsp; для прикладу __mynumber__ є __16__, тому він збільшується перед тим, як бути призначеним до __mynewnumbum__, тому ми отримуємо __17__.

Давайте налагоджуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527247841094.jpg"/></div>

Ми проводимо звичайний старт у gdb and Break на main.&nbsp;take note at __main+24__ Ми переміщуємо значення __1__ в __r3 __. На що ми встановимо breakpoint and Продовження.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527247877140.jpg"/></div>

Коли ми оцінюємо значення в __R3__ на цьому етапі, ми бачимо __17 __. &nbsp;REMEMBER ще в нашому первісному коді, що значення в __MYNUMBER__ Змінна була __16 __. &nbsp;WE бачить, що оператор попереднього інтенсивного значення був успішним для збільшення значення ____1__, щоб дати нам __17__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527247908955.jpg"/></div>

Ми бачимо, що коли ми продовжуємо код, значення __17__ успішно перегукується до терміналу, як очікувалося.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527247930003.jpg"/></div>

Давайте повторно запускаємо програму.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527248017494.jpg"/></div>

Давайте hack! &nbsp; ТЕРОГО Оглянули значення в R3, яке, як ми знаємо, є 17.&nbsp;let's hack до чогось іншого.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527248050749.jpg"/></div>

Успіх! &nbsp;as ми можемо побачити, коли ми продовжуємо, тепер ми бачимо, що зламане значення перегукується до терміналу.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527248118408.jpg"/></div>

На наступному тижні ми зануримось у оператор після інвентації.