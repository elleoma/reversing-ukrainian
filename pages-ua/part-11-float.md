---
{}
---

__Placeholder_16__ Частина 11 - Float

Сьогодні ми збираємось обробляти тип даних Float. У PICO немає коопроцесора, який би обробляв числа з плаваючою комою, оскільки це обробляється через ряд функціональності за допомогою програмного забезпечення в API.

Давайте попрацюємо з простим прикладом. & Nbsp; __ 0x05 \ _float.c __ & nbsp; наступним чином.

__Placeholder_0 __#включити & lt; stdio__placeholder_23 __ & gt;
__Placeholder_17__ включити "pico/stdlib__placeholder_24__"

__Placeholder_222__ main () & nbsp;
{
& nbsp; stdio_init_all ();

& nbsp; в той час як (1) & nbsp;
& nbsp; {
& nbsp; & nbsp; float x = 40,5;

& nbsp; & nbsp; __Placeholder_31 __ ("%f \ n", x); & nbsp;

& nbsp; & nbsp; Sleep_ms (1000);
& nbsp; }

& nbsp; повернення 0;
}
__Placeholder_1__

Дуже просто ми призначаємо поплавок _40.5_ в _x_ __placeholder_27__ надрукувати його за допомогою модифікатора _%f _format __placeholder_28__, потім спить на _1_ секунду.

Давайте зробимо новий dir & nbsp; __ 0x05 \ _float __ & nbsp; __ ploadholder_29__ __placeholder_21__ Наші & nbsp; __ cmakelists.txt __ & nbsp; __ placeholder_18__ в ньому.

__Placeholder_2__cmake_minimum_required (версія 3.13)

включити (pico_sdk_import.cmake)

Проект (test_project c cxx asm)
set (cmake_c_standard 11) & nbsp;
set (cmake_cxx_standard 17) & nbsp;
pico_sdk_init ()

add_executable (0x05_float
& nbsp; 0x05_float__placeholder_32__
)

pico_enable_stdio_usb (0x05_float 1)

pico_add_extra_outputs (0x05_float)

Target_Link_Libraries (0x05_float pico_stdlib)
__Placeholder_3__

Далі нам потрібно скопіювати & nbsp; __ pico \ _sdk \ _import.cmake __ & nbsp; __ ploadholder_19__ із зовнішньої папки в & nbsp; __ pico-sdk __ & nbsp; інсталяція до & nbsp; __ 0x05 \ _float __ & nbsp;

__Placeholder_4__cp ../pico-sdk/external/pico_sdk_import.cmake.
__Placeholder_5__

Нарешті ми готові до будівництва.

__Placeholder_6__mkdir
Комплект компакт -дисків
Експорт PICO_SDK_PATH = ../../PICO-SDK
cmake ..
робити
__Placeholder_7__

Потім просто скопіюйте & nbsp; __. Uf2 __ & nbsp; __ ploadholder_20__ на диск.

__Placeholder_8__cp 0x05_float.uf2 /томи /rpi-rp2
__Placeholder_9__

Тоді нам потрібно знайти USB -накопичувач, щоб ви могли зробити наступне.

__Placeholder_10__ls /__ ploadholder_25 __ /tty.
__Placeholder_11__

Натисніть вкладку, щоб знайти накопичувач __placeholder_30__, тоді в моєму випадку я буду використовувати & nbsp; __ екран __ & nbsp; для підключення.

__Placeholder_12__screen /__placeholder_26__/tty.usbmodem00000000001
__Placeholder_13__

Ви повинні побачити AN & nbsp; _40.5_ & nbsp; надруковано щосекунди.

__Placeholder_14__40.500000
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
__Placeholder_15__

На нашому наступному уроці ми будемо налагодити.