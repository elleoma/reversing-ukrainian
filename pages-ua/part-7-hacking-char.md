## part 7 - хакерський шар

Сьогодні ми зламаємо просту програму CHAR.

Давайте розглянемо наш код.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; char x = 'x';
&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;
&nbsp; &nbsp; printf("%c\n", x);

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }
&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;
&nbsp; return 0;
}
</pre>

Давайте розберемо наш налагоджувач.

<pre spellcheck="false">radare2 -w arm -b 16 0x03_char.elf
</pre>

Давайте автоматично проаналізуємо.

<pre spellcheck="false">aaaa
</pre>

Давайте прагнемо до головного.

<pre spellcheck="false">s main
</pre>

Перейдемо у візуальний режим, typing&nbsp;__v__&nbsp; і then&nbsp;__p__&nbsp;twice, щоб дістатися до хорошого виду налагоджувача.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1616750858178.jpg"/></div>

На нашому останньому уроці ми зламали кожен рядок. Тут ми, очевидно, зацікавлені у зламанні цінності 0x78 і змінити це на все, що ми хочемо. Спробуємо 0x79. Цей простий хак перетворить char _'x'_ в _'y'_.

<pre spellcheck="false">:&gt; wa movs r1, 0x79 @ 0x00000328
Written 2 byte(s) (movs r1, 0x79) = wx 7921
</pre>

Давайте перевіримо зміни.

<pre spellcheck="false">:&gt; pd 1 @ 0x00000328
│ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ; CODE XREF from main @ 0x338
│ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 0x00000328&nbsp; &nbsp; &nbsp; 7921 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; movs r1, 0x79 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ; 'y' ; arg1
</pre>

У цьому випадку наш налагоджувач навіть говорить нам, що це насправді _'y'_, крім того, зараз ми переміщуємо значення шестигранного ASCII у 0x79 в _R1_.

Давайте також зламаємо час сну до 2000 мс або 2 секунди.

<pre spellcheck="false">:&gt; wa lsls r0, r0, 3 @ 0x00000332
Written 2 byte(s) (lsls r0, r0, 3) = wx c000
</pre>

Тут ми просто логічний зсув ліворуч 3 рази, тому 250 x 2 = 500, 500 x 2 = 1000, 1000 x 2 = 2000.

Давайте перевіримо.

<pre spellcheck="false">:&gt; pd 1 @ 0x00000332
│ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 0x00000332&nbsp; &nbsp; &nbsp; c000 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; lsls r0, r0, 3
</pre>

Все, що нам потрібно зробити зараз, - це вийти та перетворити Ur&nbsp; __. elf&nbsp;__to&nbsp; __. Uf2__!

<pre spellcheck="false">./elf2uf2/elf2uf2 0x03_char.elf 0x03_char.uf2
</pre>

Підключіть PICO і переконайтеся, що ви тримаєте завантаження або використовуєте налаштування, яку я надав у частині 2.

<pre spellcheck="false">cp 0x03_char.uf2 /Volumes/RPI-RP2
</pre>

Давайте екранимо це!

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

Ага так!

<pre spellcheck="false">y
y
y
y
y
y
</pre>

Ми бачимо, як "Y" надруковано кожні 2 секунди!

На нашому наступному уроці ми обговоримо тип даних int.