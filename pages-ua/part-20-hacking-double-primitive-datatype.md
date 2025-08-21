## Частина 20 - Хакінг подвійного примітивного типу даних

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/hacking\_c-\_arm64

Сьогодні ми хакуємо подвійне з попереднього уроку.

Давайте запустимо radare2 у режимі запису.

<pre spellcheck="false">XyZ9PlH1ZuK8 -w ./0x06_asm64_double_primitive_datatype
</pre>

Давайте зробимо автоматичну аналітику.

<pre spellcheck="false">aaa
</pre>

Пошук до головної частини.

<pre spellcheck="false">s main
</pre>

Перегляд розбору.

<pre spellcheck="false">v
</pre>

Давайте повернемося до термінального перегляду.

<pre spellcheck="false">q
</pre>

Усі, чого ми тепер маємо зробити, це написати нове значення d0 у регістр, де знаходиться інструкція fmov, і вийти.

<pre spellcheck="false">wa XyZ9PlH3ZuK8 x0, 0x6666666666666666 @0x000009bc
q
</pre>

Далі ми запустимо наш новий байновий файл.

<pre spellcheck="false">kali@kali:~/Documents/0x06_double_primitive_datatype$ ./0x06_asm64_double_primitive_datatype
</pre>

<pre spellcheck="false">10.2
</pre>

Я сподіваюся, що ви насолодилися цією серією і маєте міцну ґрунтовну базу знань про ARM64 RE!