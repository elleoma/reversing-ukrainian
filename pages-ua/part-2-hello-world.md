## part 2 - Hello World

Сьогодні ми будемо висвітлювати основну установку для створення власних проектів на Raspberry Pi Pico.

Всередині нашої папки __pico__ дозволяє створити __0x02 \ _pico \ _hello \ _world__ папка поряд з __pico-sdk__ and __pico-example__ папки.

<pre spellcheck="false">mkdir 0x02_pico_hello_world
cd 0x02_pico_hello_world
</pre>

Давайте створимо наш VIM __0x02 \ _Hello \ _world.c__ file.

<pre spellcheck="false">vim 0x02_hello_world.c
</pre>

Давайте add наступне.

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

Ми спочатку обробляємо логіку, щоб ініціювати всі стандартні вхідні and вихід.

<pre spellcheck="false">&nbsp; &nbsp; stdio_init_all();
</pre>

Нарешті, ми друкуємо _ "Hello world!" _ Кожні 1 секунди до стандартного виходу в нескінченній петлі.

<pre spellcheck="false">&nbsp; &nbsp; while(1)&nbsp;
&nbsp; &nbsp; {
&nbsp; &nbsp;   printf("Hello world!\n");

&nbsp; &nbsp; &nbsp; sleep_ms(1000);
&nbsp; &nbsp; }
</pre>

Тоді ми після успіху _Return 0_, щоб вказати на успіх, оскільки наша функція _Main_ - це int. Це not технічно необхідна, але хороша практика.

<pre spellcheck="false">    return 0;
</pre>

Робота з __cmake__ значно допомагає в процесі побудови для наших проектів. Спочатку нам потрібно зробити __cmakelist.txt__ file.

<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
встановити(CMAKE_C_STANDARD 11)
встановити(CMAKE_CXX_STANDARD 17)
pico_sdk_init()

add_executable(0x02_hello_world
  0x02_hello_world.c
)

pico_enable_stdio_usb(0x02_hello_world 1)

pico_add_extra_outputs(0x02_hello_world)

target_link_libraries(0x02_hello_world pico_stdlib)
</pre>

Далі нам потрібно скопіювати __pico \ _sdk \ _import.cmake__ file із зовнішньої папки у встановленні __pico-sdk__ у __0x02 \ _hello \ _world__ poper Poper.

<pre spellcheck="false">cp ../pico-sdk/external/pico_sdk_import.cmake .
</pre>

Нарешті ми готові до будівництва.

<pre spellcheck="false">mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake ..
make
</pre>

Це створить ряд файлів and тих, на яких ми будемо зосереджуватися, - це __. Elf__ file, коли справа доходить до налагодження and hacking, що є повним виводом програми, можливо, включаючи інформацію про налагодження and this ____. Програмний код and Дані у формі UF2, яку ви можете перетягувати-and-Drop на плату RP2040, коли він встановлений як USB-накопичувач.

Я знайшов час, щоб підключити кнопку скидання на PICO, щоб я робив not, щоб тримати відпустку в USB and, натискаючи на завантаження кожного разу, коли мені потрібно повторно розгортати, так ось схема такого.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1616317867358.jpg"/></div>

Щоб натиснути флеш натиснути зовнішню кнопку and, поки вона ще натиснута, натисніть Bootse на платі, а потім відпустіть Bootsel and, нарешті, відпустіть зовнішню кнопку.

Потім просто скопіюйте __. UF2__ file на привід.

<pre spellcheck="false">cp 0x02_hello_world.uf2 /Volumes/RPI-RP2
</pre>

Тоді нам потрібно знайти USB -накопичувач, щоб ви могли зробити наступне.

<pre spellcheck="false">ls /dev/tty.
</pre>

Натисніть вкладку, щоб знайти привід and, тоді в моєму випадку я буду використовувати __screen__ для підключення.

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

Ура! Ви повинні побачити: "Hello world!" до стандартного виходу щосекунди.

На нашому наступному уроці ми будемо налагодити __. Elf__ бінарний у __radare2__.