## part 16 - хакерство Hello World

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте розглянемо наш код з двох тижнів тому.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520191330889.jpg"/></div>

Давайте ще раз налагодити.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520233045514.jpg"/></div>

Давайте ще раз вивчимо вміст рядка за адресою пам'яті __0x10750__ і продовжимо виконання програми.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520200292099.jpg"/></div>

Як ви бачите, він тримає рядок "__Hello World! __", і коли ми продовжуємо через нього Ехо назад до терміналу як такого.

Давайте зламаємо! &nbsp;LET тепер перезапишіть значення всередині адреси пам'яті з рядком, "__HAcked World! __" і продовжуємо виконання.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520148428152.jpg"/></div>

Woohoo! &nbsp;ourther first hack! &nbsp;as ви можете побачити, як ви розумієте, що ви маєте абсолютний контроль над усім двійковим, незалежно від того, в якій мові написано. &nbsp;in Цей дуже простий приклад, який ми змогли зламати значення в межах пам'яті __0x10750__, до якого виконали, що - до " клем або стандартний вихід.

Давайте знову запустимо двійковий і зробимо розбирання.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520230658310.jpg"/></div>

Давайте зараз зробимо ту саму процедуру, проте давайте __si__ 3x і вивчимо рядок всередині __r1 __. &nbsp;we бачимо, що він містить: "__hello World! __", як це було успішно __ldr __ (навантаження з пам'яті в реєстр) в __main+12__.

Тепер встановити r1 на "__hacked World! __" і продовжимо виконання.&nbsp;as ви можете побачити, що ми зараз зламали його, що виходить з реєстру, а не в memory.&nbsp; Ви можете чітко почати бачити ряд способів зламати що завгодно, і ось простий приклад двох таких шляхів.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520231520333.jpg"/></div>

Зворотна інженерія - це все про розуміння того, як програма виконує та викрадає потік виконання та зміну значень відповідно до нашої мети! &nbsp;today ви зробили свій перший крок у цю дивовижну подорож!

Наступного тижня ми зануримося в константи.