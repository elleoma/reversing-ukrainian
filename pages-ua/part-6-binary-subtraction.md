## PART 6 - Бінарне віднімання

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Бінарне віднімання - це не що інше, як додавання негативного значення числа, яке слід відняти. Наприклад, 8 + - 4, вихідна точка була б нульовою, до якої ми рухаємо 8 балів у позитивному напрямку and, тоді чотири точки в негативному напрямку дають значення 4.

Ми представляємо знак знака у двійковому, до якого біт 7 вказує на знак числа, де 0 є позитивним and 1, є негативним.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1537526862141.jpg"/></div>

Вищезазначене представляло б -2.

Ми використовуємо концепцію компліменту Twos, яка інвертує кожен біт and, нарешті, додаючи 1.

Давайте прикладом бінарного 2.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1537526884698.jpg"/></div>

Інвертувати шматочки.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1537526902723.jpg"/></div>

Add 1.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1537526921447.jpg"/></div>

Давайте розглянемо операцію віднімання:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1537526940998.jpg"/></div>

Отже, що таке (1), про який ви можете запитати, це біт переповнення. У майбутніх підручниках ми розглянемо, що ми називаємо прапором переповнення and.

Наступного тижня ми зануримось у довжину слів! Залишайтеся в курсі!