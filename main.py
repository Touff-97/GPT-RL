import tcod

def main():
    width, height = 80, 60
    x, y = 40, 30
    
    # Load the font from a file
    tcod.console_set_custom_font('data\dejavu10x10_gs_tc.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)

    # Initialize the root console
    console = tcod.console_init_root(width, height, 'GPT RL', False)

    # Set the background color of the console
    console.bg[0:width, 0:height] = tcod.Color(0, 0, 0)

    # Set the foreground color of the console
    console.fg[0:width, 0:height] = tcod.Color(255, 255, 255)

    while not tcod.console_is_window_closed():
        # Clear the console
        console.clear()

        # Wait for key press and release
        key = tcod.console_wait_for_keypress(True)

        # Move the character based on the input
        if key.vk == tcod.KEY_UP:
            y = max(0, y - 1)
        elif key.vk == tcod.KEY_DOWN:
            y = min(height - 1, y + 1)
        elif key.vk == tcod.KEY_LEFT:
            x = max(0, x - 1)
        elif key.vk == tcod.KEY_RIGHT:
            x = min(width - 1, x + 1)

        # Draw a character on the console
        console.put_char(x, y, 64)

        # Blit the console to the root console (i.e., the main screen)
        tcod.console_blit(console, x, y, width, height, 40, 30, 0)

        # Update the screen
        tcod.console_flush()

        print(x, y)


if __name__ == "__main__":
    main()