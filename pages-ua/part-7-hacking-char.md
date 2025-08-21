## Частина 7 - Хакінг char

Сьогодні ми хакуємо простий програму char.

Давайте переглянемо наш код.

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

Давайте запустимо наш дебагер.

<pre spellcheck="false">radare2 -w arm -b 16 0x03_char.elf
</pre>

Давайте зробимо аналіз.

<pre spellcheck="false">aaaa
</pre>

Давайте підійдемо до головної частини програми.

<pre spellcheck="false">s main
</pre>

Давайте перейдемо в візуальний режим, натиснувши __V__ і потім __p__ двічі, щоб потрапити в добре видиму дебагерську панель.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1616750858178.jpg"/></div>

У нашому останньому урокі ми розібрали кожну лінію. У цьому випадку ми явно зацікавлені в хакінгу значення 0x78 і зміни цього значення на будь-яке інше. Давайте спробуємо 0x79. Цей простий хак перетворить символ _'x'_ на _'y'_.

<pre spellcheck="false">:&gt; wa movs r1, 0x79 @ 0x00000328
Written 2 byte(s) (movs r1, 0x79) = wx 7921
</pre>

Давайте перевіримо зміну.

<pre spellcheck="false">:&gt; pd 1 @ 0x00000328
│ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ; CODE XREF from main @ 0x338
│ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 0x00000328&nbsp; &nbsp; &nbsp; 7921 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; movs r1, 0x79 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ; 'y' ; arg1
</pre>

У цьому випадку наш дебагер навіть повідомляє нам, що воно насправді _'y'_, а також ми переміщаємо значення hex ascii в 0x79 в _r1_.

Давайте також хакнемо час очікування на 2000 мс або 2 секунди.

<pre spellcheck="false">:&gt; wa lsls r0, r0, 3 @ 0x00000332
Written 2 byte(s) (lsls r0, r0, 3) = wx c000
</pre>

У цьому випадку ми просто логічно зміщуємо вліво 3 рази, тобто 250 х 2 = 500, 500 х 2 = 1000, 1000 х 2 = 2000.

Давайте перевіримо.

<pre spellcheck="false">:&gt; pd 1 @ 0x00000332
│ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 0x00000332&nbsp; &nbsp; &nbsp; c000 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; lsls r0, r0, 3
</pre>

Усі, чого ми тепер повинні зробити, це вийти і перетворити нашу __.elf__ на __.uf2__!

<pre spellcheck="false">./elf2uf2/elf2uf2 0x03_char.elf 0x03_char.uf2
</pre>

Вставте Pico і переконайтеся, що натискаєте BOOTSEL або використовуйте налаштування, які я надав у частині 2.

<pre spellcheck="false">cp 0x03_char.uf2 /Volumes/RPI-RP2
</pre>

Давайте його відобразимо!

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

АХА!

<pre spellcheck="false">y
y
y
y
y
y
</pre>

Ми бачимо 'y' виводиться кожні 2 секунди!

У нашому наступному урокі ми обговоримо тип даних int.