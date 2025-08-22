Частина 5 - char

Сьогодні ми почнемо нашу обробку даних типу C. Почнемо з char. Char є найменшим адресованим одиницею машини, яка може містити базовий набір символів. Це ціле число і може бути підписаним або несписаним.

Давайте створимо новий каталог __0x03\_char____ і додамо наш __CMakeLists.txt__ __file__ в нього.

__<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)&nbsp;
set(CMAKE_CXX_STANDARD 17)&nbsp; pico_sdk_init()

add_executable(0x03_char
&nbsp; 0x03_char.c
)

pico_enable_stdio_usb(0x03_char 1)

pico_add_extra_outputs(0x03_char)

target_link_libraries(0x03_char pico_stdlib)
</pre>__

Далі нам потрібно скопіювати __pic__ __o\_sdk\_import.cmake__&nbsp;file__ з зовнішнього каталогу в __pico-sdk__ встановлення в каталог __0x03\_char__&nbsp;project__.

__<pre spellcheck="false">cp../pico-sdk/external/pico_sdk_import.cmake.
</pre>__

Давайте створимо наш C __file__ __0x03\_char.c____ і продовжимо...

__<pre spellcheck="false">#include &lt;stdio.h&gt;
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
</pre>__

Нарешті, ми готові до будівництва.

__<pre spellcheck="false">mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake..
make
</pre>__

Далі просто скопіюйте ____.uf2__ __file__ в диск.

__<pre spellcheck="false">cp 0x03_char.uf2 /Volumes/RPI-RP2
</pre>__

Далі нам потрібно знайти зовнішній диск, щоб ви могли виконати наступні дії.

__<pre spellcheck="false">ls /dev/tty.
</pre>__

Натисніть tab, щоб знайти диск, а потім у моїй ситуації я використовую __screen__ для підключення.

__<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>__

Ви повинні побачити "x", яке друкується кожну секунду.

__<pre spellcheck="false">x
x
x
x
x
x
</pre>__

У наступному урокі ми навчимося відлагоджувати char.