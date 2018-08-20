#codingutf-8
import tensorflow as tf


import os
#os.environ["TF_CPP_MIN_LOG_LEVEL"]='1' # 这是默认的显示等级，显示所有信息
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error
#os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' # 只显示 Error

hello = tf.constant('Hello, TensorFlow!')
sess  = tf.Session()
print(sess.run(hello))

def main():
    print("主程序")

if __name__ == '__main__':
    main()