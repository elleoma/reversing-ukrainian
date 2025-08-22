## Частина 9 - Дебагування int

Сьогодні ми візьмемося за дебагування нашого дуже простого програми int. Давайте переглянемо код.

__0x04\_int.c__

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; int x = 40;&nbsp;

&nbsp; &nbsp; printf("%d\n", x);&nbsp;

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }

&nbsp; return 0;
}
</pre>

Давайте запустимо наш дебагер.

<pre spellcheck="false">radare2 -w arm -b 16 0x04_int.elf
</pre>

Давайте зробимо автоматичну аналітику.

<pre spellcheck="false">aaaa
</pre>

Давайте перейдемо до головної частини програми.

<pre spellcheck="false">s main
</pre>

Давайте перейдемо в візуальний режим, натиснувши __V__ і потім __p__ двічі, щоб потрапити до хорошого дебагерського перегляду.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1617350497179.jpg"/></div>

Ми починаємо встановлювати значення повернення головної частини програми.

<pre spellcheck="false">push {r4, lr}
</pre>

Ми викликаємо стандартну I/O ініціалізацію.

<pre spellcheck="false">bl sym.stdio_init_all
</pre>

Далі ми завантажуємо форматний модифікатор %d у _r4_.

<pre spellcheck="false">ldr r4, [0x0000033c]
</pre>

Ми можемо перевірити це.

<pre spellcheck="false">:&gt; psz @ [0x0000033c]
%d
</pre>

Далі ми завантажуємо int значення '_40'_ у _r1_, яке є _0x28_ у шістнадцятковій системі числення.

<pre spellcheck="false">movs r1, 0x28
</pre>

Ми можемо перевірити це.

<pre spellcheck="false">:&gt;? 0x28
int32 &nbsp; 40
uint32&nbsp; 40
hex &nbsp; &nbsp; 0x28
octal &nbsp; 050
unit&nbsp; &nbsp; 40
segment 0000:0028
string&nbsp; "("
fvalue: 40.0
float:&nbsp; 0.000000f
double: 0.000000
binary&nbsp; 0b00101000
ternary 0t1111
</pre>

Далі ми переміщаємо форматний модифікатор у _r0_.

<pre spellcheck="false">movs r0, r4&nbsp;
</pre>

Далі ми здійснюємо довгий стрибок до printf обгортки і викликаємо її.

<pre spellcheck="false">bl sym.__wrap_printf

</pre>

Далі ми переміщаємо 250 у десятковій системі числення або 0xfa у шістнадцятковій системі числення у _r0_.

<pre spellcheck="false">movs r0, 0xfa
</pre>

Далі ми переміщаємо 250 у десятковій системі числення, яке ми знаємо, що після двох логічних зміщень вліво буде 1,000 у десятковій системі числення або 0xfa у шістнадцятковій системі числення у _r0_.

<pre spellcheck="false">lsls r0, r0, 2
</pre>

Далі ми викликаємо функцію sleep\_ms.

<pre spellcheck="false">bl sym.sleep_ms
</pre>

Далі ми продовжуємо цикл while до нескінченності.

<pre spellcheck="false">b 0x328
</pre>

У наступному урокі ми навчимося хакувати цей дуже простий байнері.