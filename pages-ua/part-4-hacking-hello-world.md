Частина 4 - Хакінг Hello World

У останньому урокі ми розглянули, як належно відлагодити наші дуже прості бінарні файли в __Radare2__. Сьогодні ми будемо хакнути цей статичний __.elf__ бінарний файл і перетворити його на __.uf2__ формат і підключити його до нашого Pico і побачити чарівність.

Давайте знову переглянемо наші дуже прості програми.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{	
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp;   printf("Hello world!\n");

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }
    
  return 0;
}
</pre>

Давайте завантажимо наші бінарні файли.

<pre spellcheck="false">radare2 -w arm -b 16 0x02_hello_world.elf
</pre>

Давайте зробимо автоматичну аналітику.

<pre spellcheck="false">aaaa
</pre>

Давайте підійдемо до головної частини програми.

<pre spellcheck="false">s main
</pre>

Давайте використаємо візуальний режим і натисніть p двічі, щоб отримати нашу улюблену оглядову панель.

<pre spellcheck="false">V
</pre>

Давайте переглянемо простий збірник ARM32.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1616443718242.jpg"/></div>

Я б хакнув цей бінарний файл двома способами. Як ми обговорили в останньому урокі, ми бачимо вміст всередині пам'яті _0x00000338_ який містить значення нашої стрічки. Давайте натисніть колонку: і натисніть Enter.

<pre spellcheck="false">:&gt; psz @ [0x00000338]
Hello world!
</pre>

Давайте переглянемо strings. Я хочу, щоб ви звернули увагу на "Hello world!", оскільки ви побачите дві адреси. Адреса на лівому боці - фізична адреса, а адреса прямо справа - віртуальна адреса. Ми будуть займатися віртуальною адресою. Для кращого розуміння давайте зробимо наступне.

<pre spellcheck="false">:&gt; iz~ | less
</pre>

Як ви бачите, наша стрічка знаходиться вгорі.

