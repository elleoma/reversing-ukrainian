---
{}
---

__Placeholder_16__ Частина 14 - Подвійний

Сьогодні ми збираємось обробляти подвійний тип даних. Як ми обговорювали, у Піко не існує коопроцесор, який би обробляв числа з плаваючою комою, оскільки це обробляється через ряд функціональних можливостей за допомогою програмного забезпечення в API. Це те ж саме з подвійною точністю.

Давайте попрацюємо з простим прикладом. & Nbsp; __ 0x06 \ _double.c __ & nbsp; наступним чином.

__Placeholder_0 __#включити & lt; stdio__placeholder_23 __ & gt;
__Placeholder_17__ включити "pico/stdlib__placeholder_24__"

__Placeholder_222__ main () & nbsp;
{
& nbsp; stdio_init_all ();

& nbsp; в той час як (1) & nbsp;
& nbsp; {
& nbsp; & nbsp; подвійний x = 40,5;

& nbsp; & nbsp; __Placeholder_31 __ ("%f \ n", x); & nbsp;

& nbsp; & nbsp; Sleep_ms (1000);
& nbsp; }

& nbsp; повернення 0;
}
__Placeholder_1__

Дуже просто ми призначаємо поплавок & nbsp; _40.5_ & nbsp; в & nbsp; _x_ & nbsp; __ ploadholder_27__ надрукувати його за допомогою модифікатора & nbsp; _%f & nbsp; _format __placeholder_28__, а потім спите для & nbsp; _1_ & nbsp;

Давайте зробимо новий dir & nbsp; __ 0x06 \ _double __ & nbsp; __ ploadholder_29 р.

__Placeholder_2__cmake_minimum_required (версія 3.13)

включити (pico_sdk_import.cmake)

Проект (test_project c cxx asm)
set (cmake_c_standard 11) & nbsp;
set (cmake_cxx_standard 17) & nbsp;
pico_sdk_init ()

add_executable (0x06_double
& nbsp; 0x06_double__placeholder_32__
)

pico_enable_stdio_usb (0x06_double 1)

pico_add_extra_outputs (0x056_double)

Target_Link_Libraries (0x06_double pico_stdlib)
__Placeholder_3__

Далі нам потрібно скопіювати & nbsp; __ pico \ _sdk \ _import.cmake __ & nbsp; __ ploadholder_19__ із зовнішньої папки у & nbsp; __ pico-sdk __ & nbsp;

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

__Placeholder_8__cp 0x06_double.uf2 /томи /rpi-rp2
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