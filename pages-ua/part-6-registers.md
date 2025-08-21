## PART 6 - Реєстри

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

У нашому мікропроцесорі ARM є внутрішнє сховище, яке робить будь -яку операцію, повинна швидше, оскільки зовнішнього доступу до пам'яті не потрібен. Є два режими, користувач і великий палець. Ми будемо зосереджуватись на режимі користувача, оскільки в кінцевому рахунку орієнтовані на розробку для системи на мікросхемі в межах ОС Linux, а не на голій метальній програмі, що краще підходить на пристрій мікроконтролера.

У режимі користувача у нас є 16 реєстрів та реєстр CPSR, який має довжину слова, кожен, що становить 32-бітні або 8 байт кожен.

Реєстри R0 до R12-це багатоцільові регістри, до яких R13-R15 мають унікальну мету, а також CPSR. Давайте подивимось на просту таблицю, щоб проілюструвати.

<pre spellcheck="false">R0 GPR (General-Purpose Register)
R1 GPR (General-Purpose Register)
R2 GPR (General-Purpose Register)
R3 GPR (General-Purpose Register)
R4 GPR (General-Purpose Register)
R5 GPR (General-Purpose Register)
R6 GPR (General-Purpose Register)
R7 GPR (General-Purpose Register)
R8 GPR (General-Purpose Register)
R9 GPR (General-Purpose Register)
R10 GPR (General-Purpose Register)
R11 GPR (General-Purpose Register)
R12 GPR (General-Purpose Register)
R13 Stack Pointer
R14 Link Register
R15 Program Counter
CPSR Current Program Status Register
</pre>

Важливо, щоб ми розуміли регістри дуже детально. На даний момент ми розуміємо, що R0-R12 є загальним призначенням і буде використовуватися для маніпулювання даними, коли ми будуємо наші програми та додатково, коли ви зламаєте або зворотні інженерні бінарні бінарні з шестигранного сміттєзвалища на мобільному телефоні чи іншому ARM Будь -яка така вищезгадана операція.

Чіп, з яким ми працюємо, відомий як машина для завантаження та зберігання. Це означає, що ми завантажуємо регістр із вмістом регістра або місця пам'яті, і ми можемо зберігати регістр із вмістом пам'яті або реєстрації. Наприклад:

<pre spellcheck="false">ldr, r4, [r10] @ 
&nbsp;&nbsp;&nbsp; load r4 with the contents of r10, if r10 had the decimal value of 
&nbsp;&nbsp;&nbsp; say 22, 22 would go to r4

str, r9, [r4] @ 
&nbsp;&nbsp;&nbsp; store r9 contents into location in r4, if r9 had 0x02 hex, 
&nbsp;&nbsp;&nbsp; 0x02 would be stored into location r4
</pre>

@ Просто вказує на компілятора, що те, що слідує за ним у заданому рядку, є коментарем і ігнорувати.

Наступні кілька тижнів ми знайдемо свій час і подивимось на кожну з реєстрів спеціального призначення, щоб ви чудово розуміли, що вони роблять.

Наступного тижня ми зануримося в додаткову інформацію про лічильник програми! Залишайтеся в курсі!