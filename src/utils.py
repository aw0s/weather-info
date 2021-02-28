#!/usr/bin/env python
# -*- coding: utf-8 -*-


def kelvin_to_celsius(kelvin_degrees: float, decimal_places: int) -> float:
    celsius_degrees = round(kelvin_degrees - 273.5, decimal_places)

    return celsius_degrees
