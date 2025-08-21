## part 14 - хакерський булевий примітивний тип даних

Для повного змісту всіх уроків, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює. https://github.com/mytechnotalent/hacking\_c-\_arm64

Сьогодні ми зламаємо булеву з останнього уроку.

Давайте розберемо radare2 в режимі запису.

<pre spellcheck="false">radare2 -w ./0x04_asm64_boolean_primitive_datatype
</pre>

Давайте автоматично проаналізуємо.

<pre spellcheck="false">aaa
</pre>

Прагнути до головного.

<pre spellcheck="false">s main
</pre>

Переглянути демонстрацію.

<pre spellcheck="false">v
</pre>

Давайте повернемося до подання терміналу.

<pre spellcheck="false">q
</pre>

Все, що нам потрібно зробити, - це записувати на _0x00000009bc_ та вказати _0x0_.

<pre spellcheck="false">[0x000009b4]&gt; wa movz w0, 0x0 @ 0x00000009bc
Written 4 byte(s) (movz w0, 0x0) = wx 00008052
</pre>

<pre spellcheck="false">[0x000009b4]&gt;
</pre>

Давайте кинемо і запустимо новий двійковий з терміналу.

<pre spellcheck="false">[0x000009b4]&gt; q
kali@kali:~/Documents/0x04_asm64_boolean_primitive_datatype$ ./0x04_asm64_boolean_primitive_datatype
</pre>

<pre spellcheck="false">0
</pre>

Як ви бачите, ми успішно і назавжди зламали двійкову! Що спочатку було _true_ або _1_, тепер _false _or _0_.

На нашому наступному уроці ми будемо працювати з цілим примітивним типом даних.