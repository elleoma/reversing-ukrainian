## part 19 - Hacking константи

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте розглянемо наш оригінальний код.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520195148562.jpg"/></div>

Давайте hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520144504108.jpg"/></div>

Як ми можемо побачити значення в адресі пам'яті __0x10730 __, рівна __2017 __. &nbsp;LET's зміна цього значення в пам'яті на __1981 __. &nbsp;let's продовжує and. hack!

Давайте hack другий спосіб! &nbsp;RE-Start Програма and Встановіть breakpoint на main+28 and до breakpoint.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520146785758.jpg"/></div>

Давайте продовжимо and, ми бачимо, що значення в __r1__ є __2017 __. &nbsp;let зміна значення в __r1__ на __1981 __. &nbsp;we продовжуйте and. __1981 __! &nbsp;&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520148769675.jpg"/></div>

Наступного тижня ми зануримося в змінні символів.