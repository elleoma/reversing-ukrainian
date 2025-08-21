## part 13 - хакерський поплавок

Давайте розглянемо наш приклад.&nbsp;____0x05 \ _float.c__&nbsp;as.

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

Давайте розберемося в нашому налагоджувачі.

<pre spellcheck="false">radare2 -w arm -b 16 0x05_float.elf
</pre>

Давайте автоматично проаналізуємо.

<pre spellcheck="false">aaaa
</pre>

Давайте прагнемо до головного.

<pre spellcheck="false">s main
</pre>

Давайте перейдемо у візуальний режим, typing&nbsp;__v__&nbsp; і then&nbsp;__p__&nbsp;twice, щоб дістатися до хорошого виду налагоджувача.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1618389543453.jpg"/></div>

Float - at&nbsp; _ \ [0x00000340 \] _.

<pre spellcheck="false">:&gt; pff @ [0x00000340]
0x00004000 = 9.32830524e-09
</pre>

Як ми обговорювали на останньому уроці, не хвилюйтеся, що поплавок є неточним, оскільки ця машина x64. Що важливо побачити, що це value&nbsp;_0x00004000_.

На нашому останньому уроці ми також пояснили те, як Піко обробляє плавання. Давайте розглянемо деякі основи.

<pre spellcheck="false">0x3ff00000 = 1.000000
0x3ff00001 = 1.000001
0x3ff00002 = 1.000002
...
0x3ff0000f = 1.000015
0x3ff00010 = 1.000016
0x3ff00011 = 1.000017
etc...
</pre>

Давайте зламаємо до 1.000000 наступним чином.

Наш мікроконтролер - це маленька ендіанська архітектура, тому, якщо ми збираємось змінити наше 40,5 до 1,0, нам потрібно поставити це значення у зворотному порядку байтів ...

<pre spellcheck="false">0x3ff00000
</pre>

Потрібно бути ...

<pre spellcheck="false">0x0000f03f
</pre>

Тому нам потрібно змінити значення на наступному.

<pre spellcheck="false">wx 0x0000f03f @ 0x00000340
</pre>

Все, що ми маємо зробити зараз, - це вихід і перетворити Un&nbsp; __. elf&nbsp;__to&nbsp; __. Uf2__!

<pre spellcheck="false">./elf2uf2/elf2uf2 0x05_float.elf 0x05_float.uf2
</pre>

Підключіть PICO і переконайтеся, що ви тримаєте завантаження або використовуєте налаштування, яку я надав у частині 2.

<pre spellcheck="false">cp 0x05_float.uf2 /Volumes/RPI-RP2
</pre>

Давайте екранимо це!

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

Ага так!

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

Тут ми зламали значення до 1.000000, і ми дозволили 1 секунду спати.

На нашому наступному уроці ми обговоримо подвійний тип даних.