---
{}
---

__Placeholder_16__ Частина 8 - __placeholder_23__________________________

Сьогодні ми будемо працювати з типом даних __placeholder_24__, який є не що інше, як цілі цифри. Вони можуть бути підписані __placeholder_18__ також без підписання.

Давайте попрацюємо з простим прикладом. __0x04 \ _int.c__ наступним чином.

__Placeholder_0 __#включити & lt; stdio__placeholder_28 __ & gt;
__Placeholder_17__ включити "pico/stdlib__placeholder_29__"

__Placeholder_25__ main () & nbsp;
{
& nbsp; stdio_init_all ();

& nbsp; в той час як (1) & nbsp;
& nbsp; {
& nbsp; & nbsp; __Placeholder_26__ x = 40; & nbsp;

& nbsp; & nbsp; __Placeholder_36 __ ("%d \ n", x); & nbsp;

& nbsp; & nbsp; Sleep_ms (1000);
& nbsp; }

& nbsp; повернення 0;
}
__Placeholder_1__

Тут ми просто маємо нашу стандартну функцію IO, а потім наша нескінченна петля. Ми просто присвоюємо _40_ на тип даних __placeholder_27__ _x_ __placeholder_32__ надрукувати його за допомогою модифікатора формату _%d_ __placeholder_33__ сон для _1_ секунди.

Давайте зробимо новий DIR & nbsp; __ 0x04 \ _int __ & nbsp; __ ploadholder_34__ __placeholder_22__ Наші & nbsp; __ cmakelists.txt __ & nbsp; __ ploadholder_19__ в ньому.

__Placeholder_2__cmake_minimum_required (версія 3.13)

включити (pico_sdk_import.cmake)

Проект (test_project c cxx asm)
set (cmake_c_standard 11) & nbsp;
set (cmake_cxx_standard 17) & nbsp;
pico_sdk_init ()

add_executable (0x04_int
& nbsp; 0x04_int__placeholder_37__
)

pico_enable_stdio_usb (0x04_int 1)

pico_add_extra_outputs (0x04_int)

Target_Link_Libraries (0x04_int pico_stdlib)
__Placeholder_3__

Далі нам потрібно скопіювати & nbsp; __ pico \ _sdk \ _import.cmake __ & nbsp; __ ploadholder_20__ із зовнішньої папки в & nbsp; __ pico-sdk __ & nbsp; інсталяція до & nbsp; __ 0x04 \ _int __ & nbsp;

__Placeholder_4__cp ../pico-sdk/external/pico_sdk_import.cmake.
__Placeholder_5__

Нарешті ми готові до будівництва.

__Placeholder_6__mkdir
Комплект компакт -дисків
Експорт PICO_SDK_PATH = ../../PICO-SDK
cmake ..
робити
__Placeholder_7__

Потім просто скопіюйте & nbsp; __. Uf2 __ & nbsp; __ ploadholder_21__ на диск.

__Placeholder_8__cp 0x04_int.uf2 /томи /rpi-rp2
__Placeholder_9__

Тоді нам потрібно знайти USB -накопичувач, щоб ви могли зробити наступне.

__Placeholder_10__ls /__ ploadholder_30 __ /tty.
__Placeholder_11__

Натисніть вкладку, щоб знайти накопичувач __placeholder_35__, тоді в моєму випадку я буду використовувати & nbsp; __ екран __ & nbsp; для підключення.

__Placeholder_12__screen /__placeholder_31__/tty.usbmodem00000000001
__Placeholder_13__

Ви повинні бачити, як _40_ надрукується щосекунди.

__Placeholder_14__40
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
__Placeholder_15__

На нашому наступному уроці ми будемо налагодити.