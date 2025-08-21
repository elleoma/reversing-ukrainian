## part 19 - налагодження подвійного примітивного типу даних

Для повного змісту всіх уроків, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює. https://github.com/mytechnotalent/hacking\_c-\_arm64

Сьогодні ми збираємось налагодити наш дуже простий подвійний примітивний тип даних.

Для початку давайте відкриємо наш двійковий у Radare2.

<pre spellcheck="false">radare2 ./0x06_asm64_double_primitive_datatype
</pre>

Давайте скористаємось функцією автоматичного аналізу Radare2.

<pre spellcheck="false">aaa
</pre>

Наступне, що ми хочемо зробити логічно, - це розпалювати програму в режимі налагодження, щоб вона відображала сирий машинний код від диска до запущеного процесу.

<pre spellcheck="false">ood
</pre>

Тепер, коли у нас є екземпляр запуску, ми можемо прагнути до основної точки входу двійкового.

<pre spellcheck="false">s main
</pre>

Давайте пройдемо початкову експертизу, зробивши наступне.

<pre spellcheck="false">v
</pre>

When dealing with double floating-point numbers in ARM64 we have to understand that we want to locate where the&nbsp;_fmov_&nbsp;instruction occurs where we take a value from our&nbsp;_w0_&nbsp;register and move it into the floating Point&nbsp;_d0_&nbsp;register. Ось де відбувається вся магія! Це так само, як наші номери з плаваючою комою, які мають справу з _S0_.

Давайте визначимо точку розриву прямо під te&nbsp;_fmov_&nbsp;instruction. Пам'ятайте з ASLR, ваші адреси будуть різними, ніж цей приклад.

<pre spellcheck="false">[0x556bf809b4]&gt; db 0x556bf809c4
[0x556bf809b4]&gt; dc
hit breakpoint at: 0x556bf809c4
[0x556bf809c4]&gt; dr w0
0x33333333
</pre>

Ми переміщуємо Un&nbsp;_w0_&nbsp;register в _d0_, тому ми повинні змінити ці значення в _d0_&nbsp;, що відрізняється від нашого поплавця. Ми вивчимо це на наступному уроці.

Давайте продовжувати показувати нашу цінність.

<pre spellcheck="false">[0x556bf809c4]&gt; dc
10.1
(39979) Process exited with status=0x0
[0x7fa37da0fc]&gt;
</pre>

На нашому наступному уроці ми зламаємо цю цінність!