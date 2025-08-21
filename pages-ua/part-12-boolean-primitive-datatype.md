## part 12 - булевий примітивний тип даних

Для повного змісту всіх уроків, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює. https://github.com/mytechnotalent/hacking\_c-\_arm64

Сьогодні ми поговоримо про C ++ _Boolean_ Datatype, який зберігає або _0_ або _1_, щоб представити _0_ для _false _and _1_ для всього _true_.

Цей вид прапора широко використовується в програмуванні загалом, і ми розглянемо ще одну дуже базову програму, щоб зрозуміти її просте використання.

<pre spellcheck="false">#include &lt;iostream&gt;
	
	int main()
	{
	    bool my_bool = true;

	    std::cout &lt;&lt; my_bool &lt;&lt; std::endl;

	    return 0;
	}
</pre>

Ми бачимо, що ми створюємо _bool_ і присвоюємо йому _true _value або _1 _Валанти та друк.

Давайте складемо і посилаємося.

<pre spellcheck="false">g++ -o 0x04_asm64_boolean_primitive_datatype 0x04_asm64_boolean_primitive_datatype.cpp
</pre>

Давайте біжимо.

<pre spellcheck="false">./0x04_asm64_boolean_primitive_datatype
</pre>

Ми просто бачимо наступне.

<pre spellcheck="false">1
</pre>

Він успішно перегукувався _1_ до терміналу stdout. Дуже просто.

Наступного тижня ми налагоджуємо цей дуже простий приклад.