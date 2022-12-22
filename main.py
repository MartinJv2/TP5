import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tutoriel Arcade")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, arcade.color.PUMPKIN)
    arcade.draw_rectangle_filled(200, SCREEN_HEIGHT / 2, 30, 60, arcade.csscolor.BROWN, 50)
    arcade.draw_circle_filled(200, 200, 60, arcade.color.BUBBLE_GUM, num_segments=3)
    arcade.draw_circle_filled(400, 200, 60, arcade.color.BUBBLE_GUM)
    arcade.draw_ellipse_filled(500, 50, 100, 10, arcade.color.ANTI_FLASH_WHITE)
    arcade.draw_arc_filled(50, 50, 100, 100, arcade.csscolor.FOREST_GREEN, -90, 0)
    y = SCREEN_HEIGHT / 2 + 40
    arcade.draw_triangle_filled(500, y + 40, 470, y - 20, 530, y - 20, arcade.color.FOREST_GREEN)
    #arcade.draw_line(50, 50, 500, 500, arcade.color.BANANA_YELLOW, 10)


    points = [(50, 50), (500, 500), (300, 300)]
    arcade.draw_line_strip(points, arcade.color.BUFF, 10)

    arcade.finish_render()

    arcade.run()


main()
