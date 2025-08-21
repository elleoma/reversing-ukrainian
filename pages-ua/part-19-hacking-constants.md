## part 19 - зламати константи

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте розглянемо наш оригінальний код.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520195148562.jpg"/></div>

Давайте хакемо!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520144504108.jpg"/></div>

Як ми можемо побачити значення в адресі пам'яті __0x10730 __, рівна __2017 __. &nbsp;LET's зміна цього значення в пам'яті на __1981 __. &nbsp;let's продовження та спостереження за значенням __1981 __!

Давайте зламаємо другий спосіб! &nbsp;RE запускайте програму і встановимо точку перерви на main+28 і продовжимо до точки перерви.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520146785758.jpg"/></div>

Давайте продовжимо, і ми побачимо, що значення в __R1__ становить __2017 __. &nbsp;LET зміна значення в __R1__ на __1981 __. &nbsp;WE продовжуємо і дивимось програму успішно зламаною до __1981 __!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520148769675.jpg"/></div>

Наступного тижня ми зануримося в змінні символів.