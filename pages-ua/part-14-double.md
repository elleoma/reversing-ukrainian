## part 14 - подвійний

Сьогодні ми збираємось обробляти подвійний тип даних. Як ми обговорювали, у Піко не існує коопроцесор, який би обробляв числа з плаваючою комою, оскільки це обробляється через ряд функціональних можливостей за допомогою програмного забезпечення в API. Це те ж саме з подвійною точністю.

Давайте попрацюємо з простим прикладом.&nbsp;__0x06 \ _double.c__&nbsp;as.

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

Дуже просто ми призначаємо поплавок of&nbsp;_40.5_&nbsp;into&nbsp;_x_&nbsp;and друкувати його за допомогою the&nbsp;_%f&nbsp;_formatiifior modifior and потім сплять for&nbsp;_1_&nbsp;second.

Давайте зробимо новий dir&nbsp;__0x06 \ _double__&nbsp;and add ur&nbsp;__cmakelists.txt__&nbsp;file.

<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
встановити(CMAKE_C_STANDARD 11)&nbsp;
встановити(CMAKE_CXX_STANDARD 17)&nbsp;
pico_sdk_init()

add_executable(0x06_double
&nbsp; 0x06_double.c
)

pico_enable_stdio_usb(0x06_double 1)

pico_add_extra_outputs(0x056_double)

target_link_libraries(0x06_double pico_stdlib)
</pre>

Далі нам потрібно скопіювати the&nbsp;__pico \ _sdk \ _import.cmake__nbspfile із зовнішньої папки в the&nbsp;__pico-sdk__&nbsp;Installation to the&nbsp;__0x06 \ _double__&nbsp;project.

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

<pre spellcheck="false">cp 0x06_double.uf2 /Volumes/RPI-RP2
</pre>

Тоді нам потрібно знайти USB -накопичувач, щоб ви могли зробити наступне.

<pre spellcheck="false">ls /dev/tty.
</pre>

Натисніть вкладку, щоб знайти привід and, а потім у моєму випадку я буду use&nbsp;__screen__&nbsp;to connect.

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

Ви повинні побачити Anchyz9plh86zuk8_40.5_&nbsp;being надруковано щосекунди.

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