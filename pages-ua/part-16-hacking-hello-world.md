## part 16 - Hacking Hello World

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте розглянемо наш код з двох тижнів тому.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520191330889.jpg"/></div>

Давайте ще раз налагодити.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520233045514.jpg"/></div>

Давайте ще раз вивчимо вміст рядка за адресою пам'яті __0x10750__ and продовжуйте виконання програми.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520200292099.jpg"/></div>

Як ви бачите, він має "__Hello World! __" String and, коли ми продовжуємо через нього Ехо назад до терміналу як такого.

Давайте hack! &nbsp;LET зараз перепишіть значення всередині адреси пам'яті зі рядком, "__HACKED World! __" and Продовжуйте виконання.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520148428152.jpg"/></div>

Woohoo! &nbsp;our Перший hack! &nbsp;as ви можете бачити, як ви розумієте, що ви маєте абсолютний контроль над усім бінарним, незалежно від того, в якій мові він написаний. nbspin Цей дуже простий приклад ми змогли до hack. виконано, що це перегукувалося: "__ -хакерський світ! __" до стандартного випуску терміналу or.

Давайте знову запустимо двійковий and, зробимо disassembly.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520230658310.jpg"/></div>

Давайте зараз зробимо ту саму процедуру, проте давайте __si__ 3x and вивчити рядок всередині __r1 __. nbspwe бачимо, що він містить: "__hello World! __", як це було успішно __ldr __ (навантаження з пам'яті в реєстр) на __main+12__.

Тепер встановимо R1 на "__hacked World! __" and продовжити виконання.&nbsp;as ви можете побачити такі шляхи.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520231520333.jpg"/></div>

Зворотна інженерія - це все про розуміння того, як програма виконує and викрадення потоку виконання and Зміна значень відповідно до нашої мети! nbspTODAY Ви зробили свій перший крок у цю дивовижну подорож!

Наступного тижня ми зануримося в константи.