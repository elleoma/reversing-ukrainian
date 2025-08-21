## part 25 - хакерські булеві змінні

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте переглянемо наш код.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520191957701.jpg"/></div>

Давайте хакемо!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520210981189.jpg"/></div>

Давайте розірвемося в Main, Run and Disas на додаток до наступних разів.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520146846926.jpg"/></div>

Ми бачимо, що __0__ або __false__ переміщується в __R3__ на main+12.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520218746699.jpg"/></div>

Дуже просто ми встановлюємо __r3__ на __1__ або __true__ і продовжуємо виконання, на яке ми помічаємо, що булева змінна __ishacked__ зараз __true__.

Це прості люди! &nbsp;

Наступного тижня ми зануримось у цілі змінні.