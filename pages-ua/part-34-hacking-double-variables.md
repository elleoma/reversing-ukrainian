---
{}
---

__Placeholder_30__ Частина 34 - Зламати подвійні змінні

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює. & NBSP; __ Ploadholder_29__

Давайте розглянемо наш код.

__Placeholder_0__int main (void) {

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; подвійний mynumber = 1337,77;

& nbsp;

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; std :: cout & lt; & lt; mynumber & lt; & lt; std :: endl;

& nbsp;

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; повернення 0;

}
__Placeholder_1__

__Placeholder_2____placeholder_3____placeholder_4__

Давайте налагоджуємо!

__Placeholder_5____Placeholder_6____Placeholder_7__

Встановимо точку перерви в __ -мейн+24__ __placeholder_35__ Продовжуйте.

__Placeholder_8____Placeholder_9____Placeholder_10__

Ми бачимо __Strd __placeholder_31__, \ [__ ploadholder_33__, \#-12 \] __ __placeholder_36__ Ми повинні повністю зрозуміти, що це означає, що ми зберігаємо цінність у зміщенні __- 12__ з реєстру __r11__ в __r2 __. & Nbsp;

__Placeholder_11____Placeholder_12____Placeholder_13__________________

VOILA! & NBSP; ми бачимо __1337.77__ у цьому зміщеному місці __placeholder_32__ спеціально зберігається в __0x7efff230__ в пам'яті.

__Placeholder_14____Placeholder_15____Placeholder_16__

Давайте поступаємо двічі, який виконує __VLDR D0, \ [__ Ploadholder_34__, \#-12 \] __ Як ми розуміємо, що __1337.77__ тепер буде завантажений у подвійну точну математичну копроцесор __d0 __register. &

__Placeholder_17____Placeholder_18____Placeholder_19__

Давайте зламаємо реєстр __D0__!

__Placeholder_20____Placeholder_21____Placeholder_22______

Тепер давайте переглянемо значення всередині __d0__.

__Placeholder_23____placeholder_24____placeholder_25__

Продовжуємо.

__Placeholder_26____Placeholder_27____Placeholder_28__

Успішно зламано!

Наступного тижня ми занурюємось у оператор Sizeof.