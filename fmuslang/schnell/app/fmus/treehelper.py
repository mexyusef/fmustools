def get_all_tree_children(akar):
	children = []

	def get_children(root):
		if len(root.children) > 0:
			for anak in root.children:
				children.append(anak)
				get_children(anak)

	get_children(akar)
	return children


def get_last_absolute_children(akar):
	children = get_all_tree_children(akar)
	if len(children) > 0:
		return children[-1]
	return None


def get_direct_children(akar):
	return [node for node in akar.children]


def get_last_direct_children(akar):
	children = [node for node in akar.children]
	if len(children) > 0:
		return children[-1]
	return None


def set_attr_direct_children(akar, attribute, value):
	for node in akar.children:
		setattr(node, attribute, value)


def set_attr_direct_children_cond(akar, attribute, value_yes, value_no, condition):
	for node in akar.children:
		setattr(node, attribute, value_yes if condition else value_no)


def print_ready_children(item):
	children = get_all_tree_children(item)
	print_ready = [node.level*'  ' + node.original for node in children]
	print_ready = '\n'.join(print_ready)
	return print_ready


def get_root(node):
	if not hasattr(node, 'parent') or not node.parent:
		return node
	return get_root(node.parent)


def get_siblings_all(akar, include_me=True):
	if include_me:
		return [node for node in akar.parent.children]
	else:
		return [node for node in akar.parent.children if node != akar]


def get_siblings_before(akar):
	# aku = -1
	# for index, node in enumerate(akar.parent.children):
	# 	if node == akar:
	# 		aku = index
	# 		break
	aku = [index for index,item in enumerate(akar.parent.children) if item == akar] [0]
	return akar.parent.children[:aku]


def get_siblings_after(akar):
	aku = [index for index,item in enumerate(akar.parent.children) if item == akar] [0]
	return akar.parent.children[aku+1:]


def recursive_callback_for_siblings_after(akar, callback):
	for sepupu in get_siblings_after(akar):
		callback(sepupu)
		for anak_cucu in get_all_tree_children(sepupu):
			callback(anak_cucu)
			recursive_callback_for_siblings_after(anak_cucu, callback)


# def recursive_callback_for_direct_children(akar, callback):
# 	for anak_cucu in get_direct_children(akar):
# 		callback(anak_cucu)
# 		recursive_callback_for_direct_children(anak_cucu, callback)


def recursive_callback_for_bawahan(akar, callback):
	# direct children dulu
	for anak_cucu in get_all_tree_children(akar):
		callback(anak_cucu)
	recursive_callback_for_siblings_after(akar, callback)
