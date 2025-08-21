## PART 40-Злом оператора попереднього інкрементації

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

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

Коли ми заздалегідь запроваджуємо, значення змінної збільшується перед тим, як призначити її іншій змінній.&nbsp; для прикладу __mynumber__ є __16__, тому він збільшується, перш ніж бути призначеним до __mynewnumbum__, тому ми отримуємо __17__.

Давайте налагоджуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527247841094.jpg"/></div>

Ми робимо звичайний старт у gdb і розриваємо на main.&nbsp;take Note at __main+24__ Ми переміщуємо значення __1__ в __r3 __. &nbsp;we, а потім бачимо __main+28__ ми продовжуємо це значення __r11-8__, що ми встановимо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527247877140.jpg"/></div>

Коли ми оцінюємо цінність у __R3__ на цьому етапі, ми бачимо __17 __. &nbsp;REMEMBER ще в нашому первісному коді, що значення в __Mynumber__ змінна була __16 __. &nbsp;WE бачить, що оператор попереднього інтенсивності був успішним, щоб збільшити значення ____1__, щоб дати нам __17__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527247908955.jpg"/></div>

Ми бачимо, що коли ми продовжуємо код, значення __17__ успішно перегукується до терміналу, як очікувалося.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527247930003.jpg"/></div>

Давайте повторно запускаємо програму.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527248017494.jpg"/></div>

Давайте хакемо! &nbsp; - це перегляд значення в R3, яке ми знаємо, що він є 17.&nbsp;let, зламає це на щось інше.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527248050749.jpg"/></div>

Успіх! &nbsp;as ми можемо побачити, коли ми продовжуємо, тепер ми бачимо, як зламане значення перегукується до терміналу.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527248118408.jpg"/></div>

На наступному тижні ми зануримось у оператор після інвентації.