import turtle

def draw_pifagoras_tree(branch_len, level):
    if level == 0:
        return
    turtle.forward(branch_len)
    turtle.left(45)
    draw_pifagoras_tree(0.7 * branch_len, level-1)
    turtle.right(90)
    draw_pifagoras_tree(0.7 * branch_len, level-1)
    turtle.left(45)
    turtle.backward(branch_len)

def main():
    turtle.speed(0)  # Тут можна задати швидкість візуалізації
    turtle.left(90)
    turtle.up()
    turtle.backward(200)
    turtle.down()
    draw_pifagoras_tree(100, 8)  # Змінюйте другу цифру на потрібний рівень рекурсії
    turtle.exitonclick()

if __name__ == "__main__":
    main()
