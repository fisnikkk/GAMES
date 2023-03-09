import streamlit as st
import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the colors
background_color = (0, 0, 0)
paddle_color = (255, 255, 255)
ball_color = (255, 255, 255)

# Set up the paddles and ball
# Set up the paddles and ball
paddle_width = 10
paddle_height = 80
paddle_speed = 5
left_paddle_x = 50
right_paddle_x = 0
right_paddle_y = 0
ball_x = 320
ball_y = 240
ball_radius = 5
ball_dx = -1 # decrease the value to slow down the ball's horizontal movement
ball_dy = -1  # decrease the value to slow down the ball's vertical movement
left_paddle_y = 0  # declare left_paddle_y as a global variable


# Streamlit app
def main():
    global left_paddle_y, right_paddle_y, ball_x, ball_y, ball_dx, ball_dy
    # Set up the starting values for the game objects
    left_paddle_y = 0
    right_paddle_y = 0
    ball_x = 320
    ball_y = 240
    ball_dx = 5
    ball_dy = 5
    right_paddle_x = 640 - paddle_width

    st.title("Pong Game")
    st.write("Use 'W' and 'S' keys to move the left paddle and 'Up' and 'Down' keys to move the right paddle.")

    # Add a start button
    if st.button('Start Game'):
        # Wait 2 seconds to give the user time to see the button
        time.sleep(2)

        # Set up the screen size slider
        st.sidebar.write("## Screen Size")
        screen_width = st.sidebar.slider("Width", 200, 1000, 640, step=10)
        screen_height = st.sidebar.slider("Height", 200, 800, 480, step=10)

        # Set up the screen
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Pong")

        # Set up the paddles
        left_paddle_y = (screen_height - paddle_height) // 2
        right_paddle_y = (screen_height - paddle_height) // 2
        right_paddle_x = screen_width - paddle_width

        # Game loop
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Move the paddles
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and left_paddle_y > 0:
                left_paddle_y -= paddle_speed
            if keys[pygame.K_s] and left_paddle_y + paddle_height < screen_height:
                left_paddle_y += paddle_speed
            if keys[pygame.K_UP] and right_paddle_y > 0:
                right_paddle_y -= paddle_speed
            if keys[pygame.K_DOWN] and right_paddle_y + paddle_height < screen_height:
                right_paddle_y += paddle_speed

                    # Move the ball
            ball_x += ball_dx
            ball_y += ball_dy

            # Bounce the ball off the top and bottom walls
            if ball_y - ball_radius < 0 or ball_y + ball_radius > screen_height:
                ball_dy = -ball_dy

            # Bounce the ball off the left paddle
            if ball_x - ball_radius < left_paddle_x + paddle_width and \
                ball_y + ball_radius > left_paddle_y and \
                ball_y - ball_radius < left_paddle_y + paddle_height:
                    ball_dx = -ball_dx

            # Bounce the ball off the right paddle
            if ball_x + ball_radius > right_paddle_x and \
            ball_y + ball_radius > right_paddle_y and \
            ball_y - ball_radius < right_paddle_y + paddle_height:
                ball_dx = -ball_dx

            # Check if the ball goes out of bounds
            if ball_x - ball_radius < 0:
                st.warning("Right player wins!")
                # Reset ball position and direction
                ball_x = screen_width // 2
                ball_y = screen_height // 2
                ball_dx = -ball_dx
                ball_dy = -ball_dy
            if ball_x + ball_radius > screen_width:
                st.warning("Left player wins!")
                # Reset ball position and direction
                ball_x = screen_width // 2
                ball_y = screen_height // 2
                ball_dx = -ball_dx
                ball_dy = -ball_dy

            # Fill the screen with the background color
            screen.fill(background_color)

            # Draw the paddles and ball
            pygame.draw.rect(screen, paddle_color, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
            pygame.draw.rect(screen, paddle_color, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
            pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

            # Update the display
            pygame.display.update()

            # Add a delay to slow down the game
            pygame.time.delay(20)

    # Quit Pygame
    pygame.quit()
if __name__ == "__main__":
    main()

