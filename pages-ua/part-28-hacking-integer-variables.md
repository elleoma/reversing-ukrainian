## part 28 - Hacking цілі змінні

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте розглянемо наш код.&nbsp;&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1519988583160.jpg"/></div>

Давайте hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1519988510636.jpg"/></div>

Давайте знову подивимось всередину місця пам'яті __0x10730__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1519988543593.jpg"/></div>

Як ми чітко бачимо, що ціле значення __7772 з’являється and, коли ми продовжуємо це перегукується з терміналом значення __777__, що відповідає нашій функції C ++ __cout__.

Давайте hack значення всередині __0x10730__ and встановить значення __6666__ and, а потім переглядати значення всередині __0x10730__ and.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1519988571825.jpg"/></div>

Успіх! &nbsp;as ми можемо побачити

На наступному тижні ми зануримось у змінні поплавця.