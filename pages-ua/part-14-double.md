Частина 14 - подвійний

Сьогодні ми обробимо подвійний тип даних. Як ми вже обговорювали, в Піко немає співпроцесора для обробки чисел з плаваючою точкою, оскільки це обробляється через серію функцій через програмне забезпечення в API. Це те саме стосується подвійної точності.

Давайте працюємо зі простим прикладом. __0x06\_double.c__&nbsp;as слідує.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; double x = 40.5;

&nbsp; &nbsp; printf("%f\n", x);&nbsp;

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }

&nbsp; return 0;
}
</pre>

Дуже просто ми призначаємо float _40.5_ в _x_ і друкуємо його з форматним модифікатором _%f_ і потім спимося на _1_ секунду.

Давайте створимо новий каталог __0x06\_double__&nbsp;and додамо наш __CMakeLists.txt__ file в нього.

<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)&nbsp;
set(CMAKE_CXX_STANDARD 17)&nbsp; pico_sdk_init()

add_executable(0x06_double
&nbsp; 0x06_double.c
)

pico_enable_stdio_usb(0x06_double 1)

pico_add_extra_outputs(0x056_double)

target_link_libraries(0x06_double pico_stdlib)
</pre>

Наступне, нам потрібно скопіювати __pico\_sdk\_import.cmake__&nbsp;file з зовнішнього каталогу в інсталяцію __pico-sdk__ в каталог __0x06\_double__&nbsp;project.

<pre spellcheck="false">cp../pico-sdk/external/pico_sdk_import.cmake.
</pre>

Останнім кроком є підготовка до будівництва.

<pre spellcheck="false">mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake..
make
</pre>

Затем просто скопіюйте _.uf2__ file в диск.

<pre spellcheck="false">cp 0x06_double.uf2 /Volumes/RPI-RP2
</pre>

Затем нам потрібно знайти зовнішній диск, щоб ви могли виконати наступні дії.

<pre spellcheck="false">ls /dev/tty.
</pre>

Натисніть табуляцію, щоб знайти диск, а потім у моїй ситуації я використовую __screen__ для підключення.

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

Ви повинні побачити _40.5_ друкується кожну секунду.

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