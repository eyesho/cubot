import numpy as np
import cv2
import cvui

WINDOW_NAME = 'CVUI Test'
cvui.init(WINDOW_NAME)
frame = np.zeros((200, 400, 3), np.uint8)

# use an array/list because this variable will be changed by cvui
checkboxState = [False]

while True:
    frame[:] = (49, 52, 49)

    # Render the checkbox. Notice that checkboxState is used AS IS,
    # e.g. simply "checkboxState" instead of "checkboxState[0]".
    # Only internally that cvui will use checkboxState[0].
    cvui.checkbox(frame, 10, 15, 'My checkbox', checkboxState)
	
    # Check the state of the checkbox. Here you need to remember to
    # use the first position of the array/list because that's the
    # one being used by all cvui components that perform changes
    # to external variables.
    if checkboxState[0] == True:
        print('Checkbox is checked')
	cvui.update()

    if cv2.waitKey(20) == 27:
        break
