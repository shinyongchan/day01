## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self,data) :
		self.data = data
		self.link = None

def print_nodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()

def insert_node(find_data, insert_data) :
	global memory, head, current, pre

	if head.data == find_data :      # 첫 번째 노드 삽입
		node = Node(insert_data)
		node.link = head
		head = node
		return

	current = head
	while current.link != None :    # 중간 노드 삽입
		pre = current
		current = current.link
		if current.data == find_data :
			node = Node(insert_data)

			node.link = current
			pre.link = node
			return

	node = Node(insert_data)                   # 마지막 노드 삽입
	current.link = node

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
data_array = ["피카츄", "라이츄", "파이리", "꼬부기", "이상해씨"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	node = Node(data_array[0])			# 첫 번째 노드

	head = node
	memory.append(node)

	for data in data_array[1:] :		# 두 번째 노드부터
		pre = node
		node = Node(data)

		pre.link = node
		memory.append(node)

	print_nodes(head)

	insert_node("피카츄", "잠만보")
	print_nodes(head)

	insert_node("파이리", "어니부기")
	print_nodes(head)

	insert_node("성윤모", "어니부기")
	print_nodes(head)



