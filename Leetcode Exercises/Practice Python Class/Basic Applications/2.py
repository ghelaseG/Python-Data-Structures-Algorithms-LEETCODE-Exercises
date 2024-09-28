"""
Write a Python class to convert a Roman numeral to an integer.
"""

class RomanInt:
    def rom_to_int(self, rom):
        roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(rom)):
            if i > 0 and roman_value[rom[i]] > roman_value[rom[i - 1]]:
                int_val += roman_value[rom[i]] - 2 * roman_value[rom[i - 1]]
            else:
                int_val += roman_value[rom[i]]
        return int_val 

print(RomanInt().rom_to_int('MMMCMLXXXVI'))
print(RomanInt().rom_to_int('MMMM'))
print(RomanInt().rom_to_int('XXV'))