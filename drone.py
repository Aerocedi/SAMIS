from djitellopy import Tello
import time

# Create a Tello instance
tello = Tello()

def main():
    # Connect to the Tello Drone
    tello.connect()

    # Check battery
    battery = tello.get_battery()
    print(f"Battery level: {battery}%")

    # Ensure sufficient battery level
    if battery < 20:
        print("Battery too low, charge your Tello first!")
        return

    # Take off
    tello.takeoff()

    # Perform simple flight commands
    tello.move_up(30)
    time.sleep(2)
    tello.rotate_clockwise(90)
    time.sleep(2)
    tello.move_down(30)
    time.sleep(2)

    # Land
    tello.land()

    # Close the connection
    tello.end()

if __name__ == "__main__":
    main()
