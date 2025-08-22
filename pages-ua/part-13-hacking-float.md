## Частина 13 - Хакінг флоата

Давайте переглянем наш приклад.&nbsp;__0x05\_float.c__&nbsp;as слідує.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; float x = 40.5;

&nbsp; &nbsp; printf("%f\n", x);&nbsp;

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }

&nbsp; return 0;
}
</pre>

Давайте запустимо наш дебагер.

<pre spellcheck="false">radare2 -w arm -b 16 0x05_float.elf
</pre>

Давайте зробимо аналіз автоматично.

<pre spellcheck="false">aaaa
</pre>

Давайте перейдемо до головної частини програми.

<pre spellcheck="false">s main
</pre>

Давайте перейдемо в візуальний режим, натиснувши&nbsp;__V__&nbsp;і потім&nbsp;__p__&nbsp;два рази, щоб потрапити до хорошого дебагерського перегляду.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1618389543453.jpg"/></div>

Флоат знаходиться на&nbsp;_\[0x00000340\]_.

<pre spellcheck="false">:&gt; pff @ [0x00000340] 0x00004000 = 9.32830524e-09
</pre>

Як ми обговорили в останньому урокі, не хвилюйтеся, що флоат не дуже точний, оскільки ця машина x64. Що важливо побачити, це значення&nbsp;_0x00004000_.

У нашому останньому урокі ми також пояснили, як працює Pico щодо флоатів. Давайте переглянемо деякі основи.

<pre spellcheck="false">0x3ff00000 = 1.000000 0x3ff00001 = 1.000001 0x3ff00002 = 1.000002... 0x3ff0000f = 1.000015 0x3ff00010 = 1.000016 0x3ff00011 = 1.000017
etc...
</pre>

Давайте змінимо на 1.000000 наступним чином.

Наш мікроконтролер має малендійну архітектуру, тому якщо ми хочемо змінити наш 40.5 на 1.0, нам потрібно помістити цю вартість у зворотньому порядку байтів, тому...

<pre spellcheck="false">0x3ff00000
</pre>

Нам потрібно...

<pre spellcheck="false">0x0000f03f
</pre>

Отже, нам потрібно змінити значення на наступному місці.

<pre spellcheck="false">wx 0x0000f03f @ 0x00000340
</pre>

Усі, що залишилося зробити зараз, це вийти і перетворити нашу&nbsp;__.elf&nbsp;__на&nbsp;__.uf2__!

<pre spellcheck="false">./elf2uf2/elf2uf2 0x05_float.elf 0x05_float.uf2
</pre>

Під'єднайте Pico і переконайтеся, що натисніть кнопку BOOTSEL або використовуйте налаштування, які я надав у частині 2.

<pre spellcheck="false">cp 0x05_float.uf2 /Volumes/RPI-RP2
</pre>

Давайте побачимо!

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

АХА!

<pre spellcheck="false">1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
</pre>

Тут ми змінили значення на 1.000000 і дали 1 секунду, щоб воно збереглося.

У наступному урокі ми обговоримо тип даних double.