import argparse
from GameController import *


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
	
   
    #create game controller object
    GAME_CONTROLLER = GameController()

    try:

	GAME_CONTROLLER.GameLoop()
	
    except KeyboardInterrupt:
        if args.clear:
	    GAME_CONTROLLER.GameOver()
    except:
	GAME_CONTROLLER.GameOver()
