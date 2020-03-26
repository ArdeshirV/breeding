#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" breeding.py - @author: ArdeshirV@protonmail.com 2015-2020, Version 1.0 """
#   Copyright (c) 2015-2020 ArdeshirV@protonmail.com, Licensed under GPLv3+
from platform import system


def main(argv):
    if system() == 'Windows':
        from colorama import init
        init()
        
    try:
        annual_breeding_period = 8
        price, init_number = 25, 40
        chickens = 4 * annual_breeding_period
        breeding_calculator(3, price, init_number, chickens)
        chickens = 6 * annual_breeding_period
        breeding_calculator(3, price, init_number, chickens)
        chickens = 8 * annual_breeding_period
        breeding_calculator(3, price, init_number, chickens)
        chickens = 10 * annual_breeding_period
        return 0
    except Exception as exp:
        print('\033[0;31m' + exp + '\033[0m')
        return -1


def breeding_calculator(count, price, init_number, chickens):
    init_value = init_number * price
    target_number = init_number / 2 * chickens + init_number
    target_value = target_number * price * 0.80
    annual_interest_rate = (target_value / init_value)
    print((("Price$: \033[1;35m{0}\033[0m, Init: \033[1;35m{1}\033[0m, Chi" +
            "ckens: \033[1;35m{2}\033[0m, Rate%: \033[1;35m{3}\033[0m").format(
        price, init_number, chickens, annual_interest_rate)))
    for Index in range(1, count + 1):
        init_value = init_number * price
        target_number = init_number / 2 * chickens + init_number
        target_value = target_number * price * 0.80
        # annual_interest_rate = target_value / init_value
        print(("  \033[1;37m{0}\033[0m-Init: \033[1;32m{1}\033[0m, Value:" +
               " \033[1;32m{2}\033[0m, Target: \033[1;32m{3}\033[0m, Value:" +
               " \033[1;32m{4}\033[0m").format(
            Index, init_number, init_value, target_number, target_value))
        init_number = target_number
    print()


if __name__ == "__main__":
    from sys import argv, exit
    exit(main(argv))
