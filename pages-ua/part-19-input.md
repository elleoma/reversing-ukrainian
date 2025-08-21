## Частина 19 - Ввід

Останні дві лекції, надіяється, показали необхідність серйозного підходу до обробки вхідних даних будь-якої серйозної програми.

Сьогодні ми розробимо належну архітектуру вхідних даних для Pico, пов'язану зі STDIN і STDIO.

Хай ми почнемо створення нашого __input.h__ наступним чином.

<pre spellcheck="false">void input_proc(char type, char* p_usb_char, char* p_usb_string, const XyZ9PlH14ZuK8* p_USB_STRING_SIZE);
void flush_input(char* p_usb_string);
</pre>

У цьому місці ми встановлюємо наш вхідний заголовок file для обробки параметрів, про які ми говорили в останній лекції. Також ми встановлюємо нашу _flush\_input_ функцію для очищення буфера вхідних даних після використання, щоб він був чистий перед отриманням нових даних для іншого call до _input\_proc_.

Наступно ми створимо наш __print.h __якщо:

<pre spellcheck="false">void print_proc(char* p_usb_char, char* p_usb_string);
</pre>

Дуже просто ми передаємо вхідний масив символів від викликаючого програми для обробки кожного символу і масив символів від викликаючого програми для створення рядка.

Наступно ми створимо наш __input.c__ наступним чином.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include "pico/stdlib.h"

#define ZERO 0x30
#define NINE 0x39
#define PERIOD 0x2e
#define CAPITAL_A 0x41
#define LOWER_CASE_Z 0x7a
#define BACKSPACE 0x08
#define DEL 0x7f

void input_proc(char type, char* p_usb_char, char* p_usb_string, const XyZ9PlH15ZuK8* p_USB_STRING_SIZE)
{
&nbsp; *p_usb_char = '\0';
&nbsp; *p_usb_char = getchar_timeout_us(0);
&nbsp; if(*p_usb_char == BACKSPACE || *p_usb_char == DEL)
&nbsp; {
&nbsp; &nbsp; if(p_usb_string[0] != '\0')
&nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; printf("\b");
&nbsp; &nbsp; &nbsp; printf(" ");
&nbsp; &nbsp; &nbsp; printf("\b");
&nbsp; &nbsp; &nbsp; p_usb_string[strlen(p_usb_string)-1] = '\0';
&nbsp; &nbsp; }
&nbsp; }
&nbsp; if(type == 'f')
&nbsp; {&nbsp;
&nbsp; &nbsp; char* period;
&nbsp; &nbsp; while((*p_usb_char &gt;= ZERO &amp;&amp; *p_usb_char &lt;= NINE) || *p_usb_char == PERIOD)
&nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; if(*p_usb_char == PERIOD)
&nbsp; &nbsp; &nbsp; &nbsp; period = strchr(p_usb_string, '.');
&nbsp; &nbsp; &nbsp; if(period == NULL)&nbsp;
&nbsp; &nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; &nbsp; if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
&nbsp; &nbsp; &nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; putchar(*p_usb_char);
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; strncat(p_usb_string, p_usb_char, 1);
&nbsp; &nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; &nbsp; &nbsp; *p_usb_char = '\0';
&nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; &nbsp; else
&nbsp; &nbsp; &nbsp; &nbsp; break;
&nbsp; &nbsp; }
&nbsp; }
&nbsp; else if(type == 'd')
&nbsp; {&nbsp;
&nbsp; &nbsp; while(*p_usb_char &gt;= ZERO &amp;&amp; *p_usb_char &lt;= NINE)
&nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
&nbsp; &nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; &nbsp; putchar(*p_usb_char);
&nbsp; &nbsp; &nbsp; &nbsp; strncat(p_usb_string, p_usb_char, 1);
&nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; &nbsp; *p_usb_char = '\0';
&nbsp; &nbsp; }
&nbsp; }
&nbsp; else if(type == 's')
&nbsp; {&nbsp;
&nbsp; &nbsp; while(*p_usb_char &gt;= CAPITAL_A &amp;&amp; *p_usb_char &lt;= LOWER_CASE_Z)
&nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
&nbsp; &nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; &nbsp; putchar(*p_usb_char);
&nbsp; &nbsp; &nbsp; &nbsp; strncat(p_usb_string, p_usb_char, 1);
&nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; &nbsp; *p_usb_char = '\0';
&nbsp; &nbsp; }
&nbsp; }
}

