## part 10 - Hacking int

Сьогодні ми hack Проста програма int. Давайте розглянемо код.

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

Давайте розберемося в нашому налагоджувач.

<pre spellcheck="false">radare2 -w arm -b 16 0x04_int.elf
</pre>

Давайте автоматично проаналізуємо.

<pre spellcheck="false">aaaa
</pre>

Давайте прагнемо main.

<pre spellcheck="false">s main
</pre>

Перейдемо у візуальний режим, typing&nbsp;__v__&nbsp;and then&nbsp;__p__&nbsp;twice, щоб дістатися до хорошого налагоджувач виду.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1617616216893.jpg"/></div>

Ми збираємось спочатку hack int, яке ми знаємо, це _40_ десятковий or _28_ hex.

<pre spellcheck="false">:&gt; wa movs r1, 0x30 @ 0x00000328
Written 2 byte(s) (movs r1, 0x30) = wx 3021
</pre>

Тут ми бачимо _0x30_ IS _48_ десятковий.

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

Ми також бачимо, що _0xfa_, який ми знаємо, це _250_ десятковий - це наша 1/4 мілісекундна затримка, що, коли зміщується ліворуч, множиться, and стає _1000_ десятковим на 1 секунду.

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

Давайте hack, що до _50_ десяткового.

<pre spellcheck="false">:&gt; wa movs r0, 0x32 @ 0x00000330
Written 2 byte(s) (movs r0, 0x32) = wx 3220
</pre>

Ми можемо бачити, що це насправді _50_ десятковий.

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

Давайте також змістимо його лише один раз таким, що він займе _50_ десятковий and, перетворивши його на _100_, коли він зміщує ліворуч лише один раз.

<pre spellcheck="false">:&gt; wa lsls r0, r0, 1 @ 0x00000332
Written 2 byte(s) (lsls r0, r0, 1) = wx 4000
</pre>

Все, що нам потрібно зробити зараз, це exit and перетворити ur&nbsp; __. elf&nbsp;__to&nbsp; __. Uf2__!

<pre spellcheck="false">./elf2uf2/elf2uf2 0x04_int.elf 0x04_int.uf2
</pre>

Підключіть Pico and, переконайтеся, що ви тримаєте Bootsel or Використовуйте налаштування, яку я надав у частині 2.

<pre spellcheck="false">cp 0x04_int.uf2 /Volumes/RPI-RP2
</pre>

Давайте екранимо це!

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

Ага так!

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

Тут ми бачимо, що ми зламали його до 48 десяткових and Він друкує кожні 100 мілісекунд!

На нашому наступному уроці ми будемо мати справу з Floats and Унікальним способом, яким Піко обробляє їх, як це робить not.