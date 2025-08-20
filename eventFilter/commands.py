

def jog(parent, action, axis=None, direction=None):
	if action:
		return f'Jogging Axis {axis} Dir {direction}'
	else:
		return 'Jogging Stopped'
