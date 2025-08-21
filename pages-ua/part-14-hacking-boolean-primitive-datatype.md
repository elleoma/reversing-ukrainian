Частина 14 - Хакінг примітивного типу даних Boolean

Для повного змісту змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть обговорені. https://github.com/mytechnotalent/hacking\_c-\_arm64

Сьогодні ми хакуємо Boolean із попереднього уроку.

Давайте запустимо radare2 у режимі запису.

<pre spellcheck="false">XyZ9PlH1ZuK8 -w ./0x04_asm64_boolean_primitive_datatype
</pre>

Давайте зробимо аналіз автоматично.

<pre spellcheck="false">aaa
</pre>

Пошук головної частини.

<pre spellcheck="false">s main
</pre>

Переглянути розборку.

<pre spellcheck="false">v
</pre>

Давайте повернемося до термінального перегляду.

<pre spellcheck="false">q
</pre>

Усі, чого нам потрібно зробити, це написати збірку до _0x00000009bc_ і вказати _0x0_.

<pre spellcheck="false">[0x000009b4]&gt; wa movz w0, 0x0 @ 0x00000009bc
Written 4 byte(s) (movz w0, 0x0) = wx 00008052
</pre>

<pre spellcheck="false">[0x000009b4]&gt;
</pre>

Давайте вийдемо і запустимо новий бінарний файл із терміналу.

<pre spellcheck="false">[0x000009b4]&gt; q
kali@kali:~/Documents/0x04_asm64_boolean_primitive_datatype$ ./0x04_asm64_boolean_primitive_datatype
</pre>

<pre spellcheck="false">0
</pre>

Як бачите, ми успішно і постійно хакнули бінарний файл! Що було раніше _true_ або _1_ тепер _false_ або _0_.

У наступному урокі ми працюватимемо з примітивним типом даних integer.