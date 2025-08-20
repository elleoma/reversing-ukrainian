## PART 39-Налагодження оператора попереднього інкрементації

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте переглянемо наш код.

nbsp

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1526639245794.jpg"/></div>

Щоб скласти це, ми просто вводимо:

g ++ example9.cpp -o example9

./example9

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1526639272084.jpg"/></div>

Ми бачимо 17 надрукованих на екран.

Давайте розберемо його:

Ми створюємо змінну __mynumber = 16__, до якої ми створюємо іншу змінну __mynewnumber__, що попередньо запроваджує значення __mynumber __. &nbsp;we це бачимо, коли ми виконуємо наш код, він показує 17.

Коли ми заздалегідь запроваджуємо, значення змінної збільшується перед тим, як призначити її іншій змінній.&nbsp; для прикладу __mynumber__ є __16__, тому він збільшується перед тим, як бути призначеним до __mynewnumbum__, тому ми отримуємо __17__.

Давайте налагоджуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1526639315124.jpg"/></div>

Ми проводимо звичайний старт у gdb and Break на main.nbsptake примітка в __main+24__ Ми переміщуємо значення __1__ в __r3 __. На що ми встановимо breakpoint and Продовження.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1526639338414.jpg"/></div>

Коли ми оцінюємо цінність у __R3__ на цьому етапі, ми бачимо __17 __. &nbsp;REMEMBER ще в нашому первісному коді, що значення в __Mynumber__ змінна була __16 __. nbspWE може побачити, що оператор попереднього інтенсивності був успішним для збільшення значення ____1__, щоб дати нам __17__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1526639366619.jpg"/></div>

Ми бачимо, що коли ми продовжуємо код, значення __17__ успішно перегукується до терміналу, як очікувалося.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1526639388837.jpg"/></div>

На наступному тижні ми зануримось у Hacking Налагодження попереднього інтекментаційного оператора.