## part 5 - char

Сьогодні ми розпочнемо наше висвітлення типів даних С. Ми почнемо з Чар. ЧАР - це найменший адресний блок машини, яка може містити базовий набір символів. Це цілий тип and може бути або може бути підписаним or без підписання.

Давайте зробимо новий DIR __0x03 \ _char__ and add наші __cmakelists.txt__ file в ньому.

<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
встановити(CMAKE_C_STANDARD 11)&nbsp;
встановити(CMAKE_CXX_STANDARD 17)&nbsp;
pico_sdk_init()

add_executable(0x03_char
&nbsp; 0x03_char.c
)

pico_enable_stdio_usb(0x03_char 1)

pico_add_extra_outputs(0x03_char)

target_link_libraries(0x03_char pico_stdlib)
</pre>

Далі нам потрібно скопіювати the&nbsp;__pico \ _sdk \ _import.cmake__&nbsp;file із зовнішньої папки в the&nbsp;__pico-sdk__&nbsp;Installation to to The&nbsp;__0x03 \ _char__&nbsp;project.

<pre spellcheck="false">cp ../pico-sdk/external/pico_sdk_import.cmake .
</pre>

Давайте створимо наш C file __0X03 \ _Char.C__ and Roll ...

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; char x = 'x';
&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;
&nbsp; &nbsp; printf("%c\n", x);

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }
&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;
&nbsp; return 0;
}
</pre>

Нарешті ми готові до будівництва.

nbsp

Потім просто скопіюйте the&nbsp; __. Uf2__&nbsp;file на привід.

<pre spellcheck="false">cp 0x03_char.uf2 /Volumes/RPI-RP2
</pre>

Тоді нам потрібно знайти USB -накопичувач, щоб ви могли зробити наступне.

<pre spellcheck="false">ls /dev/tty.
</pre>

Натисніть вкладку, щоб знайти привід and, а потім у моєму випадку я буду use&nbsp;__screen__&nbsp;to connect.

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

Ви повинні бачити, що "X" надрукується щосекунди.

<pre spellcheck="false">x
x
x
x
x
x
</pre>

Наступний урок ми будемо налагодити Чар.