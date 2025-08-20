## part 16 - Hacking подвійний

Давайте переглянемо,

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; double x = 40.55555555555555555555;

&nbsp; &nbsp; printf("%.16f\n", x)&nbsp;

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }

&nbsp; return 0;
}
</pre>

Давайте розберемося в нашому налагоджувач.

<pre spellcheck="false">radare2 -w arm -b 16 0x06_double.elf
</pre>

Давайте автоматично проаналізуємо.

<pre spellcheck="false">aaaa
</pre>

Давайте прагнемо main.

<pre spellcheck="false">s main
</pre>

Перейдемо у візуальний режим, typingnbsp__v__&nbsp;and thenxyz9plh5cuk8__p__&nbsp;twice, щоб дістатися до хорошого налагоджувач виду.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1620377345934.jpg"/></div>

Наш мікроконтролер - це маленька ендіанська архітектура, як ми говорили раніше, тому, якщо ми збираємось змінити наше 40.5555555560000000 на 1,0, нам потрібно поставити це значення у зворотному порядку байтів, тому ...

<pre spellcheck="false">0x3ff00000
</pre>

Потрібно бути ...

<pre spellcheck="false">0x0000f03f
</pre>

Тому нам потрібно змінити значення на наступному.

<pre spellcheck="false">wx 0x0000f03f @ 0x00000344
</pre>

Все, що нам потрібно зробити зараз, це exit and перетворити ur&nbsp; __. elf&nbsp;__to&nbsp; __. Uf2__!

<pre spellcheck="false">./elf2uf2/elf2uf2 0x06_double.elf 0x06_double.uf2
</pre>

Підключіть Pico and, переконайтеся, що ви тримаєте завантаження or, використовуйте налаштування, яку я надав у частині 2.

nbsp

Давайте екранимо це!

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

Ага так!

<pre spellcheck="false">1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
1.0000002380000000
</pre>

Тепер ми повинні добре розуміти типи даних всередині С, щоб переглянути деякі трохи більші поняття.

На нашому наступному уроці ми почнемо обговорювати вклад.