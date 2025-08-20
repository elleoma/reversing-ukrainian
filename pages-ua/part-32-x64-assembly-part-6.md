## part 32 - x64 Асамблея \ [Частина 6 \]

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте розглянемо наш код.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553248751760.jpg"/></div>

Компілювати ...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553248766003.jpg"/></div>

Налагодження ...

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553248783477.jpg"/></div>

Давайте оцінимо, що знаходиться всередині адреси пам'яті 0x6000d8.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1553248844375.jpg"/></div>

Як ми бачимо, "__Hello World__" з персонажем повернення потім буде переведено в наш реєстр __RSI__.

Наступного тижня ми розглянемо це трохи ближче.