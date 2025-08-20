## PART 25 - Основи сектору завантаження \ [Частина 8 \]

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Сьогодні ми складемо всі шматки. Ми створимо нашу користувацьку ОС, яка не робить нічого, крім завантаження, встановить відео режиму and, тоді приймемо лише цифрові цифри в console. Це заключний підручник у цій міні-серії основ Boot Sector.

Давайте розглянемо наш код:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1549024795636.jpg"/></div>

Перше, що ми робимо, - це перейти до програмної області коду завантажувального сектору за адресою 0x7c00. Потім ми встановлюємо базу стека and Визначте область для нашого стека and встановіть базовий вказівник у вказівник стека.

Потім ми call Наша функція режиму відео, де ми встановимо 640x200 Greyscale console. We then call our get character input функція that will only allow digits 0 to 9 as you can see 0x30 is the hex ascii value for 0 and 0x39 is the hex ascii value of 9. If the user types anything else in the console literally nothing will enter into the console. Це абсолютний контроль, який ви маєте на складі.

Давайте складати and запускати:

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1549025055903.jpg"/></div>

Тоді ми бачимо QEMU console:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1549025085922.jpg"/></div>

Як ви бачите, я можу вводити лише числові цифри в нашій ОС. Спробуйте для себе. Напишіть код and complie and запустити в редакторі QEMU. Якщо ви робите not встановили QEMU, я детально показую вам, як встановити його в останніх двох навчальних посібниках.

Знайдіть час, щоб по-справжньому переглянути, що я роблю тут, оскільки важливо зрозуміти, що саме так ваш комп'ютер чоботи перед тим, як перейти в 32-х 64-бітний режим.

Наступного тижня ми просто обговоримо концепцію високого рівня про те, як ваш комп'ютер мостить 64-бітну ОС.