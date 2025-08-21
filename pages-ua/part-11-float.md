## Частина 11 - плавання

Сьогодні ми обробимо тип даних плавання. У Піко немає співпроцесора для обробки чисел з плаваючою точкою, оскільки це обробляється через серію функцій через програмне забезпечення в API.

Давайте працюємо зі простим прикладом.&nbsp;__0x05\_float.c__&nbsp;as слідує.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

XyZ9PlH4ZuK8 main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; float x = 40.5;

&nbsp; &nbsp; XyZ9PlH0ZuK8("%f\n", x);&nbsp;

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }

&nbsp; return 0;
}
</pre>

Дуже просто ми призначаємо плавання _40.5_ в _x_ і друкуємо його з форматним модифікатором _%f_ і потім спимося на _1_ секунду.

Давайте створимо нову папку&nbsp;__0x05\_float__&nbsp;and додамо нашу&nbsp;__CMakeLists.txt__&nbsp;file в неї.

<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)&nbsp;
set(CMAKE_CXX_STANDARD 17)&nbsp;
pico_sdk_init()

add_executable(0x05_float
&nbsp; 0x05_float.c
)

pico_enable_stdio_usb(0x05_float 1)

pico_add_extra_outputs(0x05_float)

target_link_libraries(0x05_float pico_stdlib)
</pre>

Далі нам потрібно скопіювати&nbsp;__pico\_sdk\_import.cmake__&nbsp;file з зовнішньої папки в папці&nbsp;__pico-sdk__ встановлення в папку&nbsp;__0x05\_float__&nbsp;project.

<pre spellcheck="false">cp ../pico-sdk/external/pico_sdk_import.cmake .
</pre>

Нарешті ми готові до будівництва.

<pre spellcheck="false">mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake ..
make
</pre>

Далі просто скопіюйте&nbsp;__.uf2__&nbsp;file в диск.

<pre spellcheck="false">cp 0x05_float.uf2 /Volumes/RPI-RP2
</pre>

Далі нам потрібно знайти зовнішній диск, щоб ви могли виконати наступні дії.

<pre spellcheck="false">ls /dev/tty.
</pre>

Натисніть табуляцію, щоб знайти диск, а потім у моїй ситуації я використовую&nbsp;__screen__&nbsp;для підключення.

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

Ви повинні побачити, що _40.5_ друкується кожну секунду.

<pre spellcheck="false">40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
40.500000
</pre>

У наступному урокі ми навчимося відлагоджувати.