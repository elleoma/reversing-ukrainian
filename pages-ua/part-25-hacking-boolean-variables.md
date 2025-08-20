## part 25 - Hacking boolean змінні

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте переглянемо наш код.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520191957701.jpg"/></div>

Давайте hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520210981189.jpg"/></div>

Давайте розірвемося на main, запускаємо диски and на додаток до кроку в чотири рази.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520146846926.jpg"/></div>

Ми бачимо, що __0__ or __false__ переміщується в __r3__ на main+12.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520218746699.jpg"/></div>

Дуже просто ми встановили __r3__ на __1__ or __true__ and продовжуйте виконання, до якого ми помічаємо, що булева змінна __ishacked__ зараз __true__.

Це прості люди! &nbsp;

Наступного тижня ми зануримось у цілі змінні.