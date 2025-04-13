def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # تحديد إذا كان الحرف كبير أو صغير
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')
            # حساب الحرف المشفر
            shifted = (ord(char) - start + shift) % 26
            result += chr(start + shifted)
        else:
            # إبقاء الأحرف غير الأبجدية كما هي
            result += char
    return result

def all_caesar_shifts(text):
    print("جميع احتمالات تشفير Caesar للنص:")
    print("النص الأصلي:", text)
    print("-----------------------")
    for shift in range(1, 26):
        encrypted = caesar_encrypt(text, shift)
        print(f"تحويل +{shift}: {encrypted}")

# أخذ النص من المستخدم
user_input = input("أدخل النص الذي تريد رؤية جميع احتمالات تشفير Caesar له: ")
all_caesar_shifts(user_input)
