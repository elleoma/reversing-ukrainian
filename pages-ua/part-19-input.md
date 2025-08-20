## part 19 - введення

Останні два уроки, сподіваємось, демонстрували необхідність зрілого підходу до обробки введення будь -якого серйозного додатку.

Сьогодні ми створимо належну вхідну архітектуру для PICO, пов’язаного зі stdin nbsp stdio.

Почнемо зі створення __input.h__ наступним чином.

<pre spellcheck="false">void input_proc(char type, char* p_usb_char, char* p_usb_string, const int* p_USB_STRING_SIZE);
void flush_input(char* p_usb_string);
</pre>

Тут ми налаштували наш заголовок введення file для вирішення параметрів, про які ми обговорювали на останньому уроці. Ми також встановлюємо нашу функцію _flush \ _input_ для обробки очищення вхідного буфера після того, як він буде використаний для того, щоб він був чистим до отримання нового входу для іншого call до _input \ _proc_.

Далі ми створимо наш __print.h __as наступне.

<pre spellcheck="false">void print_proc(char* p_usb_char, char* p_usb_string);
</pre>

Дуже просто ми збираємося пройти в масиві Char від абонента, щоб обробляти кожен Char and масив Char від абонента, щоб обробляти створення рядка.

Далі ми створимо наш __input.c__ наступним чином.

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

void input_proc(char type, char* p_usb_char, char* p_usb_string, const int* p_USB_STRING_SIZE)
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

У цей момент все слід повністю зрозуміти з вищезазначеним. Якщо це not, перегляньте останні два уроки.

Далі ми створимо наш __print.c__ наступним чином.

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

Тут ми приносимо нашу дію char and string string and, якщо натиснута клавіша повернення надрукує вміст рядка and, тоді call _flush \ _input_, щоб очистити буфер, як обговорювалося.

Нарешті ми створимо наш __main.c__ наступним чином.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"
#include "print.h"
#include "input.h"

int main()
{
&nbsp; stdio_init_all();

&nbsp; const int USB_STRING_SIZE = 100;
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

Тут ми просто встановлюємо нашу вхідну процедуру для обробки введення поплавця.

Давайте зробимо новий dir&nbsp;____0x07 \ _input__&nbsp;and add ur&nbsp;__cmakelists.txt__&nbsp;xyz9zuk8

<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
встановити(CMAKE_C_STANDARD 11)&nbsp;
встановити(CMAKE_CXX_STANDARD 17)&nbsp;
встановити(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE}")
встановити(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE}")
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

Далі нам потрібно скопіювати the&nbsp;__pico \ _sdk \ _import.cmake__&nbsp;file із зовнішньої папки в te&nbsp;__pico-sdk__&nbsp;__pico-sdk__&nbsp;ipation tO The&nbsp;__0x07 \ _input__&nbsp;project.

<pre spellcheck="false">cp ../pico-sdk/external/pico_sdk_import.cmake .
</pre>

Нарешті ми готові до будівництва.

<pre spellcheck="false">mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake ..
make
make flash
</pre>

Я додав у MakeFile променевий режим, щоб заощадити нам час від копіювання до піко. Не забудьте спочатку поставити PICO в режим спалаху.

Тоді нам потрібно знайти USB -накопичувач, щоб ви могли зробити наступне.

<pre spellcheck="false">ls /dev/tty.
</pre>

Натисніть вкладку, щоб знайти привід and, тоді в моєму випадку я буду use&nbsp;__screen__&nbsp;to connect.

<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>

Бум! Тепер ви побачите, що зможете ввести числа and лише один десятковий пункт. Ми правильно обробляємо для зворотного розвору and, коли ви досягнете максимуму 100 chars, він буде not дозволить набирати далі. Нарешті він відручує те, що ви набрали.

<pre spellcheck="false">32.3333
32.3333
32.11111111
32.11111111
7.99999003902930420384802384082304820384028342340284923840238948230482938429034823948293849023849223
7.99999003902930420384802384082304820384028342340284923840238948230482938429034823948293849023849223
</pre>

На нашому наступному уроці ми будемо налагодити.