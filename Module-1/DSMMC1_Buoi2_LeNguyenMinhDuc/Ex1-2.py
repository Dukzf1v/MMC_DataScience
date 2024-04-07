
second = int(input("Enter seconds:"))
hour = second // 3600
minute = (second % 3600) // 60
second = (second % 3600) % 60

print(f"{hour:02d}:{minute:02d}:{second:02d}")