void flush_input(char* p_usb_string)
{
&nbsp; p_usb_string[0] = '\0';
}
</pre>

Усі речі повинні бути повністю зрозумілі на цьому етапі, якщо ні, то зверніться до останніх двох лекцій.

Наступно ми створимо наш __print.c__ наступним чином.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"
#include "input.h"

#define RETURN 0x0d

void print_proc(char* p_usb_char, char* p_usb_string)
{
&nbsp; if(*p_usb_char == RETURN)
&nbsp; {
&nbsp; &nbsp; if(p_usb_string[0] == '\0')
&nbsp; &nbsp; &nbsp; printf("\n");
&nbsp; &nbsp; else
&nbsp; &nbsp; &nbsp; printf("\n%s\n", p_usb_string);
&nbsp; &nbsp; flush_input(p_usb_string);
&nbsp; }
}
</pre>

У цьому місці ми імпортуємо нашу здатність обробляти символи і рядки і якщо натиснути клавішу повернення, друкуємо вміст рядка і потім call _flush\_input_ для очищення буфера, про який ми говорили раніше.

Останнім кроком ми створимо наш __main.c__ наступним чином.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"
#include "print.h"
#include "input.h"

XyZ9PlH16ZuK8 main()
{
&nbsp; stdio_init_all();

&nbsp; const XyZ9PlH17ZuK8 USB_STRING_SIZE = 100;
&nbsp; char usb_char;
&nbsp; usb_char = '\0';
&nbsp; char usb_string[USB_STRING_SIZE];
&nbsp; usb_string[0] = '\0';
&nbsp;&nbsp;
&nbsp; while(1)
&nbsp; {&nbsp; &nbsp;
&nbsp; &nbsp; input_proc('f', &amp;usb_char, usb_string, &amp;USB_STRING_SIZE);
&nbsp; &nbsp; print_proc(&amp;usb_char, usb_string);
&nbsp; }

&nbsp; return 0;
}
</pre>

У цьому місці ми встановлюємо нашу вхідну процедуру для обробки вхідних даних типу float.

Хай ми створимо новий каталог __0x07\_input__&nbsp;and і додамо нашу __CMakeLists.txt__ file в нього.

<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)&nbsp;
set(CMAKE_CXX_STANDARD 17)&nbsp;
set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE}")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE}")
pico_sdk_init()

add_executable(main
&nbsp; main.c
&nbsp; print.c
&nbsp; input.c
)

pico_enable_stdio_usb(main 1)
pico_enable_stdio_uart(main 0)
pico_add_extra_outputs(main)

target_link_libraries(main pico_stdlib hardware_i2c)

add_custom_target(flash
&nbsp; &nbsp; COMMAND cp main.uf2 /Volumes/RPI-RP2/
&nbsp; &nbsp; DEPENDS main
)
</pre>

Наступно нам потрібно скопіювати __pico\_sdk\_import.cmake__&nbsp;XyZ9PlH13ZuK8 з зовнішнього каталогу в __pico-sdk__ встановлення в каталог __0x07\_input__&nbsp;project.

<pre spellcheck="false">cp ../pico-sdk/external/pico_sdk_import.cmake .
</pre>

Останнім кроком ми готові до збірки.

<pre spellcheck="false">mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake ..
make
make flash
</pre>

Я додав рутину збереження в пам'яті в makefile, щоб уникнути копіювання даних на Pico. Пам'ятайте, що потрібно встановити Pico в режим збереження в пам'яті раніше.

Наступно нам потрібно знайти зовнішній накопичувач, щоб виконати наступні дії.

<pre spellcheck="false">ls /dev/tty.
</pre>

Натисніть клавішу табуляції, щоб знайти накопичувач, а потім у моїх випадках я використовую __screen__ для підключення.

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

Бум! Тепер ви побачите, що зможете тільки вводити числа і тільки одне місце після коми. Ми належно обробляємо відміну символів і коли ви досягнете максимальної кількості 100 символів, воно не дозволить вам вводити більше символів. Останнім кроком воно друкує вміст введених даних.

<pre spellcheck="false">32.3333
32.3333
32.11111111
32.11111111
7.99999003902930420384802384082304820384028342340284923840238948230482938429034823948293849023849223
7.99999003902930420384802384082304820384028342340284923840238948230482938429034823948293849023849223
</pre>

У наступній лекції ми розпочнемо процес відлагодження.