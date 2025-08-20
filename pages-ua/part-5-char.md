---
{}
---

__Placeholder_16__ Частина 5 - Чар

Сьогодні ми розпочнемо наше висвітлення типів даних С. Ми почнемо з Чар. ЧАР - це найменший адресний блок машини, яка може містити базовий набір символів. Це цілий тип __placeholder_29__ може бути або може бути підписаним __placeholder_18__ без підписання.

Давайте зробимо новий DIR __0x03 \ _char__ __placeholder_30__ __placeholder_23__ Наші __cmakelists.txt__ __placeholder_19__ в ньому.

__Placeholder_0__cmake_minimum_required (версія 3.13)

включити (pico_sdk_import.cmake)

Проект (test_project c cxx asm)
set (cmake_c_standard 11) & nbsp;
set (cmake_cxx_standard 17) & nbsp;
pico_sdk_init ()

add_executable (0x03_char
& nbsp; 0x03_char__placeholder_34__
)

pico_enable_stdio_usb (0x03_char 1)

pico_add_extra_outputs (0x03_char)

Target_Link_Libraries (0x03_char Pico_stdlib)
__Placeholder_1__

Далі нам потрібно скопіювати & nbsp; __ pico \ _sdk \ _import.cmake __ & nbsp; __ ploadholder_20__ із зовнішньої папки в & nbsp; __ pico-sdk __ & nbsp; інсталяція до & nbsp; __ 0x03 \ _char __ & nbsp;

__Placeholder_2__cp ../pico-sdk/external/pico_sdk_import.cmake.
__Placeholder_3__

Давайте створимо наш c __placeholder_21__ __0x03 \ _char.c__ __placeholder_31__ roll ...

__Placeholder_4 __#включити & lt; stdio__placeholder_25 __ & gt;
__Placeholder_17__ включити "pico/stdlib__placeholder_26__"

__Placeholder_24__ main () & nbsp;
{
& nbsp; stdio_init_all ();

& nbsp; в той час як (1) & nbsp;
& nbsp; {
& nbsp; & nbsp; char x = 'x';
& nbsp; & nbsp; & nbsp; & nbsp; & nbsp;
& nbsp; & nbsp; __Placeholder_33 __ ("%c \ n", x);

& nbsp; & nbsp; Sleep_ms (1000);
& nbsp; }
& nbsp; & nbsp; & nbsp; & nbsp; & nbsp;
& nbsp; повернення 0;
}
__Placeholder_5__

Нарешті ми готові до будівництва.

__Placeholder_6__mkdir
Комплект компакт -дисків
Експорт PICO_SDK_PATH = ../../PICO-SDK
cmake ..
робити
__Placeholder_7__

Потім просто скопіюйте & nbsp; __. Uf2 __ & nbsp; __ ploadholder_222 на диск.

__Placeholder_8__cp 0x03_char.uf2 /томи /rpi-rp2
__Placeholder_9__

Тоді нам потрібно знайти USB -накопичувач, щоб ви могли зробити наступне.

__Placeholder_10__ls /__ ploadholder_27 __ /tty.
__Placeholder_11__

Натисніть вкладку, щоб знайти накопичувач __placeholder_32__, тоді в моєму випадку я буду використовувати & nbsp; __ екран __ & nbsp; для підключення.

__Placeholder_12__screen /__placeholder_28__/tty.usbmodem00000000001
__Placeholder_13__

Ви повинні бачити, що "X" надрукується щосекунди.

__Placeholder_14__x
X
X
X
X
X
__Placeholder_15__

Наступний урок ми будемо налагодити Чар.