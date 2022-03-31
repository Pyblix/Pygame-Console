from pygame_console import Console

c = Console(400, 300, background_color = 'gray', caption = 'Hello GitHub', prefix = '', text_color = 'black',
            cursor_color = 'purple', history_color = 'blue',
            fps = 120, resizable = False, text_font = 'comicsans')
c.run()
