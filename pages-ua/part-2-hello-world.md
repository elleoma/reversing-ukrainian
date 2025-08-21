## part 2 - Привіт світ

Сьогодні ми будемо висвітлювати основну установку для створення власних проектів на Raspberry Pi Pico.

Всередині нашої папки __pico__ дозволяє створити __0x02 \ _pico \ _hello \ _world__ папку поряд із __pico-sdk__ та __pico-example__ папки.

<pre spellcheck="false">mkdir 0x02_pico_hello_world
cd 0x02_pico_hello_world
</pre>

Давайте створимо наш VIM __0x02 \ _Hello \ _world.c__ file.

<pre spellcheck="false">vim 0x02_hello_world.c
</pre>

Додамо наступне.

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

Спочатку ми обробляємо логіку, щоб ініціювати всі стандартні вхідні та вихідні.

<pre spellcheck="false">&nbsp; &nbsp; stdio_init_all();
</pre>

Нарешті ми друкуємо _ "Привіт світ!" _ Кожні секунди до стандартного виходу в нескінченній петлі.

<pre spellcheck="false">&nbsp; &nbsp; while(1)&nbsp;
&nbsp; &nbsp; {
&nbsp; &nbsp;   printf("Hello world!\n");

&nbsp; &nbsp; &nbsp; sleep_ms(1000);
&nbsp; &nbsp; }
</pre>

Тоді ми після успіху _RETURN 0_, щоб вказати на успіх, оскільки наша функція _Main_ - це int. Це технічно не потрібно, а хороша практика.

<pre spellcheck="false">    return 0;
</pre>

Робота з __cmake__ значно допомагає в процесі побудови для наших проектів. Спочатку нам потрібно зробити __cmakelists.txt__ file.

<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
pico_sdk_init()

add_executable(0x02_hello_world
  0x02_hello_world.c
)

pico_enable_stdio_usb(0x02_hello_world 1)

pico_add_extra_outputs(0x02_hello_world)

target_link_libraries(0x02_hello_world pico_stdlib)
</pre>

Далі нам потрібно скопіювати __pico \ _sdk \ _import.cmake__ file із зовнішньої папки у встановленні __pico-sdk__ до __0x02 \ _hello \ _world__ проект.

<pre spellcheck="false">cp ../pico-sdk/external/pico_sdk_import.cmake .
</pre>

Нарешті ми готові до будівництва.

<pre spellcheck="false">mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake ..
make
</pre>

Це створить ряд файлів, а ті, на які ми будемо зосереджуватися,-це __. Elf__ file, коли мова йде про налагодження та хакерство, що є повним результатом програми, можливо, включаючи інформацію про налагодження та __. Uf2__ file, який є програмним кодом та даними у формі uf2, що ви можете перетягнути.

Я знайшов час, щоб підключити кнопку скидання на PICO, щоб мені не довелося продовжувати відключення в USB і натискаючи на завантаження кожного разу, коли мені потрібно повторно розгортати, щоб ось схема такої.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1616317867358.jpg"/></div>

Щоб натиснути флеш натиснути зовнішню кнопку, і поки вона ще натиснута, натисніть Bootse на платі, а потім відпустіть завантаження і, нарешті, відпустіть зовнішню кнопку.

Потім просто скопіюйте __. UF2__ file на привід.

<pre spellcheck="false">cp 0x02_hello_world.uf2 /Volumes/RPI-RP2
</pre>

Тоді нам потрібно знайти USB -накопичувач, щоб ви могли зробити наступне.

<pre spellcheck="false">ls /dev/tty.
</pre>

Натисніть вкладку, щоб знайти накопичувач, а потім у моєму випадку я буду використовувати __screen__ для підключення.

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

Ура! Ви повинні бачити: "Привіт світ!" до стандартного виходу щосекунди.

На нашому наступному уроці ми будемо налагодити __. Elf__ бінарний у __radare2__.