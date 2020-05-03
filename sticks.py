massiv = ["https://vk.com/sticker/1-19411-128", "https://vk.com/sticker/1-19412-128", "https://vk.com/sticker/1-19413-128", "https://vk.com/sticker/1-19414-128?1", "https://vk.com/sticker/1-19415-128",
          "https://vk.com/sticker/1-19584-128", "https://vk.com/sticker/1-19797-128", "https://vk.com/sticker/1-20012-128", "https://vk.com/sticker/1-20181-128", "https://vk.com/sticker/1-20279-128"]
result = []
for item in massiv:
    try:
        result.append(item.split('-')[1])
    except:
        pass

print(result)
