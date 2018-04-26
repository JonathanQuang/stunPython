def union(setA,setB):
	newList = [setA,setB]
	singularList =  [x for y in newList for x in y]
	retList = []
	[retList.append(x) for x in singularList if x not in retList]
	return retList

def intersect(setA,setB):
	return [x for x in setA if x in setB]

def setDiff(setU,setA):
	return [x for x in setU if not(x in setA)]

def symDiff(setA,setB):
	unionSet = union(setA,setB)
	intersectionSet =  intersect(setA,setB)
	return setDiff(unionSet,intersectionSet)

def cartProduct(setA,setB):
	return [[x,y] for x in setA for y in setB]

print("union (1,2) (2,3)" + str(union([1,2],[2,3])))
print("intersect (1,2,3) (2,3,4)  " + str(intersect([1,2,3],[2,3,4])))
print("setDiff (1,2,3) (2,3,4)  " + str(setDiff([1,2,3],[2,3,4])))
print("symDiff (1,2,3) (2,3,4) " + str(symDiff([1,2,3],[2,3,4])))
print("cartProduct (1,2) (red,white) " + str(cartProduct([1,2],['red','white'])))
