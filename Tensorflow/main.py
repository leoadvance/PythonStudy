#codingutf-8
import tensorflow as tf

# create two tfnode
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0)

print(node1, node2)

sess = tf.Session()
print(sess.run([node1, node2]))

node3 = tf.add(node1, node2)
print("node3:", node3)
print("sess.run(node3):", sess.run(node3))

#
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b
print(sess.run(adder_node, {a:3, b:4.5}))
print(sess.run(adder_node, {a: [1, 3], b: [2, 4]}))

add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, {a: 3, b: 4.5}))

# 创建变量
state = tf.Variable(0, name="counter")

# 创建常量
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

init_op = tf.initialize_all_variables()

# 启动图, 运行 op
with tf.Session() as 1:
  # 运行 'init' op
  sess1.run(init_op)
  # 打印 'state' 的初始值
  print sess1.run(state)
  # 运行 op, 更新 'state', 并打印 'state'
  for _ in range(3):
    sess1.run(update)
    print sess1.run(state)

def main():
    print("主程序")

if __name__ == '__main__':
    main()