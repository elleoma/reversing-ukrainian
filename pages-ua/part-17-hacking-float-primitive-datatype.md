Частина 17 - Хакінг примітивної типової даних типу float

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/hacking\_c-\_arm64

Сьогодні ми хакуємо float з попереднього уроку.

Спочатку оновіть наш radare2 джерельний код.

<pre spellcheck="false">cd radare2
git pull
sys/user.sh
</pre>

Якщо ви раніше не дотримувалися інструкцій, необхідно побудувати radare2 з джерела, оскільки вони рідко оновлюють випуски.

https://github.com/radareorg/radare2

Якщо ви не маєте репозиторію, клоніруйте його і дотримуйтесь інструкцій вище.

Давайте запустимо radare2 у режимі запису.

<pre spellcheck="false">radare2 -w./0x05_asm64_float_primitive_datatype
</pre>

Давайте зробимо аналіз автоматично.

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

Нам потрібно змінити дві інструкції. Давайте розглянемо дві дуже спеціальні інструкції.

<pre spellcheck="false">movz w0, 0x999a
movk w0, 0x4121, lsl 16
</pre>

Пам'ятайте з попереднього тижня, що в кінцевому підсумку w0 буде зберігати _0x4121999a_ як _lsl_ переміщає біти в зворотньому порядку байтів.

Зараз це буде давати float _10.1_ як ми бачили раніше в попередніх уроках. Важливо розуміти, що в чиселах з плаваючою комою є _мантисса_ яка в нашому випадку _10_ і _висота_ яка _1_ до якої вони розділені._ яка поєднує їх разом.

Отже, щоб отримати _10.2_ нам потрібно буде написати збірку і оновити ці інструкції.

<pre spellcheck="false">[0x000009b4]&gt; wa movz w0, 0x3333 @0x000009bc
[0x000009b4]&gt; wa movk w0, 0x4123, lsl 16 @0x000009c0
q

</pre>

Тепер запустіть бінарник!

<pre spellcheck="false">kali@kali:~/Documents/0x05_float_primitive_datatype$./0x05_float_primitive_datatype
10.2
</pre>

Я бажаю, щоб ви взяли близько на погляд деякі приклади, які я створив для вас, щоб ви могли зрозуміти, як різні значення призводять до різних результатів. Увага! Результати будуть різними, оскільки ці результати будуть активним сесією відлагодження, тому адреси будуть різними, тому ваш ASLR буде мати різні значення.

<pre spellcheck="false">[0x555e6c29c4]&gt; dr w0 = 0x4122999a 0x4121999a -&gt;0x4122999a
[0x555e6c29c4]&gt; dc
hit breakpoint at: 0x555e6c29c8
[0x555e6c29c8]&gt; dc
10.1625
(238252) Process exited with status=0x0

[0x556215e9c4]&gt; dr w0 = 0x41235555 0x4121999a -&gt;0x41235555
[0x556215e9c4]&gt; dc
hit breakpoint at: 0x556215e9c8
[0x556215e9c8]&gt; dc
10.2083
(238258) Process exited with status=0x0

[0x558216c9c4]&gt; dr w0 = 0x4123599a 0x4121999a -&gt;0x4123599a
[0x558216c9c4]&gt; dc
hit breakpoint at: 0x558216c9c8
[0x558216c9c8]&gt; dc
10.2094
(238257) Process exited with status=0x0

[0x55868a79c4]&gt; dr w0 = 0x4123999a 0x4121999a -&gt;0x4123999a
[0x55868a79c4]&gt; dc
hit breakpoint at: 0x55868a79c8
[0x55868a79c8]&gt; dc
10.225
(238253) Process exited with status=0x0

[0x55826479c4]&gt; dr w0 = 0x41233333 0x4121999a -&gt;0x41233333
[0x55826479c4]&gt; dc
hit breakpoint at: 0x55826479c8
[0x55826479c8]&gt; dc
10.2
(238259) Process exited with status=0x0

[0x55716ab9c4]&gt; dr w0 = 0x4125999a 0x4121999a -&gt;0x4125999a
[0x55716ab9c4]&gt; dc
hit breakpoint at: 0x55716ab9c8
[0x55716ab9c8]&gt; dc
10.35
(238250) Process exited with status=0x0

[0x55880169c4]&gt; dr w0 = 0x412f999f 0x4121999a -&gt;0x412f999f
[0x55880169c4]&gt; dc
hit breakpoint at: 0x55880169c8
[0x55880169c8]&gt; dc
10.975
(238245) Process exited with status=0x0

[0x559130d9c4]&gt; dr w0 = 0x412ff99e 0x4121999a -&gt;0x412ff99e
[0x559130d9c4]&gt; dc
hit breakpoint at: 0x559130d9c8
[0x559130d9c8]&gt; dc
10.9984
(238246) Process exited with status=0x0

[0x557b1b39c4]&gt; dr w0 = 0x412fff9e 0x4121999a -&gt;0x412fff9e
[0x557b1b39c4]&gt; dc
hit breakpoint at: 0x557b1b39c8
[0x557b1b39c8]&gt; dc
10.9999
(238247) Process exited with status=0x0

[0x55931439c4]&gt; dr w0 = 0x412ffffe 0x4121999a -&gt;0x412ffffe
[0x55931439c4]&gt; dc
hit breakpoint at: 0x55931439c8
[0x55931439c8]&gt; dc
11
(238248) Process exited with status=0x0
</pre>

Ви починаєте бачити шаблони тут. ВИДЕЛІТЬСЯ ПОВІДОМЛЕННЯ ІСТИННО ВИПРОБУВАТИ ЦІ ВИРОБИТИ, щоб краще зрозуміти, як ці значення в кінцевому підсумку потрапляють в регістр s0!

У наступному уроці ми обговоримо подвійні числа.