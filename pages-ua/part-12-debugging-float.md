## part 12 - налагодження поплавця

Давайте розглянемо наш приклад.&nbsp;__0x05 \ _float.c__&nbsp;as.

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

Давайте розберемося в нашому налагоджувач.

<pre spellcheck="false">radare2 -w arm -b 16 0x05_float.elf
</pre>

Давайте автоматично проаналізуємо.

<pre spellcheck="false">aaaa
</pre>

Давайте прагнемо main.

<pre spellcheck="false">s main
</pre>

Перейдемо у візуальний режим, typingnbsp__v__&nbsp;and thennbsp__p__&nbsp;twice, щоб дістатися до хорошого налагоджувач виду.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1618059343816.jpg"/></div>

Ми бачимо специфікатор формату в _ \ [0x0000033c \] ._

<pre spellcheck="false">:&gt; psz @ [0x0000033c]
%f
</pre>

Поплавок знаходиться на _ \ [0x00000340 \] _.

<pre spellcheck="false">:&gt; pff @ [0x00000340]
0x00004000 = 9.32830524e-09
</pre>

Зробіть not, що поплавок є неточним, оскільки ця машина x64. Важливо побачити значення _0x00004000_. Потім ви запитуєте себе, ей, це not _40.5_! Яка угода?

Гаразд ...

Pico робить not, має власний математичний копроцесор, тому він обробляє поплавці and парні за допомогою програмного забезпечення. Тому _0x00004000_ буде представленням _40.5_ десяткового.

Отже, якщо значення було _40.4_, наприклад, це було б _0x00003333_. Навпаки _40.6_ буде _0x00004ccc_.

Погляньте на наступну таблицю, яка допоможе проілюструвати суть.

<pre spellcheck="false">0x3ff00000 = 1.000000
0x3ff00001 = 1.000001
0x3ff00002 = 1.000002
...
0x3ff0000f = 1.000015
0x3ff00010 = 1.000016
0x3ff00011 = 1.000017
etc...
</pre>

Зрештою, значення цих 4 байт (32-біт) визначатимуть значення поплавця.

На нашому наступному уроці ми будемо hack float and продемонструвати цю логіку.