## Частина 8 - int

Сьогодні ми працюємо з типом даних int, які нічим не відрізняються від цілочисельних значень. Вони можуть бути підписаними або несписаними.

Давайте розглянемо простий приклад. __0x04\_int.c__ виглядає так.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

XyZ9PlH6ZuK8 main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; XyZ9PlH7ZuK8 x = 40;&nbsp;

&nbsp; &nbsp; XyZ9PlH0ZuK8("%d\n", x);&nbsp;

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }

&nbsp; return 0;
}
</pre>

У цьому випадку ми просто використовуємо наш стандартний функціонал IO, який слідує за нашою нескінченною петлею. Ми просто присвоюємо _40_ типу даних int змінній _x_ і друкуємо її за допомогою формату _%d_ і спляємо протягом _1_ секунди.

Давайте створимо новий каталог __0x04\_int__&nbsp;and і додамо наш __CMakeLists.txt__ file в нього.

<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)&nbsp;
set(CMAKE_CXX_STANDARD 17)&nbsp;
pico_sdk_init()

add_executable(0x04_int
&nbsp; 0x04_int.c
)

pico_enable_stdio_usb(0x04_int 1)

pico_add_extra_outputs(0x04_int)

target_link_libraries(0x04_int pico_stdlib)
</pre>

Далі нам потрібно скопіювати __pico\_sdk\_import.cmake__&nbsp;file з зовнішнього каталогу в інсталяцію __pico-sdk__ в каталог __0x04\_int__&nbsp;project.

<pre spellcheck="false">cp ../pico-sdk/external/pico_sdk_import.cmake .
</pre>

Нарешті, ми готові до будівництва.

<pre spellcheck="false">mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake ..
make
</pre>

Далі просто скопіюйте файл _.uf2__ file в диск.

<pre spellcheck="false">cp 0x04_int.uf2 /Volumes/RPI-RP2
</pre>

Далі нам потрібно знайти зовнішній диск, щоб ви могли виконати наступні дії.

<pre spellcheck="false">ls /dev/tty.
</pre>

Натисніть табуляцію, щоб знайти диск, а потім у моїй ситуації я використовую __screen__ для підключення.

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

Ви повинні побачити, що _40_ друкується кожну секунду.

<pre spellcheck="false">40
40
40
40
40
40
40
40
40
40
40
40
</pre>

У наступній лекції ми навчимося відлагоджувати.