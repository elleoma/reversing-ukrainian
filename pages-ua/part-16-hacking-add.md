## part 16 - Hacking ADD

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте знову розглянемо наш приклад ADD нижче:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520148983155.jpg"/></div>

Давайте налагоджуємо:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520143258587.jpg"/></div>

Ми бачимо, що цінність __67__ десятковий переміщення переміщується в __R1__ нижче:

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520171779364.jpg"/></div>

Давайте hack! Давайте встановити __R1 = 66__!

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520211664200.jpg"/></div>

Тепер ми бачимо, що ми зламали програму, тому коли вона додає значення, вона матиме інший вихід. Якщо ви пам’ятаєте до останньої лекції, __r0 = 120__. Тут ми бачимо, що ми зламали r1 and тепер значення __r0__ - __119__!

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1520211540477.jpg"/></div>

Це сила розуміння складання. Однак це дуже простий приклад з кожною новою серією, як я заявив, що ми створимо програму, налагодження and hack.

Ця комбінація інструкцій допоможе вам отримати досвід роботи, коли навчитися абсолютному контролю над додатком and у випадку з зворотним інженерією зловмисного програмного забезпечення дає можливість змусити двійкову робити саме те, що ви хочете!

Наступного тижня ми зануримося в додавання.