# GC-состав является важной характеристикой геномных последовательностей и
# определяется как процентное соотношение суммы всех гуанинов и цитозинов
# к общему числу нуклеиновых оснований в геномной последовательности.
#
# Напишите программу, которая вычисляет процентное содержание символов
# G (гуанин) и C (цитозин) в введенной строке (программа не должна зависеть
# от регистра вводимых символов).

genome = input()
print((genome.upper().count('G') + genome.upper().count('C')) / len(genome) * 100)
