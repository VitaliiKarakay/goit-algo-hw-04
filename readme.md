Розмір масиву: 100 \
Insertion Sort: 0.000104 секунд \
Merge Sort: 0.000094 секунд \
Timsort: 0.000007 секунд 

Розмір масиву: 1000 \
Insertion Sort: 0.010126 секунд \
Merge Sort: 0.001111 секунд \
Timsort: 0.000064 секунд 

Розмір масиву: 10000 \
Insertion Sort: 1.018478 секунд \
Merge Sort: 0.014501 секунд \
Timsort: 0.000837 секунд 

Висновки:
Сортування вставками дуже неефективне на великих масивах, оскільки його час виконання швидко зростає через квадратичну складність
O(n^2)

Сортування злиттям показує набагато кращі результати на великих масивах, завдяки своїй логарифмічній складності
O(n*logn), але потребує додаткової пам'яті.

Timsort поєднує переваги обох методів: воно використовує сортування вставками для малих підмасивів, де вставки ефективні, і сортування злиттям для великих масивів. Це робить його більш ефективним, ніж інші алгоритми в більшості реальних сценаріїв.
Таким чином, Timsort є надзвичайно ефективним і тому використовується як вбудований алгоритм сортування в Python.