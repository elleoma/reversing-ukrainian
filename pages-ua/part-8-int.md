## part 8 - int

Сьогодні ми будемо працювати з типом даних int, який є не що інше, як цілі цифри. Вони також можуть бути підписані або непідписані.

Давайте попрацюємо з простим прикладом. __0x04 \ _int.c__ наступним чином.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; int x = 40;&nbsp;

&nbsp; &nbsp; printf("%d\n", x);&nbsp;

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }

&nbsp; return 0;
}
</pre>

Тут ми просто маємо нашу стандартну функцію IO, а потім наша нескінченна петля. Ми просто призначаємо _40_ типу даних int _X_ та роздрукуємо його за допомогою модифікатора формату _%D_ і спите для _1_ секунди.

Давайте зробимо новий dir&nbsp;__0x04 \ _int__&nbsp;and додайте ur&nbsp;__cmakelists.txt__&nbsp;file в ньому.

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

Далі нам потрібно скопіювати the&nbsp;__pico \ _sdk \ _import.cmake__&nbsp;file із зовнішньої папки в the&nbsp;__pico-sdk__&nbsp;installation tot to the&nbsp;__0x04 \ _int__&nbsp;project.

<pre spellcheck="false">cp ../pico-sdk/external/pico_sdk_import.cmake .
</pre>

Нарешті ми готові до будівництва.

<pre spellcheck="false">mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake ..
make
</pre>

Потім просто скопіюйте the&nbsp; __. Uf2__&nbsp;file на привід.

<pre spellcheck="false">cp 0x04_int.uf2 /Volumes/RPI-RP2
</pre>

Тоді нам потрібно знайти USB -накопичувач, щоб ви могли зробити наступне.

<pre spellcheck="false">ls /dev/tty.
</pre>

Натисніть вкладку, щоб знайти накопичувач, а потім у моєму випадку я буду використовуватикси9plh29zuk8__screen__&nbsp;to Connect.

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

Ви повинні бачити, як _40_ надрукується щосекунди.

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

На нашому наступному уроці ми будемо налагодити.