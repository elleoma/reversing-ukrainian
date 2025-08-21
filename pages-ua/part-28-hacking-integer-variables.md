## part 28 - зламати цілі змінні

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте розглянемо наш код.&nbsp;&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1519988583160.jpg"/></div>

Давайте хакемо!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1519988510636.jpg"/></div>

Давайте знову подивимось всередину місця пам'яті __0x10730__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1519988543593.jpg"/></div>

Як ми чітко бачимо, що ціле значення __777__ з’являється, і коли ми продовжуємо, воно переживає до терміналу значення __777__, що відповідає нашій функції C ++ __cout__.

Давайте зламаємо значення всередині __0x10730__ і встановимо значення __666____, а потім переглядати значення всередині __0x10730__ і продовжимо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1519988571825.jpg"/></div>

Успіх! &nbsp;as ми можемо побачити, що ми зламали цінність __666____, коли ми продовжуємо, ми бачимо, що це перегукується з stdout.

На наступному тижні ми зануримось у змінні поплавця.