<pre spellcheck="false">[Strings]
nth paddr&nbsp; &nbsp; &nbsp; vaddr&nbsp; &nbsp; &nbsp; len size section type&nbsp; &nbsp; string
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――
0&nbsp; &nbsp;0x00014cf8 0x00004cf8 12&nbsp; 13&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Hello world!
1&nbsp; &nbsp;0x00014d08 0x00004d08 26&nbsp; 27&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;No spinlocks are available
2&nbsp; &nbsp;0x00014d24 0x00004d24 33&nbsp; 34&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Hardware alarm %d already claimed
3&nbsp; &nbsp;0x00014d48 0x00004d48 15&nbsp; 16&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;\n*** PANIC ***\n
4&nbsp; &nbsp;0x00014d5c 0x00004d5c 11&nbsp; 12&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Hard assert
5&nbsp; &nbsp;0x00014d68 0x00004d68 7&nbsp; &nbsp;8&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Release
6&nbsp; &nbsp;0x00014d70 0x00004d70 5&nbsp; &nbsp;6&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;1.0.0
7&nbsp; &nbsp;0x00014d78 0x00004d78 4&nbsp; &nbsp;5&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;pico
8&nbsp; &nbsp;0x00014d80 0x00004d80 16&nbsp; 17&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;0x02_hello_world
9&nbsp; &nbsp;0x00014d94 0x00004d94 11&nbsp; 12&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Mar 21 2021
10&nbsp; 0x00014db2 0x00004db2 4&nbsp; &nbsp;5&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;uBhM
11&nbsp; 0x00014dbc 0x00004dbc 10&nbsp; 11&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;UART stdin
12&nbsp; 0x00014dc8 0x00004dc8 11&nbsp; 12&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;UART stdout
13&nbsp; 0x00014dd4 0x00004dd4 19&nbsp; 20&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;UART stdin / stdout
14&nbsp; 0x00014dfc 0x00004dfc 18&nbsp; 19&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;USB stdin / stdout
15&nbsp; 0x00014e1c 0x00004e1c 12&nbsp; 13&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Raspberry Pi
16&nbsp; 0x00014e2c 0x00004e2c 4&nbsp; &nbsp;5&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Pico
17&nbsp; 0x00014e34 0x00004e34 12&nbsp; 13&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;000000000000
18&nbsp; 0x00014e44 0x00004e44 9&nbsp; &nbsp;10&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Board CDC
19&nbsp; 0x00014ec4 0x00004ec4 19&nbsp; 20&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Unhandled IRQ 0x%x\n
20&nbsp; 0x00014ed8 0x00004ed8 39&nbsp; 40&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Isochronous wMaxPacketSize %d too large
21&nbsp; 0x00014f00 0x00004f00 30&nbsp; 31&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;ep %d %s was already available
22&nbsp; 0x00014f20 0x00004f20 40&nbsp; 41&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Can't continue xfer on inactive ep %d %s
23&nbsp; 0x00014f4c 0x00004f4c 35&nbsp; 36&nbsp; &nbsp;.rodata ascii&nbsp; &nbsp;Transferred more data than expected
0&nbsp; &nbsp;0x00020135 0x10000135 5&nbsp; &nbsp;6&nbsp; &nbsp;.data&nbsp; &nbsp;ascii&nbsp; &nbsp;V\n`\eh
1&nbsp; &nbsp;0x0002018b 0x1000018b 5&nbsp; &nbsp;6&nbsp; &nbsp;.data&nbsp; &nbsp;ascii&nbsp; &nbsp;&amp;CF\eh
2&nbsp; &nbsp;0x000201a0 0x100001a0 4&nbsp; &nbsp;5&nbsp; &nbsp;.data&nbsp; &nbsp;ascii&nbsp; &nbsp;CF\ey
3&nbsp; &nbsp;0x000201a8 0x100001a8 4&nbsp; &nbsp;5&nbsp; &nbsp;.data&nbsp; &nbsp;ascii&nbsp; &nbsp;CF\eh
4&nbsp; &nbsp;0x000201d0 0x100001d0 4&nbsp; &nbsp;5&nbsp; &nbsp;.data&nbsp; &nbsp;ascii&nbsp; &nbsp;\thAq
5&nbsp; &nbsp;0x0002028d 0x1000028d 5&nbsp; &nbsp;6&nbsp; &nbsp;.data&nbsp; &nbsp;ascii&nbsp; &nbsp;GpF\t8
6&nbsp; &nbsp;0x00020805 0x10000805 5&nbsp; &nbsp;11&nbsp; &nbsp;.data&nbsp; &nbsp;utf16le \a \b \b
7&nbsp; &nbsp;0x00020905 0x10000905 5&nbsp; &nbsp;11&nbsp; &nbsp;.data&nbsp; &nbsp;utf16le \b \t \t
8&nbsp; &nbsp;0x00020a05 0x10000a05 5&nbsp; &nbsp;11&nbsp; &nbsp;.data&nbsp; &nbsp;utf16le \t \n \n
9&nbsp; &nbsp;0x00020b05 0x10000b05 5&nbsp; &nbsp;11&nbsp; &nbsp;.data&nbsp; &nbsp;utf16le \n \v \v
(END)
</pre>

Ви можете побачити значення _0x00004cf8_ яке містить нашу стрічку, щоб підтвердити це ми можемо зробити наступне.

<pre spellcheck="false">:&gt; psz @ 0x00004cf8
Hello world!
</pre>

Давайте хакнемо це.

<pre spellcheck="false">:&gt; w Hacked World! @ [0x00000338]
</pre>

Давайте тепер перевіримо, чи змінилося значення.

<pre spellcheck="false">:&gt; psz @ 0x00004cf8
Hacked World!
</pre>

Іншою річчю, яку я хотів би хакнути, є sleep\_ms яка зараз встановлена на 1000. Пам'ятайте, вона показує 250 десяткове або 0xfa шістнадцяткове і ми логічно зміщуємо ліворуч двічі, як ми обговорили в останньому урокі. Перший логічний зміщення ліворуч буде збільшувати на 2, привівши нас до 500, а другий логічний зміщення ліворуч буде збільшувати на 2, привівши нас до 1000.

<pre spellcheck="false">lsls r0, r0, 2&nbsp;
</pre>

Давайте хакнемо це, змінивши 2 на 1. Це зробить затримку 500 мс або півсекунди.

<pre spellcheck="false">:&gt; wa lsls r0, r0, 1 @ 0x00000330
Written 2 byte(s) (lsls r0, r0, 1) = wx 4000
</pre>

Давайте перевіримо.

<pre spellcheck="false">:&gt; pd 1 @ 0x00000330
│ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 0x00000330&nbsp; &nbsp; &nbsp; 4000 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; lsls r0, r0, 1
</pre>

Ми можемо побачити, що воно змінилося.

Тепер у нас нічого не залишається, як вийти і перетворити наші __.elf__ на __.uf2__!

<pre spellcheck="false">./elf2uf2/elf2uf2 0x02_hello_world.elf 0x02_hello_world.uf2
</pre>

Підключіть Pico і переконайтеся, що ви натискаєте BOOTSEL або використовуєте налаштування, які я надав у останньому урокі.

<pre spellcheck="false">cp 0x02_hello_world.uf2 /Volumes/RPI-RP2
</pre>

Давайте побачимо!

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

АХА!

<pre spellcheck="false">Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
Hacked World!
</pre>

Кожну півсекунду!

У наступному урокі ми обговоримо змінні.