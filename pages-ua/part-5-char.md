Частина 5 - char

Сьогодні ми почнемо своє висвітлення даних типу C. Почнемо з char. Char є найменшим адресованим одиницею машини, яка може містити базовий набір символів. Це ціле тип і може бути підписаним або несписаним.

Давайте створимо новий каталог __0x03\_char__ і додамо наш __CMakeLists.txt__ file в нього.

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

Далі нам потрібно скопіювати __pico\_sdk\_import.cmake__&nbsp;file з зовнішнього каталогу в __pico-sdk__ встановлення в каталог __0x03\_char__&nbsp;project.

<pre spellcheck="false">cp ../pico-sdk/external/pico_sdk_import.cmake .
</pre>

Давайте створимо наш C file __0x03\_char.c__ і продовжимо...

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

XyZ9PlH5ZuK8 main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; char x = 'x';
&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;
&nbsp; &nbsp; XyZ9PlH0ZuK8("%c\n", x);

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

Далі просто скопіюйте _.uf2__ file в диск.

<pre spellcheck="false">cp 0x03_char.uf2 /Volumes/RPI-RP2
</pre>

Далі нам потрібно знайти зовнішній диск, щоб ви могли виконати наступні дії.

<pre spellcheck="false">ls /dev/tty.
</pre>

Натисніть табуляцію, щоб знайти диск, а потім у моїх випадках я використовую __screen__ для підключення.

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

Ви повинні побачити "х" друкується кожну секунду.

<pre spellcheck="false">x
x
x
x
x
x
</pre>

У наступному урокі ми навчимося відлагоджувати char.