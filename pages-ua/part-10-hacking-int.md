## Частина 10 - Хакінг int

Сьогодні ми хакуємо наш простий int програму. Давайте переглянемо код.

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

<pre spellcheck="false">radare2 -w arm -b 16 0x04_int.XyZ9PlH10ZuK8
</pre>

Давайте зробимо аналіз автоматично.

<pre spellcheck="false">aaaa
</pre>

Давайте перейдемо до головної частини програми.

<pre spellcheck="false">s main
</pre>

Давайте перейдемо в візуальний режим, натиснувши __V__ і потім __p__ двічі, щоб потрапити до хорошого дебагерського перегляду.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1617616216893.jpg"/></div>

Ми почнемо з хакування int значення, яке ми знаємо, що воно дорівнює _40_ у десятичній системі числення або _28_ у шістнадцятковій системі числення.

<pre spellcheck="false">:&gt; wa movs r1, 0x30 @ 0x00000328
Written 2 byte(s) (movs r1, 0x30) = wx 3021
</pre>

У цьому місці ми бачимо _0x30_, який дорівнює _48_ у десятичній системі числення.

<pre spellcheck="false">:&gt; ? 0x30
int32 &nbsp; 48
uint32&nbsp; 48
hex &nbsp; &nbsp; 0x30
octal &nbsp; 060
unit&nbsp; &nbsp; 48
segment 0000:0030
string&nbsp; "0"
fvalue: 48.0
float:&nbsp; 0.000000f
double: 0.000000
binary&nbsp; 0b00110000
ternary 0t1210
</pre>

Також ми бачимо, що _0xfa_, яке ми знаємо, що воно дорівнює _250_ у десятичній системі числення, є нашою 1/4 мілісекундною затримкою, яка при зміщенні вліво двічі, збільшується і стає _1000_ у десятичній системі числення для затримки на 1 секунду.

<pre spellcheck="false">:&gt; ? 0xfa
int32 &nbsp; 250
uint32&nbsp; 250
hex &nbsp; &nbsp; 0xfa
octal &nbsp; 0372
unit&nbsp; &nbsp; 250
segment 0000:00fa
string&nbsp; "\xfa"
fvalue: 250.0
float:&nbsp; 0.000000f
double: 0.000000
binary&nbsp; 0b11111010
ternary 0t100021
</pre>

Давайте хакнемо його на _50_ у десятичній системі числення.

<pre spellcheck="false">:&gt; wa movs r0, 0x32 @ 0x00000330
Written 2 byte(s) (movs r0, 0x32) = wx 3220
</pre>

Ми бачимо, що воно насправді дорівнює _50_ у десятичній системі числення.

<pre spellcheck="false">:&gt; ? 0x32
int32 &nbsp; 50
uint32&nbsp; 50
hex &nbsp; &nbsp; 0x32
octal &nbsp; 062
unit&nbsp; &nbsp; 50
segment 0000:0032
string&nbsp; "2"
fvalue: 50.0
float:&nbsp; 0.000000f
double: 0.000000
binary&nbsp; 0b00110010
ternary 0t1212
</pre>

Давайте також змішаємо його лише вліво один раз, щоб воно перетворилося на _100_ при зміщенні вліво лише один раз.

<pre spellcheck="false">:&gt; wa lsls r0, r0, 1 @ 0x00000332
Written 2 byte(s) (lsls r0, r0, 1) = wx 4000
</pre>

Тепер у нас залишається тільки вийти і перетворити нашу __.elf__ на __.uf2__!

<pre spellcheck="false">./elf2uf2/elf2uf2 0x04_int.XyZ9PlH12ZuK8 0x04_int.uf2
</pre>

Вставте Піко і переконайтеся, що ви натискаєте кнопку BOOTSEL або використовуєте налаштування, які я надав у частині 2.

<pre spellcheck="false">cp 0x04_int.uf2 /Volumes/RPI-RP2
</pre>

Давайте його відобразимо!

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

АХА, так!

<pre spellcheck="false">48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
</pre>

У цьому місці ми бачимо, що ми його хакнули на _48_ у десятичній системі числення, і воно друкує кожні 100 мілісекунд!

У наступній лекції ми будуть займатися плаваючими точками та особливим чином, яким Піко обробляє їх, оскільки воно не має співпроцесора.