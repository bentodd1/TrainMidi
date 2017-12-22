Using Magenta to generate a song.

Magenta makes using machine learning to make songs much easier.  It has everything pre-packaged

Before you get started creating a song in Magenta you will have to do the following
Pre Magenta Steps
1. Install Magenta https://github.com/tensorflow/magenta
2. Install Tensorflow https://github.com/tensorflow/tensorflow
3. Install Dependencies
4. Find a group of midi sequences


First you need to install magenta and tensor flow on your machine.

Once those are installed, there are 4 steps needed to generate midi sequences.

1. Convert To Note Sequences
2. Create DataSet
3. Train
4. Generate

Here are the commands I ran for each.  Now I have new sequences to enjoy!

convert_dir_to_note_sequences --input_dir=~/Downloads/Midi/ --output_file=~/Downloads/techno_sequences.tfrecord --recursive

melody_rnn_create_dataset \
--config='basic_rnn' \
--input=~/Downloads/techno_sequences.tfrecord \
--output_dir=/Users/bentodd/Downloads/Midi/data \
--eval_ratio=0.10

melody_rnn_train \
--config=basic_rnn \
--run_dir=/Users/bentodd/Downloads/Midi/train \
--sequence_example_file=/Users/bentodd/Downloads/Midi/data/training_melodies.tfrecord \
--num_training_steps=20000 

melody_rnn_generate \
--config=basic_rnn \
--run_dir=/Users/bentodd/Downloads/Midi/train \
--output_dir=/Users/bentodd/Downloads/Midi/generate \
--num_outputs=3 \
--num_steps=256 \
--primer_melody=[67]




