Частина 2 - Привітання світу

Сьогодні ми навчимося створювати власні проекти на Raspberry Pi Pico.

У нашому каталозі __pico__ створимо каталог __0x02\_pico\_hello\_world____ поряд з каталогами __pico-sdk__ і __pico-example__.

ХМДХ<pre spellcheck="false">mkdir 0x02_pico_hello_world
cd 0x02_pico_hello_world
</pre>ХМДХ

Створимо свій vim __0x02\_hello\_world.c__ file.

ХМДХ<pre spellcheck="false">vim 0x02_hello_world.c
</pre>ХМДХ

Додамо наступне.

ХМДХ<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

XMDX8074388f38d3XMDX main()&nbsp;
{	
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp;   XMDX75f455ff1d42XMDX("Hello world!
");

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }
    
  return 0;
}
</pre>ХМДХ

Спочатку обробимо логіку для ініціалізації всіх стандартних вхідних і виходів.

ХМДХ<pre spellcheck="false">&nbsp; &nbsp; stdio_init_all();
</pre>ХМДХ

Нарешті, виведемо _"Привітання світу!"_ кожну секунду до стандартного виходу в нескінченний цикл.

ХМДХ<pre spellcheck="false">&nbsp; &nbsp; while(1)&nbsp;
&nbsp; &nbsp; {
&nbsp; &nbsp;   XMDXf86a742b2f82XMDX("Hello world!
");

&nbsp; &nbsp; &nbsp; sleep_ms(1000);
&nbsp; &nbsp; }
</pre>ХМДХ

Потім після успішного виконання повернемо _0_ для вказівки успішності, оскільки наш функція _main_ є int. Це не технічна вимога, але добра практика.

ХМДХ<pre spellcheck="false">    return 0;
</pre>ХМДХ

Робота з __cmake__ значно полегшує процес будівництва для наших проектів. Спочатку нам потрібно створити __CMakeLists.txt__ file.

ХМДХ<pre spellcheck="false">cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17) pico_sdk_init()

add_executable(0x02_hello_world 0x02_hello_world.c
)

pico_enable_stdio_usb(0x02_hello_world 1)

pico_add_extra_outputs(0x02_hello_world)

target_link_libraries(0x02_hello_world pico_stdlib)
</pre>ХМДХ

Далі нам потрібно скопіювати __pico\_sdk\_import.cmake____ file з зовнішнього каталогу в установці __pico-sdk__ до каталогу проекту __0x02\_hello\_world____.

ХМДХ<pre spellcheck="false">cp../pico-sdk/external/pico_sdk_import.cmake.
</pre>ХМДХ

Нарешті, ми готові до будівництва.

ХМДХ<pre spellcheck="false">mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake..
make
</pre>ХМДХ

Це призведе до створення декількох файлів, і ті, які ми візьмемо до уваги, це __.elf__ file при відладці і хакінгу, який є повним виводом програми, можливо, включаючи інформацію про відладку, і __.uf2__ file, який є програмним кодом і даними в форматі UF2, який можна перетягнути на до плати RP2040, коли вона встановлена як зовнішній диск.

Я витратив час на підключення кнопки перезавантаження на Піко, щоб я не мав роз'єднувати USB і натискати BOOTSEL кожного разу, коли мені потрібно перезавантажити, тому ось схема такого.

ХМДХ<XMDX1226887aa769XMDX class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1616317867358.jpg"/></XMDX4154dc41f172XMDX>ХМДХ

Щоб перезавантажити, натисніть зовнішню кнопку і під час її натискання натисніть кнопку BOOTSEL на платі, потім звільніть кнопку BOOTSEL і, нарешті, звільніть зовнішню кнопку.

Затем просто скопіюйте __.uf2__ file в зовнішній диск.

ХМДХ<pre spellcheck="false">cp 0x02_hello_world.uf2 /Volumes/RPI-RP2
</pre>ХМДХ

Затем нам потрібно знайти зовнішній диск, щоб ви могли виконати наступні дії.

ХМДХ<pre spellcheck="false">ls /dev/tty.
</pre>ХМДХ

Натисніть таб, щоб знайти зовнішній диск, а потім у моїх випадках я використовую __screen__ для підключення.

ХМДХ<pre spellcheck="false">screen /dev/tty.usbmodem0000000000001
</pre>ХМДХ

Вітаємо! Ви повинні побачити "Привітання світу!" до стандартного виходу кожну секунду.

У наступному урокі ми навчимося відлагоджувати __.elf__ бінарний файл в __Radare2__.

У наступному уроку ми навчимося відлагоджувати __.elf__ бінарний файл в __Radare2__.