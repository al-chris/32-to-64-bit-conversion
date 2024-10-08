# 64-to-32-bit-conversion

The function in this repo converts 64 bit integers to 32 bit integers using the IEEE 754 format.

**Below is an explanation of the format**
## **IEEE 745 format**
The **IEEE 754 format** is a standard for representing floating-point numbers in computers. It defines how real numbers, such as fractions and very large or small values, are stored in binary form. This standard is used to ensure that floating-point arithmetic behaves consistently across different computing systems. The IEEE 754 format is available in various sizes, but the most common ones are 32-bit (single-precision) and 64-bit (double-precision).

### **Structure of a 32-bit IEEE 754 Floating Point Number**

A 32-bit floating-point number is divided into three parts: **Sign**, **Exponent**, and **Mantissa** (or **Significand**).

| Sign (1 bit) | Exponent (8 bits) | Mantissa (23 bits) |
|--------------|-------------------|-------------------|
| S            | EEEE EEEE         | MMMMMMMMMMMMMMMMMMMMMMMMM |

1. **Sign (1 bit)**:
   - This bit indicates the sign of the number:
     - `0` = Positive number
     - `1` = Negative number
   - For example, `0` would indicate a positive number like `+5.75`, while `1` would indicate a negative number like `-5.75`.

2. **Exponent (8 bits)**:
   - The exponent determines the range or scale of the number.
   - The exponent is **stored with a bias**. In a 32-bit format, the bias is `127`.
     - For example, an exponent value of `129` actually represents `129 - 127 = 2`.
   - This bias allows the exponent to represent both positive and negative exponents.

3. **Mantissa / Significand (23 bits)**:
   - The mantissa represents the significant digits of the number.
   - In a normalized number, the mantissa always starts with an implicit leading `1`, which is not stored. This is known as the "hidden bit."
     - For example, a mantissa of `0111` actually represents `1.0111`.
   - The 23 bits of the mantissa store the fractional part of the significant digits.
   - More bits in the mantissa lead to higher precision.

### **Example: Representing -5.75 in 32-bit IEEE 754 Format**

1. **Convert the Number to Binary**:
   - `-5.75` is negative, so the **Sign bit** is `1`.
   - The absolute value of `5.75` in binary is `101.11`.
     - `5` in binary is `101`.
     - `.75` in binary is `.11`.

2. **Normalize the Binary Number**:
   - The normalized form of `101.11` is `1.0111 × 2²`.
   - This means the mantissa is `0111` (digits after the leading `1`).
   - The **Exponent** is `2`.

3. **Calculate the Exponent Value**:
   - The bias for a 32-bit float is `127`.
   - Actual Exponent = `127 + 2 = 129`.
   - The stored exponent value is `129`, which in binary is `1000 0001`.

4. **Construct the Mantissa**:
   - The mantissa is `0111`, and we need to fill 23 bits.
   - Pad with zeros to get: `0111 0000 0000 0000 0000 000`.

5. **Combine the Parts**:
   - Sign bit: `1`
   - Exponent: `1000 0001`
   - Mantissa: `0111 0000 0000 0000 0000 000`

6. **Resulting 32-bit Representation**:
   - `1 10000001 01110000000000000000000`

### **Summary of the Format:**
- The IEEE 754 format allows for storing both very large and very small numbers due to the separation of the exponent and the mantissa.
- The **Sign bit** controls the polarity.
- The **Exponent** controls the range.
- The **Mantissa** controls the precision.

### **Advantages of the IEEE 754 Format**:
1. **Consistency**: Arithmetic operations across different platforms yield consistent results.
2. **Range and Precision**: Using separate fields for exponent and mantissa allows representing a wide range of values.
3. **Standardization**: It’s used universally, making it easier to transfer floating-point numbers between systems.

This structure allows for efficient representation and computation with floating-point numbers, while maintaining a balance between range and precision.


## **How a decimal number is stored in 32-bit**

A 32-bit floating-point number follows the IEEE 754 format and is represented as:

```
1 bit for Sign | 8 bits for Exponent | 23 bits for Mantissa (Significand)
```

### Bit Layout:
| Sign (1 bit) | Exponent (8 bits) | Mantissa (23 bits) |
|--------------|-------------------|-------------------|
| S            | EEEE EEEE         | MMMMMMMMMMMMMMMMMMMMMMMMM |

- **Sign (S)**: Determines whether the number is positive (0) or negative (1).
- **Exponent (E)**: The exponent is stored with a bias of 127. This means that the actual exponent is calculated as `Exponent - 127`.
- **Mantissa (M)**: Represents the significant digits of the number, where the leading 1 is implied for normalized numbers.

### Example: Representation of `-5.75` in 32-bit Floating Point

Let's break down the steps to represent `-5.75` in 32-bit floating-point format:

1. **Sign Bit (1 bit)**:
   - Since `-5.75` is negative, the sign bit will be `1`.

2. **Convert to Binary**:
   - The absolute value of `5.75` in binary is:  
     `5` in binary is `101`.  
     `.75` in binary is `.11` (because 0.75 = 0.5 + 0.25).

   - So, `5.75` in binary is `101.11`.

3. **Normalize**:
   - Normalized binary representation: `1.0111 × 2²`.
   - The mantissa is `0111` (trailing part after the leading `1`).
   - The exponent is `2`.

4. **Exponent (8 bits)**:
   - The exponent is `2` and the bias for 32-bit floats is `127`.
   - Therefore, the stored exponent value is `127 + 2 = 129`.
   - `129` in binary is `1000 0001`.

5. **Mantissa (23 bits)**:
   - The mantissa (fractional part) is `0111`, and we need to fill 23 bits.
   - So, it becomes `0111 0000 0000 0000 0000 000`.

6. **Combine the Parts**:
   - Sign = `1`
   - Exponent = `1000 0001`
   - Mantissa = `0111 0000 0000 0000 0000 000`

### Final 32-bit Representation of `-5.75`:

```
1 10000001 01110000000000000000000
```

### Hexadecimal Representation:
- This 32-bit binary value translates to `0xC0B80000` in hexadecimal format.

### Summary:

| Component   | Binary                      | Hexadecimal   |
|-------------|-----------------------------|---------------|
| Sign        | `1`                         | -             |
| Exponent    | `1000 0001`                 | `81`          |
| Mantissa    | `0111 0000 0000 0000 0000 000` | `B80000`      |

This is how `-5.75` is represented in a 32-bit floating point using the IEEE 754 standard.
