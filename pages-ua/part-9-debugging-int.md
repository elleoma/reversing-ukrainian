Частина 9 - Дебагування int

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

<pre spellcheck="false">radare2 -w XyZ9PlH11ZuK8 -b 16 0x04_int.XyZ9PlH14ZuK8
</pre>

Давайте зробимо аналіз автоматично.

<pre spellcheck="false">aaaa
</pre>

Давайте перейдемо до головної частини програми.

<pre spellcheck="false">s main
</pre>

Давайте перейдемо в візуальний режим, натиснувши __V__ і потім __p__ двічі, щоб потрапити до хорошого дебагерського перегляду.

<XyZ9PlH12ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1617350497179.jpg"/></XyZ9PlH13ZuK8>

Ми починаємо встановлювати значення повернення головної частини програми.

<pre spellcheck="false">push {r4, lr}
</pre>

Ми викликаємо стандартну ініціалізацію I/O.

<pre spellcheck="false">XyZ9PlH15ZuK8 sym.stdio_init_all
</pre>

Далі ми завантажуємо формат модифікатор %d у _r4_.

<pre spellcheck="false">ldr r4, [0x0000033c]
</pre>

Ми можемо перевірити це.

<pre spellcheck="false">:&gt; psz @ [0x0000033c]
%d
</pre>

Далі ми завантажуємо наш int _'40'_ у _r1_, який є _0x28_ у вигляді шістнадцяткового числа.

<pre spellcheck="false">movs r1, 0x28
</pre>

Ми можемо перевірити це.

<pre spellcheck="false">:&gt; ? 0x28
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

Далі ми переміщаємо формат модифікатор у _r0_.

<pre spellcheck="false">movs r0, r4&nbsp;
</pre>

Далі ми здійснюємо стрибок на довгу відстань до обгортки printf і викликаємо її.

<pre spellcheck="false">XyZ9PlH16ZuK8 sym.__wrap_printf

</pre>

Далі ми переміщаємо 250 у вигляді десятичного числа або 0xfa у вигляді шістнадцятного числа у _r0_.

<pre spellcheck="false">movs r0, 0xfa
</pre>

Далі ми переміщаємо 250 у вигляді десятичного числа, яке ми знаємо, що після двох логічних зміщень вліво буде 1,000 у вигляді десятичного числа або 0xfa у вигляді шістнадцятного числа у _r0_.

<pre spellcheck="false">lsls r0, r0, 2
</pre>

Далі ми викликаємо функцію sleep\_ms.

<pre spellcheck="false">XyZ9PlH17ZuK8 sym.sleep_ms
</pre>

Далі ми продовжимо цикл while нескінченно.

<pre spellcheck="false">b 0x328
</pre>

У наступному урокі ми навчимося хакувати цю дуже просту бінарну програму.