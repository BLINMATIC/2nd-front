def GetPercentage(length, percent):
	return length * percent // 100

def CenterPos(l1, l2):
	return l1 // 2 - l2 // 2

def CenterPosPercent(l1, p1):
	return CenterPos(l1, GetPercentage(l1, p1))