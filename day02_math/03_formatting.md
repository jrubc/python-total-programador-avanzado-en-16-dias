# Format strings

Format strings also known as f-strins, are a way to embed expressions inside strings literals, using curly braces `{}`. There are several ways to format strings:

1. Using function format():

```
color_auto = "red"
license_plate = "GDLJ1921HB"
print("My car is {} and has the license plate {}".format(color_auto, license_plate))
```

2. Using literal strings:

```
color_auto = "red"
license_plate = "GDLJ1921HB"
print(f"My car is {color_auto} and has the license plate {license_plate}")
```
