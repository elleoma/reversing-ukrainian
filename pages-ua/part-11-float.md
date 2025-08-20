## part 11 - float

Сьогодні ми збираємось обробляти тип даних Float. У PICO немає коопроцесора, який би обробляв числа з плаваючою комою, оскільки це обробляється через ряд функціональності за допомогою програмного забезпечення в API.

Давайте попрацюємо з простим прикладом.&nbsp;__0x05 \ _float.c__&nbsp;as.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; float x = 40.5;

&nbsp; &nbsp; printf("%f\n", x);&nbsp;

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }

&nbsp; return 0;
}
</pre>

Дуже просто ми призначаємо поплавок _40.5_ в _x_ and надрукувати його з модифікатором _%f _format and, а потім спимо на _1_ секунду.

Давайте зробимо новий dir&nbsp;__20x05 \ _float__&nbsp;and add ur&nbsp;__cmakelists.txt__&nbsp;file.

<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
встановити(CMAKE_C_STANDARD 11)&nbsp;
встановити(CMAKE_CXX_STANDARD 17)&nbsp;
pico_sdk_init()

add_executable(0x05_float
&nbsp; 0x05_float.c
)

pico_enable_stdio_usb(0x05_float 1)

pico_add_extra_outputs(0x05_float)

target_link_libraries(0x05_float pico_stdlib)
</pre>

Далі нам потрібно скопіювати the&nbsp;__pico \ _sdk \ _import.cmake__&nbsp;file із зовнішньої папки в the&nbsp;__pico-sdk__&nbsp;Installation to to the&nbsp;__0x05 \ _float__&nbsp;project.

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

<pre spellcheck="false">cp 0x05_float.uf2 /Volumes/RPI-RP2
</pre>

Тоді нам потрібно знайти USB -накопичувач, щоб ви могли зробити наступне.

<pre spellcheck="false">ls /dev/tty.
</pre>

Натисніть вкладку, щоб знайти привід and, тоді в моєму випадку я буду використовуватикси9plh68zuk8__screen__&nbsp;to connect.

nbsp

Ви повинні побачити Anchyz9plh70zuk8_40.5_&nbsp;being надруковано щосекунди.

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

На нашому наступному уроці ми будемо налагодити.