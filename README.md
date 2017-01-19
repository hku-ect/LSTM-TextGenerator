# LSTM-TextGenerator
An example of a LSTM network implementation to generate text on a word-for-word basis using tensorflow and keras. Based on a keras example.

## LSTM
LSTM stands for Long Short Term Memory, which is a form of network that you can train on input data to generate output of similar data. More information: http://colah.github.io/posts/2015-08-Understanding-LSTMs/

## How to use
The current example is trained on Alice in Wonderland, and ready to go. Use <b>lstm_generate.py</b> to generate runs of 400 words of varying diversities.

You can provide new full-text input data in the root folder, and then replace the following line at the beginning of <b>lstm_train.py</b>:

<code>
fileName = "[YOUR FILENAME]"
</code>

Then run the lstm_train.py file, and let it finish (this may take some time). You can edit the amount of "epochs" (training runs, default set to 40) to a smaller number to speed up training (but decrease quality of the lstm network). You can also increase it to get better results if you notice the output is poor. Make sure the input-text is long enough (the more data it has to train on, the better it will know what to do)!

After training it will do a single generation run, and output a "hdf5" file. Copy the filename, and edit the <b>lstm_generate.py</b> in a similar way to include your own input-data and the generated file:

<code>fileName = "[YOUR FILENAME]"</code>

<code>modelData = "[GENERATED HDF5 FILENAME]</code>

Then simply run the <b>lstm_generate.py</b> as many times as you want to generate more output text. You can edit the amount of text generated at line 94 (currently it generates 400 words):

<code>for i in range(400):</code>

## Dependencies
The provided code runs on a couple of dependencies:
* Python 2.7.10
* Keras 1.1.0
* Tensorflow 0.12
* scipy
* numpy
* h5py

People working on Windows are recommended to use MiniConda (http://conda.pydata.org/miniconda.html) or Anaconda to simplify the install-procedure for these dependencies, because they cannot be easily installed through pip on Windows. UNIX users should be able to use pip.

If you're new to working with Python, I suggest using PyCharm: https://www.jetbrains.com/pycharm/

### Known issues with keras & tensorflow 0.12
You may encounter an issue when attempting to run this from a fresh install, because keras still relies on an older version of tensorflow. To resolve this, modify the import of "control_flow_ops" in the ''tensorflow_backend.py'' file (part of keras 1.1.0) to the following:

<code>from tensorflow.python.ops import control_flow_ops</code>

Then search through the file for any point where control_flow_ops is used, and use it directly (without the library prefix) as follows:

<code>
x = control_flow_ops.cond(tf.cast(condition, 'bool'),
                          lambda: then_expression,
                          lambda: else_expression)
</code>
