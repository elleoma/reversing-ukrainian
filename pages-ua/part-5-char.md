## part 5 - char

Сьогодні ми розпочнемо наше висвітлення типів даних С. Ми почнемо з Чар. ЧАР - це найменший адресний блок машини, яка може містити базовий набір символів. Це цілий тип і може бути або може бути підписаний, або без підписання.

Давайте зробимо новий DIR __0x03 \ _char__ і додамо наших __cmakelists.txt__ file в ньому.

<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)&nbsp;
set(CMAKE_CXX_STANDARD 17)&nbsp;
pico_sdk_init()

add_executable(0x03_char
&nbsp; 0x03_char.c
)

pico_enable_stdio_usb(0x03_char 1)

pico_add_extra_outputs(0x03_char)

target_link_libraries(0x03_char pico_stdlib)
</pre>

Далі нам потрібно скопіювати the&nbsp;__pico \ _sdk \ _import.cmake__&nbsp;file із зовнішньої папки в the&nbsp;__pico-sdk__&nbsp;Installation to the&nbsp;__0x03 \ _char__&nbsp;project.

<pre spellcheck="false">cp ../pico-sdk/external/pico_sdk_import.cmake .
</pre>

Давайте створимо наш C file __0x03 \ _Char.c__ і Roll ...

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

<pre spellcheck="false">mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake ..
make
</pre>

Потім просто скопіюйте the&nbsp; __. Uf2__&nbsp;file.

<pre spellcheck="false">cp 0x03_char.uf2 /Volumes/RPI-RP2
</pre>

Тоді нам потрібно знайти USB -накопичувач, щоб ви могли зробити наступне.

<pre spellcheck="false">ls /dev/tty.
</pre>

Натисніть вкладку, щоб знайти накопичувач, а потім у моєму випадку я буду використовуватикси9plh22zuk8__screen__&nbsp;to connect.

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