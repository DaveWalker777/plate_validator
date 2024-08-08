# Простая библиотека для проверки (валидации) номерного знака транспорта

## Установка
```
pip install -i https://test.pypi.org/simple/ plate-validator-DaveWalker777==0.0.1
```
## Импорт
``` 
from plate_validator_DaveWalker777 import validate_plate
```
## Типы номеров
```
# 1 - легковые, грузовые, автобусы А111АА123
# 2 - такси, маршрутки АО36578
# 3 - мотоциклы, вездеходы 1111АА123
# 4 - военные 0245ОК123
# 5 - полиция А1234123 012А123 5537А123
```

## Использование
В качестве первого аргумента необходимо передать гос. номер в формате string, вторым аргументом следует передать тип номера
``` 
validate_plate(plate, plate_type)
```
В результате будет передано значение True или False
## Пример
``` 
from plate_validator_DaveWalker777 import validate_plate

plate = 'А111АА123'

print(validate_plate(plate, 1))

>>> True
```