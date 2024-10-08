import struct

def double_to_float32(double_value):
    # Pack the double value into 64-bit binary representation
    double_bits = struct.unpack('>Q', struct.pack('>d', double_value))[0]
    
    # Extract sign, exponent, and mantissa from the 64-bit double
    sign = (double_bits >> 63) & 0x1           # 1-bit sign
    exponent = (double_bits >> 52) & 0x7FF      # 11-bit exponent
    mantissa = double_bits & 0xFFFFFFFFFFFFF    # 52-bit mantissa
    
    # Handle special cases: Infinity or NaN
    if exponent == 0x7FF:
        # Check if the mantissa is zero (Infinity) or non-zero (NaN)
        new_mantissa = 0 if mantissa == 0 else 0x7FFFFF
        # Set exponent to 0xFF for 32-bit format (Infinity or NaN)
        return struct.unpack('>f', struct.pack('>I', (sign << 31) | (0xFF << 23) | new_mantissa))[0]

    # Calculate new exponent by adjusting the bias from 64-bit to 32-bit
    new_exponent = exponent - 1023 + 127

    # Handle exponent overflow or underflow in 32-bit format
    if new_exponent >= 0xFF:
        # Overflow: Set to infinity
        return struct.unpack('>f', struct.pack('>I', (sign << 31) | (0xFF << 23)))[0]
    elif new_exponent <= 0:
        # Underflow: Set to zero (denormalized numbers not handled here)
        return struct.unpack('>f', struct.pack('>I', (sign << 31)))[0]

    # Convert the mantissa: Truncate from 52 bits to 23 bits
    new_mantissa = mantissa >> (52 - 23)

    # Assemble the 32-bit float representation
    float32_bits = (sign << 31) | (new_exponent << 23) | new_mantissa

    # Convert the 32-bit binary representation back to a float
    return struct.unpack('>f', struct.pack('>I', float32_bits))[0]

# Example usage
double_value = -5.75
float32_value = double_to_float32(double_value)
print(f"64-bit double: {double_value}")
print(f"Converted 32-bit float: {float32_value}")
