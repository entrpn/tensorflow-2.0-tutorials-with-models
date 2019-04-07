from __future__ import absolute_import, division, print_function

import tensorflow as tf
import numpy as np


class Model():
    def __init__(self):
        path_to_file = tf.keras.utils.get_file(
            'shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
        text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
        vocab = sorted(set(text))
        vocab_size = len(vocab)
        print(vocab_size)
        self.char2idx = {u: i for i, u in enumerate(vocab)}
        self.idx2char = np.array(vocab)
        text_as_int = np.array([self.char2idx[c] for c in text])

        def build_model(vocab_size=65, embedding_dim=256, rnn_units=1024, batch_size=1):
            model = tf.keras.Sequential([
                tf.keras.layers.Embedding(vocab_size, embedding_dim,
                                          batch_input_shape=[batch_size, None]),
                tf.keras.layers.LSTM(rnn_units,
                                     return_sequences=True,
                                     stateful=True,
                                     recurrent_initializer='glorot_uniform'),
                tf.keras.layers.Dense(vocab_size)
            ])
            return model
        self.model = build_model()
        checkpoint_dir = './training_checkpoints'
        self.model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
        self.model.build(tf.TensorShape([1, None]))

    def generate_text(self, start_string):
        print('generate_text')
        num_generate = 200

        # Converting our start string to numbers (vectorizing)
        input_eval = [self.char2idx[s] for s in start_string]
        input_eval = tf.expand_dims(input_eval, 0)

        # Empty string to store our results
        text_generated = []

        # Low temperatures results in more predictable text.
        # Higher temperatures results in more surprising text.
        # Experiment to find the best setting.
        temperature = 1.0

        # Here batch size == 1
        self.model.reset_states()
        for i in range(num_generate):
            predictions = self.model(input_eval)
            # remove the batch dimension
            predictions = tf.squeeze(predictions, 0)

            # using a categorical distribution to predict the word returned by the model
            predictions = predictions / temperature
            predicted_id = tf.random.categorical(
                predictions, num_samples=1)[-1, 0].numpy()

            # We pass the predicted word as the next input to the model
            # along with the previous hidden state
            input_eval = tf.expand_dims([predicted_id], 0)

            text_generated.append(self.idx2char[predicted_id])

        return start_string + ''.join(text_generated)
