## part 9 - налагодження int

Сьогодні ми збираємось налагодити нашу дуже просту програму int. Давайте розглянемо код.

__0x04 \ _int.c__

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

Давайте розберемося в нашому налагоджувачі.

<pre spellcheck="false">radare2 -w arm -b 16 0x04_int.elf
</pre>

Давайте автоматично проаналізуємо.

<pre spellcheck="false">aaaa
</pre>

Давайте прагнемо до головного.

<pre spellcheck="false">s main
</pre>

Перейдемо у візуальний режим, typing&nbsp;__v__&nbsp; і then&nbsp;__p__&nbsp;twice, щоб дістатися до хорошого виду налагоджувача.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1617350497179.jpg"/></div>

Ми починаємо з налаштування нашого основного значення повернення.

<pre spellcheck="false">push {r4, lr}
</pre>

Ми call стандартний init init.

<pre spellcheck="false">bl sym.stdio_init_all
</pre>

Потім ми завантажуємо наш формат модифікатор %d Ofx9plh41zuk8_r4_.

<pre spellcheck="false">ldr r4, [0x0000033c]
</pre>

Ми можемо це довести.

<pre spellcheck="false">:&gt; psz @ [0x0000033c]
%d
</pre>

Потім ми завантажуємо наш int&nbsp;_'40'_&nbsp;INTO&nbsp;_R1 _, що _0x28_ hex.

<pre spellcheck="false">movs r1, 0x28
</pre>

Ми можемо це довести.

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

Потім ми переміщуємо модифікатор формату Of&nbsp;_r0_.

<pre spellcheck="false">movs r0, r4&nbsp;
</pre>

Потім ми розгалужуємось довго до обгортки printf та call it.

<pre spellcheck="false">bl sym.__wrap_printf

</pre>

Потім ми переміщуємо 250 десяткових або 0xfa Hex Ofx9plh46zuk8_r0_.

<pre spellcheck="false">movs r0, 0xfa
</pre>

Потім ми переміщуємо 250 десятків, що знаємо, коли логічний зсув двічі буде 1000 десяткових або 0xfa HEX OFX9PLH47ZUK8_R0_.

<pre spellcheck="false">lsls r0, r0, 2
</pre>

Тоді ми call функція sleep \ _ms.

<pre spellcheck="false">bl sym.sleep_ms
</pre>

Потім ми продовжуємо весь петлю нескінченно.

<pre spellcheck="false">b 0x328
</pre>

На нашому наступному уроці ми зламаємо цей дуже простий двійковий.