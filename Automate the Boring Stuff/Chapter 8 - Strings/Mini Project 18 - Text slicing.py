
url = "https://www.example.com/products/shoes"
filename = "report_2026_final.pdf"
phone = "+61412345678"
sentence = "The quick brown fox"
code = "ABC-2026-XYZ-001"

start = url.find("www.") + 4
end = url.find("/", start)
domain = url[start:end]

filename = filename[:-4]
phone = phone[3:]
sentence = sentence[::-1]

start = code.find('ABC-') + 4
end = code.find('-XYZ', start)
code = code[start:end]

print(domain)
print(filename)
print(phone)
print(sentence)
print(code)

