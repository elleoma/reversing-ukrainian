## Частина 20 - Хакінг подвійного примітивного типу даних

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/hacking\_c-\_arm64

Сьогодні ми хакуємо подвійне з попереднього уроку.

Давайте запустимо radare2 у режимі запису.

<pre spellcheck="false">radare2 -w./0x06_asm64_double_primitive_datatype
</pre>

Давайте зробимо автоматичний аналіз.

<pre spellcheck="false">aaa
</pre>

Перейдіть до головної частини.

<pre spellcheck="false">s main
</pre>

Перегляньте розборку.

<pre spellcheck="false">v
</pre>

Давайте повернемося до термінального перегляду.

<pre spellcheck="false">q
</pre>

Усі, чого ми зараз маємо зробити, це написати нове значення d0 у регістр, де знаходиться інструкція fmov, і вийти.

<pre spellcheck="false">wa mov x0, 0x6666666666666666 @0x000009bc
q
</pre>

Далі ми запустимо наш новий байнері.

<pre spellcheck="false">kali@kali:~/Documents/0x06_double_primitive_datatype$./0x06_asm64_double_primitive_datatype
</pre>

<pre spellcheck="false">10.2
</pre>

Я сподіваюся, ви насолодилися цією серією і маєте міцну ґрунтовну базу знань ARM64 RE!