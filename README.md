# Pygame-Console

### Summary
This project allows you to create a console for your Pygame project.

### Usage
Place the file in your Python lib folder or in your project folder.
`import pygame_console`

### Libraries used
* Pygame
* os
* [pygame_textinput](https://github.com/Nearoo/pygame-text-input)
Thanks to Nearoo for this lib (:

### Arguments
**Class "Console"**
| Argument | Description |
|------------|--------------|
| width | console width
| height | console height
| background_color | console background color
| caption | window caption
| prefix | prefix for entered text
| icon | window icon
| text_color | input text color
| cursor_color | cursor color
| history_color | written text color
| fps | frames per second for console
| resizable | boolean if resizing is allowed or not
| text_font | font to use for the input text
| history_font | font to use for the written text

### Example
This is the simplest example for the Console:
```
from pygame_console import Console

c = Console(400, 300)
c.run()
```

### Method example
You can use threads in your program for the console and communicate with the function `cprint(_yourtext_)`.

### Another example
```
from pygame_console import Console

c = Console(400, 300, background_color = 'gray', caption = 'Hello GitHub', prefix = '', text_color = 'black',
            cursor_color = 'purple', history_color = 'blue',
            fps = 120, resizable = False, text_font = 'comicsans')
c.run()

```

### Modifying
You can modify the console as you wish. Go to the `check_input` function and add your conditions with `if`/`else`.

```
    def check_input(self, input):
        if input == 'github':
            return 'Hello GitHUb'
        else:
            return input
```

### Download
* pygame_console.py
* console_example.py
* another_console_example.py
