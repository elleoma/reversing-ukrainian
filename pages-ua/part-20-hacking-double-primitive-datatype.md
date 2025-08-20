## part 20 - Hacking подвійний примітивний тип даних

Для повного змісту всіх уроків, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює. https://github.com/mytechnotalent/hacking\_c-\_arm64

Сьогодні ми hack подвійний з останнього уроку.

Давайте розберемо radare2 в режимі запису.

<pre spellcheck="false">radare2 -w ./0x06_asm64_double_primitive_datatype
</pre>

Давайте автоматично проаналізуємо.

<pre spellcheck="false">aaa
</pre>

Прагнути до main.

<pre spellcheck="false">s main
</pre>

Переглянути disassembly.

<pre spellcheck="false">v
</pre>

Давайте повернемося до подання терміналу.

<pre spellcheck="false">q
</pre>

Все, що нам потрібно зробити зараз, - це записати нове значення D0 в реєстр, де інструкція FMOV - and.

<pre spellcheck="false">wa mov x0, 0x6666666666666666 @0x000009bc
q
</pre>

Тоді ми керуємо нашим новим двійковим.

<pre spellcheck="false">kali@kali:~/Documents/0x06_double_primitive_datatype$ ./0x06_asm64_double_primitive_datatype
</pre>

<pre spellcheck="false">10.2
</pre>

Я сподіваюся, що вам сподобалася ця серія and, добре сприймайте ARM64 re!