Частина 14 - подвійний

Сьогодні ми будемо працювати з подвійним типом даних. Як ми вже обговорювали, в Піко немає співпроцесора для обробки чисел з плаваючою точкою, оскільки це обробляється через серію функцій через програмне забезпечення в API. Це те саме стосується подвійної точності.

Давайте працюємо зі простим прикладом. __0x06\_double.c__&nbsp;as слідує.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

XyZ9PlH4ZuK8 main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; double x = 40.5;

&nbsp; &nbsp; XyZ9PlH0ZuK8("%f\n", x);&nbsp;

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }

&nbsp; return 0;
}
</pre>

Дуже просто ми присвоюємо float _40.5_ змінній _x_ і друкуємо її з форматним модифікатором _%f_ і потім спимося на _1_ секунду.

Давайте створимо нову папку __0x06\_double__&nbsp;and і додамо наш __CMakeLists.txt__ file в неї.

<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)&nbsp;
set(CMAKE_CXX_STANDARD 17)&nbsp;
pico_sdk_init()

add_executable(0x06_double
&nbsp; 0x06_double.c
)

pico_enable_stdio_usb(0x06_double 1)

pico_add_extra_outputs(0x056_double)

target_link_libraries(0x06_double pico_stdlib)
</pre>

Далі нам потрібно скопіювати __pico\_sdk\_import.cmake__&nbsp;file з зовнішньої папки в папці __pico-sdk__ встановлення в папку __0x06\_double__&nbsp;project.

<pre spellcheck="false">cp ../pico-sdk/external/pico_sdk_import.cmake .
</pre>

Нарешті ми готові до будівництва.

<pre spellcheck="false">mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake ..
make
</pre>

Далі просто скопіюйте __.uf2__ file в диск.

<pre spellcheck="false">cp 0x06_double.uf2 /Volumes/RPI-RP2
</pre>

Далі нам потрібно знайти зовнішній диск, щоб ви могли виконати наступні дії.

<pre spellcheck="false">ls /dev/tty.
</pre>

Натисніть таб, щоб знайти диск, а потім у моїй ситуації я використовую __screen__ для підключення.

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