## part 17 - хакерський поплавковий примітивний тип даних

Для повного змісту всіх уроків, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює. https://github.com/mytechnotalent/hacking\_c-\_arm64

Сьогодні ми зламаємо поплавок з останнього уроку.

Перший оновіть наш вихідний код radare2.

<pre spellcheck="false">cd radare2
git pull
sys/user.sh
</pre>

Якщо ви не дотримувались інструкцій раніше, вам доведеться створити radare2 з джерела, щоб це працювало, коли вони рідко оновлюють випуски.

https://github.com/radareorg/radare2

Якщо у вас немає репо, клонуйте його та дотримуйтесь вказівок вище.

Давайте розберемо radare2 в режимі запису.

<pre spellcheck="false">radare2 -w ./0x05_asm64_float_primitive_datatype
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

Нам тут потрібно зламати дві інструкції. Давайте розглянемо дві дуже конкретні інструкції.

<pre spellcheck="false">movz w0, 0x999a
movk w0, 0x4121, lsl 16
</pre>

Згадайте з минулого тижня, що в кінцевому підсумку W0 збирається утримувати _0x4121999a_, оскільки _lsl_ переміщує укуси у зворотному порядку.

В даний час це призведе до плавання _10.1_, як ми бачили на попередніх уроках. Важливо, щоб ви розуміли, що в числах з плаваючою комою є _mantissa_, що в нашому випадку є _10_ і _exponent_, що є _1_, до якого вони розділені a_ ._, що їх пов'язує разом.

Тому, щоб отримати _10.2_, нам потрібно буде записати збірку та оновити ці інструкції.

<pre spellcheck="false">[0x000009b4]&gt; wa movz w0, 0x3333 @0x000009bc
[0x000009b4]&gt; wa movk w0, 0x4123, lsl 16 @0x000009c0
q

</pre>

Тепер запустіть двійкову!

<pre spellcheck="false">kali@kali:~/Documents/0x05_float_primitive_datatype$ ./0x05_float_primitive_datatype
10.2
</pre>

Я хочу, щоб ви уважно ознайомилися з деякими прикладами, які я зібрав для вас, щоб ви могли зрозуміти, як різні значення призводять до різних результатів. Майте на увазі, що ці результати знаходяться на активному сеансі налагодження, тому адреси будуть різними, тому ваш ASLR матиме різні значення.

<pre spellcheck="false">[0x555e6c29c4]&gt; dr w0 = 0x4122999a
0x4121999a -&gt;0x4122999a
[0x555e6c29c4]&gt; dc
hit breakpoint at: 0x555e6c29c8
[0x555e6c29c8]&gt; dc
10.1625
(238252) Process exited with status=0x0

[0x556215e9c4]&gt; dr w0 = 0x41235555
0x4121999a -&gt;0x41235555
[0x556215e9c4]&gt; dc
hit breakpoint at: 0x556215e9c8
[0x556215e9c8]&gt; dc
10.2083
(238258) Process exited with status=0x0

[0x558216c9c4]&gt; dr w0 = 0x4123599a
0x4121999a -&gt;0x4123599a
[0x558216c9c4]&gt; dc
hit breakpoint at: 0x558216c9c8
[0x558216c9c8]&gt; dc
10.2094
(238257) Process exited with status=0x0

[0x55868a79c4]&gt; dr w0 = 0x4123999a
0x4121999a -&gt;0x4123999a
[0x55868a79c4]&gt; dc
hit breakpoint at: 0x55868a79c8
[0x55868a79c8]&gt; dc
10.225
(238253) Process exited with status=0x0

[0x55826479c4]&gt; dr w0 = 0x41233333
0x4121999a -&gt;0x41233333
[0x55826479c4]&gt; dc
hit breakpoint at: 0x55826479c8
[0x55826479c8]&gt; dc
10.2
(238259) Process exited with status=0x0

[0x55716ab9c4]&gt; dr w0 = 0x4125999a
0x4121999a -&gt;0x4125999a
[0x55716ab9c4]&gt; dc
hit breakpoint at: 0x55716ab9c8
[0x55716ab9c8]&gt; dc
10.35
(238250) Process exited with status=0x0

[0x55880169c4]&gt; dr w0 = 0x412f999f
0x4121999a -&gt;0x412f999f
[0x55880169c4]&gt; dc
hit breakpoint at: 0x55880169c8
[0x55880169c8]&gt; dc
10.975
(238245) Process exited with status=0x0

[0x559130d9c4]&gt; dr w0 = 0x412ff99e
0x4121999a -&gt;0x412ff99e
[0x559130d9c4]&gt; dc
hit breakpoint at: 0x559130d9c8
[0x559130d9c8]&gt; dc
10.9984
(238246) Process exited with status=0x0

[0x557b1b39c4]&gt; dr w0 = 0x412fff9e
0x4121999a -&gt;0x412fff9e
[0x557b1b39c4]&gt; dc
hit breakpoint at: 0x557b1b39c8
[0x557b1b39c8]&gt; dc
10.9999
(238247) Process exited with status=0x0

[0x55931439c4]&gt; dr w0 = 0x412ffffe
0x4121999a -&gt;0x412ffffe
[0x55931439c4]&gt; dc
hit breakpoint at: 0x55931439c8
[0x55931439c8]&gt; dc
11
(238248) Process exited with status=0x0
</pre>

Ви можете почати бачити шаблони тут. Знайдіть час і фактично спробуйте їх, щоб ви краще зрозуміли, як ці цінності в кінцевому підсумку потрапляють до реєстру S0!

Наступний урок ми обговоримо парні.