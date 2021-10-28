import tensorflow as tf
from tensorflow.keras import layers


class LowRankDense(layers.Layer):
    def __init__(self, num_outputs, init_rank=1):
        super(LowRankDense, self).__init__()
        self.num_outputs = num_outputs
        self.num_inputs = None

        self.init_rank = init_rank
        self.rank = 0
        self.kernel_us = []
        self.kernel_vs = []
        self.b = None

    def build(self, input_shape):
        self.num_inputs = int(input_shape[-1])
        b_init = tf.zeros_initializer()
        self.b = self.add_weight(
            shape=(self.num_outputs,),
            initializer=b_init,
            trainable=True,
            name="bias"
        )
        self.add_rank(self.init_rank)  # initial ranks

    def add_rank(self, num_ranks):
        w_init = tf.random_normal_initializer()
        kernel_u = self.add_weight(
            shape=(self.num_inputs, num_ranks),
            initializer=w_init,
            trainable=True,
            name=f"u_rank-{self.rank}-{self.rank + num_ranks}"
        )
        kernel_v = self.add_weight(
            shape=(num_ranks, self.num_outputs),
            initializer=w_init,
            trainable=True,
            name=f"v_rank-{self.rank}-{self.rank + num_ranks}"
        )
        self.kernel_us.append(kernel_u)
        self.kernel_vs.append(kernel_v)
        self.rank += num_ranks

    def kernel_u(self):
        return tf.concat(self.kernel_us, axis=1)

    def kernel_v(self):
        return tf.concat(self.kernel_vs, axis=0)

    def call(self, inputs, *args, **kwargs):
        return inputs @ (self.kernel_u() @ self.kernel_v()) + self.b

    def effective_weights(self):
        return [(self.kernel_u() @ self.kernel_v()).numpy(), self.b.numpy()]
